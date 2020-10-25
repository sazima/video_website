<template>
    <div>
        <b-container :fluid='true'>
            <span style="color: #666">
                <span class="h4">{{title}}</span>
                <router-link v-if="showMoreButton" to="list" style="float:right; text-decoration: none; color: #000">&nbsp;更 多 >></router-link>
            </span>
            <b-row>
                <b-col v-for="(item) in items" :key="item.id" cols="12" sm="6" lg="3" style="margin-top: 30px">
                    <router-link to="play">
                        <b-card :img-src="item.src" img-alt="Image">
                            <b-card-text style="height: 50px; overflow: hidden">
                                {{item.text}}
                            </b-card-text>
                            <template v-slot:footer>
                                <small class="text-muted">{{item.datetime}}</small>
                            </template>
                        </b-card>
                    </router-link>
                </b-col>
            </b-row>
        </b-container>
    </div>

</template>

<script>
  export default {
    name: "ContentItem",
    props: ['title', 'showMoreButton'],
    data() {
      return {
        items: [{
          id: 1,
          src: 'https://picsum.photos/300/300/?image=41',
          text: '必要なのは勇気だけ！業務中の女を落とすナン店員',
          datetime: 'Last updated 3 mins ago'
        },
          {
            id: 3,
            src: 'https://picsum.photos/300/300/?image=41',
            text: 'adn00148-不貞な上下関係 松下紗栄子',
            datetime: 'Last updated 3 mins ago'
          },
          {
            id: 2,
            src: 'https://picsum.photos/300/300/?image=41',
            text: '84umso00218-Part-2-関西弁熟女のエロさ半端ないって！ ',
            datetime: 'Last updated 3 mins ago'
          }, {
            id: 4,
            src: 'https://picsum.photos/300/300/?image=41',
            text: '1nhdtb00191-Part-1-夜行バスで声も出せずイカされた隙に生ハメされた女はスローピストンの痺れる快感に理性を失い中出しも拒めない 女子○生限定2 腰振り発情SP ',
            datetime: 'Last updated 3 mins ago'
          }
        ]
      }
    },
    mounted() {
      console.log(this.showMoreButton)
    }
  }
</script>

<style scoped>

</style>
