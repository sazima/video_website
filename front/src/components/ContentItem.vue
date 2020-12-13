<template>
    <div>
        <b-container :fluid='true'>
            <span style="color: #666">
                <span class="h4">{{title}}</span>
                <router-link v-if="showMoreButton" :to="{name: 'list', query: {typeId: typeId, typeName: title}}" style="float:right; text-decoration: none; color: #000">&nbsp;更 多 >></router-link>
            </span>
            <b-row align-h="center">
                <b-col v-for="(item) in videos" :key="item.av" cols="12" sm="6" lg="2" style="margin-top: 30px"  >
                    <router-link :to="{name: 'play', query: {av: item.av}}"  target="_blank">
                        <b-card :img-src="item.picture" img-alt="Image" :img-width="img_width" :img-height="img_width * 271 /196" ref="card">
                            <b-card-text style="height: 50px; overflow: hidden">
                                {{item.name}}
                            </b-card-text>
                            <template v-slot:footer>
                                <small class="text-muted">{{item.updateTime}}</small>
                            </template>
                        </b-card>
                    </router-link>
                </b-col>
            </b-row>
        </b-container>
    </div>

</template>

<script>
  export default {
    name: "ContentItem",
    props: {showMoreButton: Boolean, items: Array, title: String, typeId: Number, videos: Array},
    data() {
      return {
        img_width: 196,
        intervalTask: []

      }
    },
    mounted() {
      let task  = setInterval(() => {
        this.img_width = this.$refs.card[0].clientWidth
      }, 1000)
      this.intervalTask.push(task)
    },
    beforeDestroy() {
      for (let task of this.intervalTask) {
        window.clearInterval(task);
      }
      this.intervalTask = []
    }
  }
</script>

<style scoped>

</style>
