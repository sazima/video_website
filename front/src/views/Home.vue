<template>
    <div class="home">
        <slide-image></slide-image>
        <b-container :fluid='true'>
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <content-item :show-more-button="true" style="margin-top: 40px" title="电影"></content-item>
                    <content-item :show-more-button="true" style="margin-top: 40px" title="电视剧"></content-item>
                    <content-item :show-more-button="true" style="margin-top: 40px" title="综艺"></content-item>
                    <content-item :show-more-button="true" style="margin-top: 40px" title="咨询"></content-item>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>

  import SlideImage from "../components/SlideImage";
  import ContentItem from "../components/ContentItem";

  export default {
    name: 'Home',
    components: {SlideImage, ContentItem},
    data() {
      return {
        items: [
          {
            text: 'Admin',
            href: '#'
          },
          {
            text: 'Manage',
            href: '#'
          },
          {
            text: 'Library',
            active: true
          }
        ],
      }
    }
  }
</script>
