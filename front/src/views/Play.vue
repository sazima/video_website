<template>
    <div>
        <b-container :fluid='true'>
            <b-row align-h="center" style="margin-top: 89px">
                <b-col cols="12" md="10">
                    <b-alert show variant="info">{{videoInfo.vod_name}} -- {{name}}</b-alert>
                </b-col>
            </b-row>
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <video id="vid1" ref="videoPlayer" class="video-js" controls>
                        <source type="application/x-mpegURL"/>
                    </video>
                    <tanmu ref="tanmu" v-show='showTanmu' :height="danmuContainerHeight" :width="danmuContainerWidth" ></tanmu>
                </b-col>
            </b-row>
          <b-row align-h="center" style="margin-top: 20px">
            <b-col cols="9" md="7">
              <b-input placeholder="发送弹幕, 请注意弹幕礼仪" v-model="inputTanmu" v-show="currentPlayerTime !== 0"></b-input>
            </b-col>
            <b-col cols="3" >
              <b-button variant="outline-primary" @click="submitTanmu"  :disabled="!canSubmitTanmu || !inputTanmu">{{sendTanmuButtonText}}</b-button>
            </b-col>
          </b-row>
          <b-row align-h="center" style="background-color: #fff; margin-top: 20px">
                <b-col cols="12" md="10">
                    <b-card>
                        <b-tabs card style="background-color: #fff">
                            <b-tab v-for="(url, index) in videoInfo.urls" :key="index" :title="url.play_line_name"
                                   ref="tab" :active="false">
                                <b-button v-for="(link, index) in url.links" :key="index" @click="startPlay(link)"
                                          variant="outline-primary">{{link.name}}
                                </b-button>
                            </b-tab>
                        </b-tabs>
                    </b-card>
                </b-col>
            </b-row>
            <b-row align-h="center" style="background-color: #fff; margin-top: 20px">
                <b-col cols="12" md="10">
                    <b-card>
                        <b-media>
                            <template v-slot:aside>
                                <b-img :src="videoInfo.vod_pic" blank-color="#ccc" width="64" alt="placeholder"></b-img>
                            </template>

                            <h5 class="mt-0">{{videoInfo.vod_name}}</h5>
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

  export default {
    name: "Play",
    components: {tanmu},
    data() {
      return {
        player: null,
        src: '',
        vod_id: '',
        inputTanmu: '',
        sendTanmuButtonText: '发送弹幕',
        showTanmu: true,
        videoInfo: {},
        currentPlayerTime: -1,
        danmuContainerHeight: 90,
        danmuContainerWidth: 90,
        canSubmitTanmu: false,
        name: '',
        tanmuList: { }
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
        this.danmuContainerHeight = this.$refs.videoPlayer.clientHeight
        this.danmuContainerWidth = this.$refs.videoPlayer.clientWidth
        // this.danmuContainerWidth = document.body.clientWidth
      },
      startPlay(link) {
        this.src = link.link
        this.name = link.name
        document.title = this.videoInfo.vod_name + this.name
        if (!this.player) {
          this.createPlayer()
        } else {
          this.player.src(link.link)
          this.player.load()
          this.player.play()
        }
        // 播放条事件
        this.$refs.videoPlayer.addEventListener('timeupdate', this.timeUpdate)
        this.initTanmu()
      },
      // 根据播放条发送弹幕
      timeUpdate(event) {
        if (event.srcElement.currentTime === 0) {
          this.canSubmitTanmu = false
          return
        }
        this.canSubmitTanmu = true
        let previouseTime = this.currentPlayerTime
        this.currentPlayerTime = event.srcElement.currentTime
        console.log('playtime update: ', event.srcElement.currentTime, 'previou time ', previouseTime)
        if (parseInt(previouseTime) === parseInt(this.currentPlayerTime)) {
          return
        }
        let currentTanmuList = this.tanmuList[parseInt(this.currentPlayerTime)]
        if (!currentTanmuList) {
          return
        }
        for (let tanData of currentTanmuList) {
          setTimeout(() => {
            this.$refs.tanmu.add(tanData)
          }, (tanData.current_time - this.currentPlayerTime) * 1000)
        }
      },
      submitTanmu() {
        // 为空不能发送
        if (! this.inputTanmu.trim()) {
          return
        }
        this.canSubmitTanmu = false
        addTanmu({
          vod_id: this.vod_id,
          play_url: this.src,
          current_time: this.$refs.videoPlayer.currentTime,
          content: this.inputTanmu
        })
        this.$refs.tanmu.add({
          content: this.inputTanmu
        })
        this.inputTanmu = ''
        let remainSenconds = 10  // 设置10s间隔, 不能发送太频繁
        let i  = setInterval(() => {
          if (remainSenconds <= 0) {
            this.sendTanmuButtonText = '发送弹幕'
            this.canSubmitTanmu = true
            clearInterval(i)
            return
          }
          this.sendTanmuButtonText = `${remainSenconds}s`
          remainSenconds --
        }, 1000)
      },
      initTanmu() {
        this.inputTanmu = ''
        this.tanmuList = {1: [{'content': '发送一条弹幕试试吧'}, {'content': '弹幕有你更精彩'}]}
        this.currentPlayerTime = -1
        this.showTanmu = true
        getTanmu({
          vod_id: this.vod_id,
          play_url: this.src
        }).then(data => {
          console.log('获取弹幕成功', data)
          this.tanmuList = data
        }).catch(err => {
          console.log('获取弹幕失败', err)
        })
      }
    },
    mounted() {
      this.vod_id = this.$route.query.vod_id
      getVideoById(this.vod_id).then(data => {
        this.videoInfo = data
        this.videoInfo.vod_content = "&nbsp;&nbsp;&nbsp;&nbsp;" + data.vod_content.replace(/\s*/g,"").replace(/<br\/>*/, '<br> &nbsp;&nbsp;&nbsp;&nbsp;');
        this.startPlay(this.videoInfo.urls[0].links[0])
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
