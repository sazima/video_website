<template>
  <div>
    <b-container :fluid='true'>
      <b-row align-h="center" style="margin-top: 89px">
        <b-col cols="12" md="8">
          <b-alert show variant="info">{{ videoInfo.vod_name }} -- {{ name }}</b-alert>
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
              <b-tab v-for="(url, index) in videoInfo.urls" :key="index" :title="url.play_line_name"
                     ref="tab" :active="false">
                <b-button v-for="(link, index) in url.links" :key="index" @click="startPlay(link, url.play_line_name)"
                          variant="outline-primary">{{ link.name }}
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
                <b-img :src="videoInfo.vod_pic" blank-color="#ccc" width="64" height="90" alt="placeholder"></b-img>
              </template>

              <h5 class="mt-0">{{ videoInfo.vod_name }}</h5>
              <p v-html="videoInfo.vod_content"></p>
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
      vod_id: '',
      inputTanmu: '',
      sendTanmuButtonText: '发射',
      showTanmu: true,
      videoInfo: {},
      currentPlayerTime: -1,
      danmuContainerHeight: 90,
      danmuContainerWidth: 90,
      canSubmitTanmu: false,
      name: '',
      play_line_name: '',
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
    startPlay(link, play_line_name) {
      this.src = link.link
      this.name = link.name
      this.play_line_name = play_line_name
      document.title = this.videoInfo.vod_name + this.name
      if (!this.player) {
        this.createPlayer()
      } else {
        this.player.src(link.link)
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
      const current_time = this.player.cache_.currentTime
      let tanmuData = {
        vod_id: this.vod_id,
        play_url: this.src,
        current_time: current_time,
        play_line_name: this.play_line_name,
        play_name: this.name,
        content: this.inputTanmu
      }
      addTanmu(tanmuData)  // 调用接口
      this.$refs.tanmu.add({
        content: this.inputTanmu
      })
      // 存刚刚发的弹幕数据, 延迟是因为担心会重复显示
      setTimeout(() => {
        if (this.tanmuList[parseInt(current_time)]) {
          this.tanmuList[parseInt(current_time)].push(tanmuData)
        } else {
          this.tanmuList[parseInt(current_time)] = [tanmuData]
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
        vod_id: this.vod_id,
        play_line_name: this.play_line_name,
        play_name: this.name,
        play_url: this.src
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
    this.vod_id = this.$route.query.vod_id
    getVideoById(this.vod_id).then(data => {
      this.videoInfo = data
      this.videoInfo.vod_content = "&nbsp;&nbsp;&nbsp;&nbsp;" + data.vod_content.replace(/\s*/g, "").replace(/<br\/>*/, '<br> &nbsp;&nbsp;&nbsp;&nbsp;');
      this.startPlay(this.videoInfo.urls[0].links[0], this.videoInfo.urls[0].play_line_name)
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
