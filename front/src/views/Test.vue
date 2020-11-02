<template>
<div style="margin-top: 100px">
  <button @click="test">test</button>
</div>
</template>

<script>
import {toast} from "@/utils/utils";

export default {
  name: "Test",
  methods: {
    test() {
      toast('测试')
    }
  }

}
</script>

<style scoped>

</style>