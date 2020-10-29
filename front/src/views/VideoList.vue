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
        page: null,
        total: 12,
        perPage: 48,
        videos: []
      }
    },
    methods: {
      getList() {
        const type_en = this.$route.query.type_en
        getVideoList({type_en, page: this.page, per_page: this.perPage}).then(data => {
          this.total = data.total
          this.videos = data.data
        })
        scroll(0,0)
      },
      changePage(value) {
        if (value != this.$route.query.page) {
          this.page = Number(value)
          console.log(this.page)
          let query = this.$route.query
          let newQuery = JSON.parse(JSON.stringify(query));
          newQuery.page = this.page
          console.log(query);
          let path = this.$router.history.current.path;
          this.$router.push({path, query:newQuery})
        }
        this.getList()
      }
    },
    mounted() {
      document.title = this.$route.query.type_name
      this.page = Number(this.$route.query.page || 1)
      this.getList()
    }

  }
</script>

<style scoped>

</style>
