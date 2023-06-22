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
          <div id="dplayer" ref="dplayer" >
          </div>
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
// import TanmuPlayer from "@/components/TanmuPlayer/index";
import DPlayer from 'dplayer';
// no-unused-vars
import Hls from 'hls.js';


export default {
  name: "Play",
  components: {},
  data() {
    return {
      player: null,
      av: '',
      inputTanmu: '',
      // sendTanmuButtonText: '发射',
      videoInfo: {},
      urlName: {},
      canSubmitTanmu: true,
      fromName: '',  // 链接来源
      playName: '',
      tanmuList: {}
    };
  },
  methods: {
    startPlay(urlName, fromName) {
      this.playName = urlName.name
      this.fromName = fromName
      document.title = this.videoInfo.name + this.playName
      // 初始化 MuiPlayer 插件，MuiPlayer 方法传递一个对象，该对象包括所有插件的配置
      const baseUrl = process.env.VUE_APP_BASE_URL || window.location.protocol + "://" + window.location.host
      const url = `${baseUrl}/tanmu/`
      const dp = new DPlayer({
        container: document.getElementById('dplayer'),
        danmaku: {
          api: url,
          user: 'DIYgod',
          bottom: '15%',
          unlimited: true,
          speedRate: 0.5,
          id: `${this.av}~${this.fromName}~${this.playName}`
        },
        video: {
          url: urlName.url[0].src,
          type: 'customHls',
          customType: {
            customHls: function (video, player) {
              const hls = new Hls();
              hls.loadSource(video.src);
              hls.attachMedia(video);
            },
          },
        },
      });
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
