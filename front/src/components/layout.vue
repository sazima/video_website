<template>
    <div id="app">
        <b-navbar toggleable="lg" type="dark" variant="info" fixed="top">
            <b-navbar-brand href="/">主页</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item v-for="item in this.parent_type" :key="item.type_id" :to="{name: 'list', query: {type_en: item.type_en, type_name: item.type_name}}">
                        {{item.type_name}}
                    </b-nav-item>
                </b-navbar-nav>

                <b-navbar-nav >
                    <b-nav-form>
                        <b-form-input v-model="kw" size="sm" class="mr-sm-2" placeholder="Search" @keydown.enter.native="test"/>

                        <b-button size="sm" class="my-2 my-sm-0"  @click="search">Search</b-button>
                    </b-nav-form>
<!--                    <b-nav-item-dropdown right>-->
<!--                        <template v-slot:button-content>-->
<!--                            <em>User</em>-->
<!--                        </template>-->
<!--                        <b-dropdown-item href="#">Profile</b-dropdown-item>-->
<!--                        <b-dropdown-item href="#">Sign Out</b-dropdown-item>-->
<!--                    </b-nav-item-dropdown>-->
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>

        <router-view/>
    </div>
</template>

<script>
  import {getTypes} from '../apis/video'

  export default {
    name: "layout",
    data() {
      return {
        parent_type: [],
        child_type: {},
        kw: ''
      }
    },
    methods: {
      parseTypeList(all_type) {
        for (let type_item of all_type) {
          if (type_item.type_pid === 0) {
            this.parent_type.push(type_item)
          } else {
            if (!this.child_type[type_item.type_pid]) {
              this.child_type[type_item.type_pid] = []
            }
            this.child_type[type_item.type_pid].push(type_item)
          }
        }
      },
    test(event) {
        console.log(event.which)
        if (event.which === 13) {
          event.preventDefault()
          this.search()
        }
    },
      search() {
        if (!this.kw){
          return
        }
        this.$router.push({ name: 'list', query: { kw: this.kw }}).catch(err => {
          console.log(err);
          location.reload()
        })
      }
    },
    mounted() {
      getTypes().then(all_type => {
        this.parseTypeList(all_type)
      })
    }
  }
</script>

<style scoped>

</style>
