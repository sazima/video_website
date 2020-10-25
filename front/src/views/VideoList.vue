<template>
    <div>
        <b-container :fluid='true' style="margin-top: 50px">
            <b-row align-h="center">
                <b-col cols="12" md="10">
                    <content-item :show-more-button="false" style="margin-top: 40px" title="电影"></content-item>
                </b-col>
            </b-row>
        </b-container>
    </div>

</template>

<script>
  import ContentItem from "../components/ContentItem";

  export default {
    name: "VideoList",
    components: {ContentItem}
  }
</script>

<style scoped>

</style>
