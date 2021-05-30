<template>
  <div>
    <b-container :fluid='true' style="margin-top: 50px">
      <b-table striped hover :items="collectionApis" :fields="fields">
        <template v-slot:cell(operator)="item">
          <!-- `data.value` is the value after formatted by the Formatter -->
          <b-button>
            编辑
          </b-button>
          <b-button @click="showCollectionOptions(item)">
            开始采集
          </b-button>
          <b-button @click="showLog(item)">
            日志
          </b-button>
        </template>
      </b-table>
    </b-container>
    <b-modal title="采集" ref="collectModal" ok-title="开始采集" cancel-title="取消" @ok="startCollect">
      采集时间： <b-input v-model="collectionHour"></b-input>
    </b-modal>
    <b-modal title="日志" ref="logModal" ok-disabled cancel-title="取消" @hidden="closeLog">
      <div v-html="collectionLog"></div>
    </b-modal>
  </div>
</template>

<script>
import {getAll, getTaskByKey, startCollection} from "@/apis/collection";

export default {
  name: "Collect",
  data() {
    return {
      collectionApis: [],
      currentCollectionApi: null,
      collectionHour: 24,
      intervalTask: [],
      collectionLog: '',
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
    }
  },
  created() {
    this.getCollectionApis()
  },
  beforeDestroy() {
    this.closeLog()
  }
}
</script>

<style scoped>

</style>