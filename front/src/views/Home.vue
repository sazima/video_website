<template>
    <div class="home">
        <slide-image :items="brand" v-if="false"></slide-image>
        <b-container :fluid='true' style="margin-top: 40px">
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <content-item
                            v-for="item in typeVideoItems" :show-more-button="true" :title="item.typeName"
                            :videos="item.videoListVos"
                            :typeId="item.typeId"
                            style="margin-top: 40px" :key="item.typeId"></content-item>
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
        typeVideoItems: [],
        brand: []
      }
    },
    async mounted() {
      document.title = '电影网站'
      let indexTree = await getIndexTree()
      this.brand = indexTree.brand
      let typeWithVideoListVoList = indexTree.typeWithVideoListVoList
      for (let typeVideoItem of typeWithVideoListVoList) {
        this.typeVideoItems.push({
          typeId: typeVideoItem.typeId,
          typeName: typeVideoItem.typeName,
          videoListVos: isMobile() ? typeVideoItem.videoListVos.slice(0, 6) : typeVideoItem.videoListVos
        })
      }
      console.log(this.typeVideoItems);
    }
  }
</script>
