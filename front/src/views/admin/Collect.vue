<template>
  <div>
    <b-container :fluid='true' style="margin-top: 50px">
      <b-table striped hover :items="collectionApis" :fields="fields">
        <template v-slot:cell(operator)="item">
          <!-- `data.value` is the value after formatted by the Formatter -->
          <b-button @click="showUpdateOrCreateModal(item)">
            编辑
          </b-button>
          <b-button @click="showCollectionOptions(item)">
            开始采集
          </b-button>
          <b-button @click="showLog(item)">
            日志
          </b-button>
          <b-button @click="showBindTypeModel(item)">
            绑定分类
          </b-button>
        </template>
      </b-table>
    </b-container>
    <b-modal title="采集" ref="collectModal" ok-title="开始采集" cancel-title="取消" @ok="startCollect">
      采集时间： <b-input v-model="collectionHour"></b-input>
    </b-modal>

    <b-modal title="编辑" ref="updateOrCreateModal" ok-title="确定" cancel-title="取消" @ok="updateOrCreate">
      名称： <b-input v-model="currentCollectionApi.name"></b-input>
      key： <b-input v-model="currentCollectionApi.key"></b-input>
      链接api <b-input v-model="currentCollectionApi.url"></b-input>
<!--      分类绑定：<div v-for="item in currentCollectionApi.bindId" :key="item.apiId">{{item}}</div>-->
    </b-modal>

    <b-modal title="日志" ref="logModal" ok-disabled cancel-title="取消" @hidden="closeLog">
      <div v-html="collectionLog"></div>
    </b-modal>

    <b-modal title="分类绑定" ref="bindTypeModal" cancel-title="取消" @hidden="closeBindType" @ok="submitBindType">
      <div v-for="item in currentCollectionApi.bindId" :key="item.apiId">
        {{item.apiName}}:
        <b-form-select v-model="selectApiIdToSystemId[item.apiId]" :options="currentTypeOptions" size="sm" class="mt-3"></b-form-select>
      </div>
      <b-button @click="refreshCollectionTypes">刷新</b-button>
      <b-button @click="autoBindTypes">自动整理</b-button>
    </b-modal>

  </div>
</template>

<script>
import {
  getAll,
  getTaskByKey,
  refreshCollectionTypesByKey,
  startCollection,
  updateOrCreateCollection
} from "@/apis/collection";
import {getTypes} from "@/apis/video";

export default {
  name: "Collect",
  data() {
    return {
      collectionApis: [],
      currentCollectionApi: {},
      collectionHour: 24,
      currentTypeOptions: [],  //分类选项
      systemTypeIdToName: {},
      selectApiIdToSystemId: {},
      intervalTask: [],
      collectionLog: '',
      allTypeList: [],
      fields: [{
        key: 'name',
        label: '名称'
      },
        {
          key: 'key',
          label: '标志'
        },
        {
        key: 'url',
        label: '链接'
      },
        {
          key: 'operator',
          label: '操作'
        },
      ]
    }
  },
  methods: {
    getCollectionApis() {
      getAll().then(res => {
        this.collectionApis = res
      });
    },
    showCollectionOptions(current) {
      this.currentCollectionApi = current.item
      this.$refs.collectModal.show()
    },
    startCollect() {
      const key = this.currentCollectionApi.key
      const hours = this.collectionHour
      startCollection(key, hours).then(res => {
        console.log(res);
      })
      this.$refs.collectModal.hide()
    },
    showLog(current) {
      this.collectionLog = ''
      this.$refs.logModal.show()

      let task  = setInterval(async () => {
        const res = await getTaskByKey(current.item.key)
          this.collectionLog = res.data.join('<br/>')
      }, 1000)
      this.intervalTask.push(task)
    },
    closeLog() {
      console.log('close log')
      for (let task of this.intervalTask) {
        window.clearInterval(task);
      }
      this.intervalTask = []
      this.$refs.logModal.hide()
    },
    showBindTypeModel(current){
      this.currentCollectionApi = current.item
      this.selectApiIdToSystemId = {}
      this.systemTypeIdToName = {}
      this.refreshSelectOptions()
      this.$refs.bindTypeModal.show()
    },
    refreshSelectOptions() {
      this.currentTypeOptions = this.allTypeList.map(item => {
        return {
          'text': item.name,
          'value': item.id
        }
      })
      for (let item of this.currentCollectionApi.bindId) {
        this.systemTypeIdToName[item.systemId] = item.typeName
        this.selectApiIdToSystemId[item.apiId] = item.systemId
      }
    },
    closeBindType() {

    },
    submitBindType() {
      let newBindId = []
      for (let item of this.currentCollectionApi.bindId) {
        // if (item.apiId in  this.selectApiIdToSystemId)
        const isBind = item.apiId in this.selectApiIdToSystemId
        newBindId.push({
          apiId: item.apiId,
          apiName: item.apiName,
          systemId: isBind ? this.selectApiIdToSystemId[item.apiId] : null,
          typeName: isBind ? this.systemTypeIdToName[this.selectApiIdToSystemId[item.apiId]] : null
        })
      }
      this.currentCollectionApi.bindId = newBindId
      this.updateOrCreate()
    },
    getAllType(){
      getTypes().then(res => {
        this.allTypeList = res
      })
    },
    refreshCollectionTypes() {
      let apiIds = this.currentCollectionApi.bindId.map(item => {
        return item.apiId;
      })
      // 获取 第三方的分类
      refreshCollectionTypesByKey(this.currentCollectionApi.key).then(res => {
        for (let item of res.data) {
          if (apiIds.indexOf(item.id) === -1) {
            apiIds.push(item.id)
            this.currentCollectionApi.bindId.push({
              systemId: null,
              apiId: item.id,
              apiName: item.name,
              typeName: null
            })
          }
        }
        this.refreshSelectOptions()
      })
    },
    // 自动整理分类
    autoBindTypes() {

      let systemNameToId = {}
      for (let item of this.allTypeList) {
        systemNameToId[item.name] = item.id
      }
      console.log(this.currentCollectionApi.bindId);
      for (let item of this.currentCollectionApi.bindId) {
        if (item.apiName in systemNameToId) {
          item.systemId = systemNameToId[item.apiName]
          item.typeName = item.apiName
        }
      }
      this.refreshSelectOptions()
    },
    showUpdateOrCreateModal(current) {
      this.currentCollectionApi = current.item
      this.$refs.updateOrCreateModal.show()
      this.getAllType()
    },
    updateOrCreate() {
      updateOrCreateCollection(this.currentCollectionApi).then(res => {
        console.log(res);
      })
    }

  },
  created() {
    this.getCollectionApis()
    this.getAllType()
  },
  beforeDestroy() {
    this.closeLog()
  }
}
</script>

<style scoped>

</style>