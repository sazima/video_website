<template>
  <div>
    <b-container :fluid='true'>
      <b-row align-h="center" style="margin-top: 89px">
        <b-col cols="12" md="8">
          <b-alert show variant="info">{{ videoInfo.name }} -- {{ playName }}</b-alert>
        </b-col>
      </b-row>
      <b-row align-h="center">
        <b-col cols="12" md="8">
          <tanmu-player ref="tanmuPlayer" ></tanmu-player>
        </b-col>
      </b-row>
      <b-row align-h="center" style="margin-top: 20px">
        <b-col cols="9" md="7">
          <b-input-group  >
            <b-form-input placeholder="弹幕内容" v-model="inputTanmu">

            </b-form-input>
            <b-input-group-append>

              <b-button variant="outline-primary" @click="submitTanmu" :disabled="!canSubmitTanmu || !inputTanmu"
                        style="float: right">{{ sendTanmuButtonText }}
              </b-button>
            </b-input-group-append>
          </b-input-group>
        </b-col>
        <b-col cols="3" md="1">
          <b-button>投屏</b-button>
        </b-col>
      </b-row>

      <b-row align-h="center" style="background-color: #fff; margin-top: 20px">
        <b-col cols="12" md="8">
          <b-card>
            <b-tabs card style="background-color: #fff">
              <b-tab v-for="(group, index) in videoInfo.videoPlayGroupList"
                     :key="index" :title="group.fromName" ref="tab" :active="false">
                <b-button v-for="(urlName, index) in group.videoPlayUrlVoList" :key="index" @click="startPlay(urlName, group.fromName)"
                          variant="outline-primary">
                    {{ urlName.name}}
                </b-button>
              </b-tab>
            </b-tabs>
          </b-card>
        </b-col>
      </b-row>
      <b-row align-h="center" style="background-color: #fff; margin-top: 20px">
        <b-col cols="12" md="8">
          <b-card>
            <b-media>
              <template v-slot:aside>
                <b-img :src="videoInfo.picture" blank-color="#ccc" width="64" height="90" alt="placeholder"></b-img>
              </template>
              <h5 class="mt-0">{{ videoInfo.name }}</h5>
              <p v-html="videoInfo.content"></p>
            </b-media>
          </b-card>
        </b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import {addTanmu, getTanmu, getVideoById} from "@/apis/video";
// import tanmu from '../components/tanmu'
import TanmuPlayer from "@/components/TanmuPlayer/index";

export default {
  name: "Play",
  components: {TanmuPlayer},
  data() {
    return {
      player: null,
      av: '',
      inputTanmu: '',
      sendTanmuButtonText: '发射',
      videoInfo: {},
      urlName: {},
      canSubmitTanmu: true,
      fromName: '',  // 链接来源
      playName: '',
      tanmuList: {}
    };
  },
  methods: {
    submitTanmu() {
      // 为空不能发送
      if (!this.inputTanmu.trim()) {
        return
      }
      this.canSubmitTanmu = false
      const currentTime = this.$refs.tanmuPlayer.player.cache_.currentTime
      let tanmuData = {
        av: this.av,
        playUrl: this.arc,
        currentTime: currentTime,
        fromName: this.fromName,
        playName: this.playName,
        content: this.inputTanmu
      }
      addTanmu(tanmuData)  // 调用接口
      this.$refs.tanmuPlayer.pushTanmu(tanmuData)
      this.inputTanmu = ''
      let remainSenconds = 10  // 设置10s间隔, 不能发送太频繁
      let i = setInterval(() => {
        if (remainSenconds <= 0) {
          this.sendTanmuButtonText = '发射'
          this.canSubmitTanmu = true
          clearInterval(i)
          return
        }
        this.sendTanmuButtonText = `${remainSenconds}s`
        remainSenconds--
      }, 1000)
    },
    initTanmu() {
      getTanmu({
        av: this.av,
        playName: this.playName,
        fromName: this.fromName,
        playUrl: ""
      }).then(data => {
        console.log('获取弹幕成功', data)
        this.tanmuList = data
        this.$refs.tanmuPlayer.setTanmu(data)
      }).catch(err => {
        console.log('获取弹幕失败', err)
      })
    },
    startPlay(urlName, fromName) {
      this.playName = urlName.name
      this.fromName = fromName
      document.title = this.videoInfo.name + this.playName
      this.$refs.tanmuPlayer.startPlay(urlName)
      this.initTanmu()
    }
  },
  mounted() {
    this.av = this.$route.query.av
    getVideoById(this.av).then(data => {
      this.videoInfo = data
      this.videoInfo.content = "&nbsp;&nbsp;&nbsp;&nbsp;" + data.content.replace(/\s*/g, "").replace(/<br\/>*/, '<br> &nbsp;&nbsp;&nbsp;&nbsp;');
      this.startPlay(this.videoInfo.videoPlayGroupList[0].videoPlayUrlVoList[0], this.videoInfo.videoPlayGroupList[0].fromName)
    })
  }
}
</script>

<style scoped>

</style>
