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
          <div class="art" style=" width: 100%; " ref="art"></div>
        </b-col>
      </b-row>

      <b-row align-h="center" style="background-color: #fff; margin-top: 20px">
        <b-col cols="12" md="8">
          <b-card>
            <b-tabs card style="background-color: #fff">
              <b-tab v-for="(group, index) in videoInfo.videoPlayGroupList"
                     :key="index" :title="group.fromName" ref="tab" :active="false">
                <b-button v-for="(urlName, index) in group.videoPlayUrlVoList" :key="index"
                          @click="startPlay(urlName, group.fromName)"
                          variant="outline-primary">
                  {{ urlName.name }}
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
// import TanmuPlayer from "@/components/TanmuPlayer/index";
// no-unused-vars
import Hls from 'hls.js';
import Artplayer from 'artplayer/dist/artplayer.legacy.js';
import artplayerPluginDanmuku from 'artplayer-plugin-danmuku'

export default {
  name: "Play",
  components: {},
  data() {
    return {
      task: null,
      player: null,
      av: '',
      videoInfo: {},
      urlName: {},
      canSubmitTanmu: true,
      fromName: '',  // 链接来源
      playName: '',
      tanmuList: []
    };
  },
  methods: {
    submitTanmu(t) {
      // {mode: 0, color: '#FFFFFF', border: true, text: '1', time: 13.284628}
      const style = {'color1': t.color, mode: t.mode, border: t.border}
      let tanmuData = {
        av: this.av,
        playUrl: this.arc,
        currentTime: t.time,
        fromName: this.fromName,
        playName: this.playName,
        content: t.text,
        style: JSON.stringify(style)
      }
      addTanmu(tanmuData)  // 调用接口
    },
    initTanmu() {
      getTanmu({
        av: this.av,
        playName: this.playName,
        fromName: this.fromName,
        playUrl: ""
      }).then(data => {
        let tanmuList = []
        for (const t of data) {
            const style = t.style
            let color1 = '#fff'
            let border = false
            let mode = 0
            if (style) {
              const styleJson = JSON.parse(style)
              color1 = styleJson.color1 || color1
              border = styleJson.border || border
              mode = style.mode || mode
            }
            tanmuList.push({
              text: t.content, // 弹幕文本
              time: t.currentTime, // 发送时间，单位秒
              color: color1, // 弹幕局部颜色
              border: border, // 是否显示描边
              mode: mode, // 弹幕模式: 0表示滚动, 1静止
            })
        }
        this.tanmuList = tanmuList
        console.log('-------', this.tanmuList)
        this.player.plugins.artplayerPluginDanmuku.config({
          danmuku: this.tanmuList
        })
        this.player.plugins.artplayerPluginDanmuku.load()
      }).catch(err => {
        console.log('获取弹幕失败', err)
      })
    },
    startPlay(urlName, fromName) {
      const src = urlName.url[0].src
      const option = {
        container: '.art',
        fullscreen: true,
        fullscreenWeb: true,
        type: 'm3u8',
        customType: {
          m3u8: playM3u8,
        },
        plugins: [
          artplayerPluginDanmuku({
            // 弹幕数组
            danmuku: []
          }),
        ],
      };
      if (!this.player){
        this.player = new Artplayer(option);
        this.player.on('artplayerPluginDanmuku:emit', (danmu) => {
          console.info('新增弹幕', danmu);
          this.submitTanmu(danmu)
        });
      }
      this.player.url = src
      this.playName = urlName.name
      this.fromName = fromName
      document.title = this.videoInfo.name + this.playName
      function playM3u8(video, url, art) {
        if (Hls.isSupported()) {
          if (art.hls) art.hls.destroy();
          const hls = new Hls();
          hls.loadSource(url);
          hls.attachMedia(video);
          art.hls = hls;
          art.on('destroy', () => hls.destroy());
        } else if (video.canPlayType('application/vnd.apple.mpegurl')) {
          video.src = url;
        } else {
          art.notice.show = 'Unsupported playback format: m3u8';
        }
      }
      this.initTanmu()
    }
  },
  mounted() {
    this.$refs.art.style.height = '' + (this.$refs.art.clientWidth * 9 / 16) + 'px'
    this.task = setInterval(() => {
      this.$refs.art.style.height = '' + (this.$refs.art.clientWidth * 9 / 16) + 'px'
    }, 5000)
    this.av = this.$route.query.av
    getVideoById(this.av).then(data => {
      this.videoInfo = data
      this.videoInfo.content = "&nbsp;&nbsp;&nbsp;&nbsp;" + data.content.replace(/\s*/g, "").replace(/<br\/>*/, '<br> &nbsp;&nbsp;&nbsp;&nbsp;');
      this.startPlay(this.videoInfo.videoPlayGroupList[0].videoPlayUrlVoList[0], this.videoInfo.videoPlayGroupList[0].fromName)
    })
  },
  beforeDestroy() {
    if (this.task) {
      window.clearInterval(this.task);

    }
  }
}

</script>

<style scoped>

</style>
