<template>
    <div>
        <b-container :fluid='true'>
            <span style="color: #666">
                <span class="h4">{{title}}</span>
                <router-link v-if="showMoreButton" :to="{name: 'list', query: {type_en: type_en, type_name: title}}" style="float:right; text-decoration: none; color: #000">&nbsp;更 多 >></router-link>
            </span>
            <b-row align-h="center">
                <b-col v-for="(item) in videos" :key="item.vod_id" cols="12" sm="6" lg="2" style="margin-top: 30px">
                    <router-link :to="{name: play}">
                        <b-card :img-src="item.vod_pic" img-alt="Image" :img-width="img_width" :img-height="img_width * 271 /196" ref="card">
                            <b-card-text style="height: 50px; overflow: hidden">
                                {{item.vod_name}}
                            </b-card-text>
                            <template v-slot:footer>
                                <small class="text-muted">{{item.vod_time}}</small>
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
    props: {showMoreButton: Boolean, items: Array, title: String, type_en: String, videos: Array},
    data() {
      return {
        img_width: 196
      }
    },
    mounted() {
      if (this.$refs.card) {
        this.img_width = this.$refs.card[0].clientWidth
      }
    }
  }
</script>

<style scoped>

</style>
