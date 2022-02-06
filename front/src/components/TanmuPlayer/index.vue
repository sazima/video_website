<template>
  <div ref="videoCol" @keydown="keymonitor">
    <video id="vid1" ref="videoPlayer" class="video-js" controls playsinline  style="height: 100%;  ">
      <source type="application/x-mpegURL"/>
    </video>
    <tanmu ref="tanmu" v-show='showTanmu' :height="danmuContainerHeight" :width="danmuContainerWidth"></tanmu>
  </div>
</template>

<script>
import {clearEventListener, isIOS, requestFullScreen} from "@/utils/utils";
import tanmu from "@/components/TanmuPlayer/tanmu";

export default {
  name: "TanmuPlayer",
  props: [],
  components: {tanmu},
  data() {
    return {
      player: null,
      src: null,
      showTanmu: true,
      danmuContainerHeight: 90,
      danmuContainerWidth: 90,
      tanmuList: {}
    }
  },
  methods: {
    createPlayer() {
      //  播放参数
      let options = {
        controls: true, // 是否显示底部控制栏
        preload: "auto", // 加载<video>标签后是否加载视频
        playbackRates: [0.5, 1, 1.5, 2],// 倍速播放
        aspectRatio: '16:9',
        fluid: true,
        sources: this.src,
      };
      this.player = this.$video(this.$refs.videoPlayer, options)
      this.player.controlBar.addChild('QualitySelector');  // 选择线路
      this.player.ready(() => {
        this.player.tech_.off('dblclick');
        this.player.on('dblclick', () => {
          this.switchFull()
        })
        if (!isIOS()) {
          this.replaceFullScreenButton()
        }
        // 播放条事件
        this.player.on("timeupdate", this.timeUpdate);
      })
    },
    startPlay(urlName) {
      this.src = urlName.url
      console.log('start play _> ', this.src)
      this.playName = urlName.name
      if (!this.player) {
        this.createPlayer()
      } else {
        this.player.src(this.src)
        this.player.load()
        this.player.play()
      }
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
    setTanmu(tanmuList) {
      this.$refs.tanmu.removeAll()
      this.inputTanmu = ''
      this.tanmuList = {1: [{'content': '发送一条弹幕试试吧'}, {'content': '弹幕有你更精彩'}]}
      this.currentPlayerTime = -1
      this.showTanmu = true
      this.tanmuList = tanmuList
    },
    getTanmu() {
      return this.tanmuList
    },
    pushTanmu(tanmuData) {
      const currentTime = tanmuData.currentTime
      this.$refs.tanmu.add({
        content: tanmuData.content
      })
      setTimeout(() => {
        if (this.tanmuList[parseInt(currentTime)]) {
          this.tanmuList[parseInt(currentTime)].push(tanmuData)
        } else {
          this.tanmuList[parseInt(currentTime)] = [tanmuData]
        }
      }, 3000)
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
    },
    keymonitor(e) {
      this.$refs.videoPlayer.focus()
      if (e.keyCode === 39) {  // 向右
        this.$refs.videoPlayer.currentTime += 15
      } else if (e.keyCode === 37) {  // 向左
        this.$refs.videoPlayer.currentTime -= 15
      } else if (e.keyCode === 32) {
        this.$refs.videoPlayer.paused === true ? this.$refs.videoPlayer.play() : this.$refs.videoPlayer.pause();
      }
    }
  },
  mounted() {
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