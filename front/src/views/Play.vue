<template>
  <div>
    <b-container :fluid='true'>
      <b-row align-h="center" style="margin-top: 89px">
        <b-col cols="12" md="8">
          <b-alert show variant="info">{{ videoInfo.name }} -- {{ playName }}</b-alert>
        </b-col>
      </b-row>
      <b-row align-h="center">
        <b-col cols="12" md="8" ref="videoCol">
          <video id="vid1" ref="videoPlayer" class="video-js" controls playsinline>
            <source type="application/x-mpegURL"/>
          </video>
          <tanmu ref="tanmu" v-show='showTanmu' :height="danmuContainerHeight" :width="danmuContainerWidth"></tanmu>
        </b-col>
      </b-row>
      <b-row align-h="center" style="margin-top: 20px">
        <b-col cols="9" md="7">
          <b-input placeholder="发送弹幕, 请注意弹幕礼仪" v-model="inputTanmu"></b-input>
        </b-col>
        <b-col cols="3" md="1">
          <b-button variant="outline-primary" @click="submitTanmu" :disabled="!canSubmitTanmu || !inputTanmu"
                    style="float: right">{{ sendTanmuButtonText }}
          </b-button>
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
import {addTanmu, getTanmu, getVideoById} from "../apis/video";
import tanmu from '../components/tanmu'
import {requestFullScreen, clearEventListener, isIOS} from "../utils/utils";

export default {
  name: "Play",
  components: {tanmu},
  data() {
    return {
      player: null,
      src: '',
      av: '',
      inputTanmu: '',
      sendTanmuButtonText: '发射',
      showTanmu: true,
      videoInfo: {},
      currentPlayerTime: -1,
      danmuContainerHeight: 90,
      danmuContainerWidth: 90,
      canSubmitTanmu: false,
      fromName: '',  // 链接来源
      playName: '',
      tanmuList: {}
    };
  },
  methods: {
    createPlayer() {
      // // 播放参数
      let options = {
        controls: true, // 是否显示底部控制栏
        preload: "auto", // 加载<video>标签后是否加载视频
        playbackRates: [0.5, 1, 1.5, 2],// 倍速播放
        aspectRatio: '16:9',
        fluid: true,
        sources: [{
          type: "application/x-mpegURL",
          src: this.src
        }],
      };
      this.player = this.$video(this.$refs.videoPlayer, options)

      this.player.ready(() => {
        this.player.tech_.off('dblclick');
        this.player.on('dblclick', () => {
          this.switchFull()
        })
        if (!isIOS()) {
          this.replaceFullScreenButton()
        }
        // // 播放条事件
        this.player.on("timeupdate", this.timeUpdate);
      })
    },
    startPlay(urlName, fromName) {
      this.src = urlName.url
      this.playName = urlName.name
      this.fromName = fromName
      document.title = this.videoInfo.name + this.playName
      if (!this.player) {
        this.createPlayer()
      } else {
        this.player.src(urlName.url)
        this.player.load()
        this.player.play()
      }
      this.initTanmu()
    },
    // 根据播放条发送弹幕
    timeUpdate() {
      this.danmuContainerHeight = this.player.el_.clientHeight
      this.danmuContainerWidth = this.player.el_.clientWidth
      const time = this.player.cache_.currentTime
      if (time === 0) {
        this.canSubmitTanmu = false
        return
      }
      this.canSubmitTanmu = true
      let previouseTime = this.currentPlayerTime
      this.currentPlayerTime = time
      if (parseInt(previouseTime) === parseInt(this.currentPlayerTime)) {
        return
      }
      let currentTanmuList = this.tanmuList[parseInt(this.currentPlayerTime)]
      if (!currentTanmuList) {
        return
      }
      for (let tanData of currentTanmuList) {
        setTimeout(() => {
          console.log('发送弹幕, ', tanData.content)
          this.$refs.tanmu.add(tanData)
        }, (tanData.current_time - this.currentPlayerTime) * 1000)
      }
    },
    submitTanmu() {
      // 为空不能发送
      if (!this.inputTanmu.trim()) {
        return
      }
      this.canSubmitTanmu = false
      const currentTime = this.player.cache_.currentTime
      let tanmuData = {
        av: this.av,
        playUrl: this.arc,
        currentTime: currentTime,
        fromName: this.fromName,
        playName: this.playName,
        content: this.inputTanmu
      }
      addTanmu(tanmuData)  // 调用接口
      this.$refs.tanmu.add({
        content: this.inputTanmu
      })
      // 存刚刚发的弹幕数据, 延迟是因为担心会重复显示
      setTimeout(() => {
        if (this.tanmuList[parseInt(currentTime)]) {
          this.tanmuList[parseInt(currentTime)].push(tanmuData)
        } else {
          this.tanmuList[parseInt(currentTime)] = [tanmuData]
        }
      }, 3000)
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
      this.$refs.tanmu.removeAll()
      this.inputTanmu = ''
      this.tanmuList = {1: [{'content': '发送一条弹幕试试吧'}, {'content': '弹幕有你更精彩'}]}
      this.currentPlayerTime = -1
      this.showTanmu = true
      getTanmu({
        av: this.av,
        playName: this.playName,
        fromName: this.fromName,
        playUrl: this.src
      }).then(data => {
        console.log('获取弹幕成功', data)
        this.tanmuList = data
      }).catch(err => {
        console.log('获取弹幕失败', err)
      })
    },
    switchFull() {
      requestFullScreen(this.$refs.videoCol)
    },
    replaceFullScreenButton() {
      // 修改全屏按钮, 使用自定义的全屏功能
      let fullButton = document.getElementsByClassName("vjs-fullscreen-control")[0]
      try {
        fullButton = clearEventListener(fullButton)
      } catch (err) {
        console.log(err);
      }
      fullButton.onclick = () => {
        this.switchFull()
      }
    }
  },
  mounted() {
    this.av = this.$route.query.av
    getVideoById(this.av).then(data => {
      this.videoInfo = data
      this.videoInfo.content = "&nbsp;&nbsp;&nbsp;&nbsp;" + data.content.replace(/\s*/g, "").replace(/<br\/>*/, '<br> &nbsp;&nbsp;&nbsp;&nbsp;');
      this.startPlay(this.videoInfo.videoPlayGroupList[0].videoPlayUrlVoList[0], this.videoInfo.videoPlayGroupList[0].fromName)
    })
  },
  beforeDestroy() {
    if (this.player) {
      this.player.dispose()
    }
  }
}
</script>

<style scoped>

</style>
