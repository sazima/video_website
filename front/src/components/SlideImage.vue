<template>
    <div>
        <b-carousel
                id="carousel-1"
                v-model="slide"
                :interval="4000"
                controls
                indicators
                background="#ababab"
                img-width="1024"
                img-height="480"
                style="text-shadow: 1px 1px 2px #333;"
                @sliding-start="onSlideStart"
                @sliding-end="onSlideEnd"

        >
            <!-- Text slides with image -->
            <b-carousel-slide v-for="(item, index) in items" :key="index"
                              :caption="item.vod_name"
                              text="hello">
                <template v-slot:img>
                    <img
                            class="d-block img-fluid w-100 brand-img"
                            width="1024"
                            height="480"
                            :src="item.vod_pic"
                            alt="image slot"
                            style="max-height: 400px;  width: auto; margin: 0 auto"
                    >
                </template>
            </b-carousel-slide>

            <!-- Slide with blank fluid image to maintain slide aspect ratio -->
            <!--            <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">-->
            <!--                <p>-->
            <!--                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt-->
            <!--                    a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.-->
            <!--                </p>-->
            <!--            </b-carousel-slide>-->
        </b-carousel>
    </div>
</template>

<script>
  export default {
    name: "SlideImage",
    props: {items: Array},
    data() {
      return {

        slide: 0,
        sliding: null
      }

    },
    methods: {
      onSlideStart(slide) {
        console.log(slide)

        this.sliding = true
      },
      onSlideEnd(slide) {
        console.log(slide)
        this.sliding = false
      },

    },
    mounted() {
    }
  }
</script>

<style scoped>
    .brand-img {
        max-width:630px;
    }

</style>
