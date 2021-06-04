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
    </b-modal>

  </div>
</template>

<script>
import {getAll, getTaskByKey, startCollection, updateOrCreateCollection} from "@/apis/collection";
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
      this.currentTypeOptions = []
      this.selectApiIdToSystemId = {}
      this.systemTypeIdToName = {}
      console.log(this.currentCollectionApi);
      for (let item of this.allTypeList) {
        this.currentTypeOptions.push({
          'text': item.name,
          'value': item.id
        })
      }
      for (let item of current.item.bindId) {
        this.systemTypeIdToName[item.systemId] = item.typeName
        this.selectApiIdToSystemId[item.apiId] = item.systemId
      }
      this.$refs.bindTypeModal.show()
    },
    closeBindType() {

    },
    submitBindType() {
      for (let item of this.currentCollectionApi.bindId) {
        item.bindId = {
          apiId: item.apiId,
          apiName: item.apiName,
          systemId: this.selectApiIdToSystemId[item.apiId],
          typeName: this.systemTypeIdToName[this.selectApiIdToSystemId[item.apiId]]
        }
      }
      console.log('-------------------', this.currentCollectionApi);
      this.updateOrCreate()
    },
    getAllType(){
      getTypes().then(res => {
        this.allTypeList = res
      })
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