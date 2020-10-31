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
                        v-model="currentPage"
                        :total-rows="total"
                        :per-page="perPage"
                        @change="changePage"
                ></b-pagination>
            </b-row>
        </b-container>
    </div>

</template>

<script>
  import ContentItem from "../components/ContentItem";
  import {getVideoList} from "../apis/video";
  // import merge from 'webpack-merge'


  export default {
    name: "VideoList",
    components: {ContentItem},
    data() {
      return {
        currentPage: null,
        total: 9999,
        perPage: 48,
        kw: '',
        videos: []
      }
    },
    methods: {
      getList() {
        const type_en = this.$route.query.type_en
        let page = Number(this.$route.query.page || 1)
        getVideoList({type_en, kw: this.kw, page: page, per_page: this.perPage}).then(data => {
          this.total = data.total
          this.videos = data.data
          this.currentPage = page
        })
        scroll(0,0)
      },
      changePage(value) {
        console.log(value);
        let query = this.$route.query
        let path = this.$router.history.current.path;
        let newQuery = JSON.parse(JSON.stringify(query));
        newQuery.page = value
        this.$router.push({path, query: newQuery})
      },
      init() {
        document.title = this.$route.query.type_name || '视频网站'
        this.kw = this.$route.query.kw || ''
        this.getList()
      }
    },
    watch: {
      $route() {
        this.init()
      }
    },
    mounted() {
      this.init()
    }

  }
</script>

<style scoped>

</style>
