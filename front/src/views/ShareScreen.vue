<template>
  <b-container :fluid='true' style="margin-top: 89px" @dblclick="toFull" ref="container">
    <b-row align-h="center">
      <b-col cols="12" md="8" ref="col" v-show="showVideo">
        <tanmu-player ref="tanmuPlayer" style="height: 100%"></tanmu-player>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import {getUid} from "@/apis/share";

import websocket from "@/apis/websocket";
import TanmuPlayer from "@/components/TanmuPlayer";
import {requestFullScreen} from "@/utils/utils";

export default {
  name: "ShareScreen",
  components: {TanmuPlayer},
  data() {
    return {
      uid: null,
      ws: null,
      showVideo: false,
      urlName: null,
      tanmuPlayer: null,
    }
  },
  methods: {
    getUid() {
      getUid().then(uid => {
        this.uid = uid
        this.ws = websocket.getWebsocket(uid)
        this.ws.onmessage = (data) => {
          const jsonData = JSON.parse(data.data)
          if (jsonData.url) {
            this.urlName = jsonData
            this.startPlay(this.urlName)
          }
        }
      })
    },
    startPlay(urlName) {
      console.log(urlName)
      this.showVideo = true
      this.$refs.tanmuPlayer.startPlay(urlName)
      this.$refs.container.$el.dbclick()
    },
    toFull() {
      requestFullScreen(this.$refs.col)
      this.$refs.tanmuPlayer.player.play()
    }
  },
  mounted() {
    this.getUid()
  },
  beforeDestroy() {
    this.ws.close()
  }
}
</script>

<style scoped>

</style>