<template>
<div style="margin-top: 100px">
  <button @click="test">test</button>
</div>
</template>

<script>
import {toast, aes_decrypt, aes_encrypt} from "@/utils/utils";

export default {
  name: "Test",
  methods: {
    test() {
      toast('测试')
    }
  },
  mounted() {
    let plaintext = 'Congratulations'
    let key = "ddfbccae-b4c4-11"
    let iv = "ddfbccae-b4c4-11"

    let ciphertext = aes_encrypt(plaintext, key, iv)
    console.log('ciphertext', ciphertext)

    plaintext = aes_decrypt(ciphertext, key, iv)
    console.log('plaintext', plaintext)

  }

}
</script>

<style scoped>

</style>