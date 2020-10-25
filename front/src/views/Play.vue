<template>
    <div>
        <b-container :fluid='true' style="margin-top: 50px">
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <video id="vid1" ref="videoPlayer" class="video-js" style="margin-top: 40px" >
                        <source
                                :src="src"
                                type="application/x-mpegURL"
                        />
                    </video>
                </b-col>
            </b-row>
        </b-container>

    </div>
</template>

<script>
  export default {
    name: "Play",
    data() {
      return {
        player: null,
        src: 'https://cdn-yong.bejingyongjiu.com/20201024/24492_eb62a589/index.m3u8'
      };
    },
    mounted() {
      // 播放参数
      let options = {
        controls: true, // 是否显示底部控制栏
        preload: "auto", // 加载<video>标签后是否加载视频
        playbackRates: [0.5, 1, 1.5, 2],// 倍速播放
        width: "720",
        height: "480"
      };
      this.player = this.$video(this.$refs.videoPlayer, options, function onPlayerReady() {
        console.log('onPlayerReady', this);
      });
    }
    ,
    beforeDestroy() {
      if (this.player) {
        this.player.dispose()
      }
    }
  }
</script>

<style scoped>

</style>
