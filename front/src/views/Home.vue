<template>
    <div class="home">
        <slide-image :items="brand" v-if="false"></slide-image>
        <b-container :fluid='true' style="margin-top: 40px">
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <content-item
                            v-for="item in typeItems" :show-more-button="true" :title="item.type_name"
                            :videos="item.videos"
                            :type_en="item.type_en"
                            style="margin-top: 40px" :key="item.type_en"></content-item>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>

  import SlideImage from "../components/SlideImage";
  import ContentItem from "../components/ContentItem";
  import {getIndexTree} from "../apis/index"

  import {isMobile} from "../utils/utils";

  export default {
    name: 'Home',
    components: {SlideImage, ContentItem},
    data() {
      return {
        typeItems: [],
        brand: []
      }
    },
    async mounted() {
      document.title = '电影网站'
      let indexTree = await getIndexTree()
      this.brand = indexTree.brand
      let type_with_video_list = indexTree.type_with_video_list
      for (let typeItem of type_with_video_list) {
        this.typeItems.push({
          type_en: typeItem.type_en,
          type_name: typeItem.type_name,
          videos: isMobile() ? typeItem.videos.slice(0, 6) : typeItem.videos
        })
      }
      console.log(this.typeItems);
    }
  }
</script>
