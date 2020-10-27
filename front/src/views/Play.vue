<template>
    <div>
        <b-container :fluid='true' style="margin-top: 50px">
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <video id="vid1" ref="videoPlayer" class="video-js" style="margin-top: 40px" controls >
                        <source type="application/x-mpegURL"/>
                    </video>
                </b-col>
            </b-row>
            <b-row align-h="center" style="background-color: #fff; margin-top: 20px">
                <b-col cols="12" md="10">
                <b-card >
                    <b-tabs card style="background-color: #fff">
                        <b-tab v-for="(url, index) in videoInfo.urls" :key="index" :title="url.play_line_name" active>
                            <b-button v-for="(link, index) in url.links" :key="index" @click="playUrl(link.link)" variant="outline-primary">{{link.name}}</b-button>
                        </b-tab>
                    </b-tabs>
                </b-card>
                </b-col>
            </b-row>
        </b-container>

    </div>
</template>

<script>
  import {getVideoById} from "../apis/video";

  export default {
    name: "Play",
    data() {
      return {
        player: null,
        src: '',
        vod_id: '',
        videoInfo: {}
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
      },
      playUrl(url) {
        this.src = url
        if (!this.player) {
          this.createPlayer()
        } else {
          console.log(url);
          this.player.src(url)
          this.player.load()
          this.player.play()
        }
      }
    },
    mounted() {
      this.vod_id = this.$route.query.vod_id
        getVideoById(this.vod_id).then(data => {
          this.videoInfo = data
          this.playUrl(this.videoInfo.urls[0].links[0].link)
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
