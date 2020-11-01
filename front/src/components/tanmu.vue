<template>
    <div id="barrageWrapper" ref="barrageWrapper" :style="`height: 1; width: ${width}px`">

    </div>
</template>
<style lang="scss">
    #barrageWrapper {

        position: absolute;
        top: 0;
        //left: 0;

      .barrageItem {
            width: auto;
            text-align: center;
            height: 30px;
            background-color: rgba(0, 59, 147, .7);
            font-size: 25px;
            color: #FEED64;
            display: inline-block;
            line-height: 30px;
            padding: 0px 4px;
            border-radius: 30px;
            position: absolute;
            white-space: nowrap;
            z-index: 2147483647;

            /*&.move {*/
            /*    transition: transform 4.5s linear;*/
            /*}*/
        }
    }
</style>
<script>
  import Component from 'vue-class-component';

  // const bodyWidth = window.document.body.clientWidth;

  @Component({
    props: {
      // data: Array,
      line: { // 行数
        default: 8,
        type: Number,
      },
      lastTime: {
        default: 8,
        type: Number,
      },
      height: {
        default: 90,
        type: Number,
      },
      width: {
        default: 90,
        type: Number,
      }
    }
  })


  class Barrage {


    add(data) {
      this.createDom(data)
    }
    createDom(data) {
      if (!data) {
        return
      }
      const wrapperItem = this.$refs.barrageWrapper;
      const div = window.document.createElement('div');
      div.innerText = data.content;
      div.classList.add('barrageItem');
      wrapperItem.appendChild(div);
      const divH = div.clientHeight * (Math.floor(Math.random() * this.line));
      div.style.width = `${div.clientWidth}px`;
      div.style.right = 0
      div.style.webkitTransform = `translate3d(${div.clientWidth}px, ${divH}px, 0)`;
      setTimeout(() => {
        console.log(div.style.width)
        div.style.webkitTransform = `translate3d(${-this.width - div.clientWidth}px, ${divH}px, 0)`;
        div.style.transition = `transform ${this.lastTime}s linear`
      }, 10);
      setTimeout(() => {
        wrapperItem.removeChild(div)
      }, (this.lastTime) * 1000)
    }
    removeAll() {
      const wrapperItem = this.$refs.barrageWrapper;
      wrapperItem.innerText = ''
    }
  }

  export default Barrage
</script>
