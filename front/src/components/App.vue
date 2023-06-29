<template>
  <div id="app">
    <component :is="layout">
      <router-view/>
    </component>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      default_layout: "userLayout",
    };
  },
  computed: {
    layout() {
      return this.$route.meta.layout || this.default_layout;
    },
  },

}
</script>

<style scoped>

</style>