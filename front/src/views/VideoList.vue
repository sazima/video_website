<template>
    <div>
        <b-container :fluid='true' style="margin-top: 50px">
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <content-item :show-more-button="false" style="margin-top: 40px" title=""
                                  :videos="videos"></content-item>
                </b-col>
            </b-row>
            <b-row align-h="center" style="margin-top: 20px">
                <b-pagination
                        v-model="page"
                        :total-rows="total"
                        :per-page="perPage"
                        first-number
                ></b-pagination>
            </b-row>
        </b-container>
    </div>

</template>

<script>
  import ContentItem from "../components/ContentItem";
  import {getVideoList} from "../apis/videoList";

  export default {
    name: "VideoList",
    components: {ContentItem},
    data() {
      return {
        page: 1,
        total: 12,
        perPage: 36,
        videos: []
      }
    },
    methods: {
      async getList() {
        const type_en = this.$route.query.type_en
        const data = await getVideoList({type_en, page: this.page, per_page: this.perPage})
        this.total = data.total
        this.videos = data.data
        scroll(0,0)
      }
    },
    watch: {
      page() {
        this.getList()
      }
    },
    async mounted() {
      document.title = this.$route.query.type_name
      await this.getList()
    }

  }
</script>

<style scoped>

</style>
