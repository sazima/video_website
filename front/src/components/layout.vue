<template>
  <div id="app">
    <b-navbar toggleable="lg" type="dark" variant="info" fixed="top" style="z-index: 999">
      <b-navbar-brand href="/">主页</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item v-for="item in this.parentType" :key="item.type_id"
                      :to="{name: 'list', query: {typeId: item.id, typeName: item.name}}">
            {{ item.name }}
          </b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav>
          <b-nav-form>
          </b-nav-form>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input v-model="kw" size="sm" class="mr-sm-2" placeholder="Search"
                          @keydown.enter.native="listenEnterKey"/>
            <b-button size="sm" class="my-2 my-sm-0" @click="search">Search</b-button>
          </b-nav-form>
          <b-nav-item v-if="!userInfo" v-b-modal="'loginModal'">
            <span>未登录</span>
          </b-nav-item>
          <b-nav-item-dropdown right v-else>
            <template v-slot:button-content>
              <span>{{ userInfo.nickName }}</span>
            </template>
            <b-dropdown-item href="#">更多功能， 敬请期待</b-dropdown-item>
            <b-dropdown-item href="#" @click="signOut">退出</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <router-view/>
    <b-modal id="loginModal" title="登录"
             ok-title="登录"
             cancel-title="取消"
             @ok="login"
    >
      <b-container fluid>
        <b-row align-h="center">
          <b-form-input :cols="12" sm="12" lg="12" v-model="loginForm.email" placeholder="邮箱"></b-form-input>
          <b-form-input required cols="12" sm="12" lg="12" v-model="loginForm.password" placeholder="密码" type="password"
                        style="margin-top: 10px"></b-form-input>
        </b-row>
        <b-row @click="showRegisterModal">
          <span style="margin-top: 20px">
          还没有帐号, 点击注册
          </span>
        </b-row>
      </b-container>
    </b-modal>

    <b-modal id="registerModal" title="注册"
             ok-title="注册"
             cancel-title="取消"
             @ok="register"
    >
      <b-container fluid>
        <b-row align-h="center">
          <b-form style="width: 100%">
            <b-form-input :state="validationEmail" v-model="registerForm.email"
                          placeholder="邮箱" style="margin-top: 10px"></b-form-input>
            <b-form-invalid-feedback :state="validationEmail">
              输入合法邮箱
            </b-form-invalid-feedback>
          </b-form>

          <b-form style="width: 100%">
            <b-form-input :state="validationNickName" v-model="registerForm.nickName"
                          placeholder="昵称" style="margin-top: 10px"></b-form-input>
            <b-form-invalid-feedback :state="validationNickName">
              输入昵称
            </b-form-invalid-feedback>
          </b-form>
          <b-form style="width: 100%">
            <b-form-input cols="12" sm="12" lg="12" v-model="registerForm.password" placeholder="密码" type="password"
                          style="margin-top: 10px"></b-form-input>
          </b-form>
          <b-form style="width: 100%">
            <b-form-input :state="validateConfirmPassword" cols="12" sm="12" lg="12"
                          v-model="registerForm.confirmPassword" placeholder="确认密码" type="password"
                          style="margin-top: 10px"></b-form-input>
            <b-form-invalid-feedback :state="validateConfirmPassword">
              与密码一致
            </b-form-invalid-feedback>
          </b-form>
        </b-row>
      </b-container>
    </b-modal>


  </div>
</template>

<script>
import {getTypes} from '../apis/video'
import {cleanToken, getUserInfo, setToken} from "@/utils/authUtils";
import {getLoginStatus, login, registerUser} from "@/apis/user";
import {toast} from "@/utils/utils";

export default {
  name: "layout",
  data() {
    return {
      parentType: [],
      kw: '',
      userInfo: null,
      loginForm: {
        email: '',
        password: ''
      },
      registerForm: {
        email: '',
        nickName: '',
        password: '',
        confirmPassword: '',
        picture: ''
      }
    }
  },
  methods: {
    parseTypeList(all_type) {
      for (let type_item of all_type) {
        if (type_item.parentType === 0) {
          this.parentType.push(type_item)
        }
      }
    },
    listenEnterKey(event) {
      console.log(event.which)
      if (event.which === 13) {
        event.preventDefault()
        this.search()
      }
    },
    search() {
      if (!this.kw) {
        return
      }
      this.$router.push({name: 'list', query: {kw: this.kw}}).catch(err => {
        console.log(err);
        location.reload()
      })
    },
    login(bvModalEvt) {
      bvModalEvt.preventDefault()
      login(this.loginForm).then(res => {
        console.log(res, 'success');
        toast('登录成功', 'success')
        this.$bvModal.hide('loginModal')
        const token = res.token
        const userDetailInfo = res.userDetailVo
        this.userInfo = {
          token: token,
          email: userDetailInfo.email,
          nickName: userDetailInfo.nickName
        }
        setToken(this.userInfo)
      }).catch(err => {
        console.log(err);
        // this.$bvModal.show('loginModal')
      })
    },
    register(bvModalEvt) {
      bvModalEvt.preventDefault()
      if (!this.validateConfirmPassword || !this.validationNickName || !this.validationEmail) {
        bvModalEvt.preventDefault()
        return
      }
      registerUser(this.registerForm).then(res => {
        console.log(res);
        toast('注册成功，  请点击登录', 'success')
        this.$bvModal.hide('registerModal')
        this.$bvModal.show('loginModal')
      }).catch(err => {
        console.log(err);
      })
    },
    showRegisterModal() {
      this.$bvModal.hide('loginModal')
      this.$bvModal.show('registerModal')
    },
    signOut() {
      cleanToken()
      this.userInfo = null
    },
    getTypes() {
      const allType = sessionStorage.getItem('allType')
      if (allType) {
        return this.parseTypeList(JSON.parse(allType))
      }
      getTypes().then(allType => {
        sessionStorage.setItem('allType', JSON.stringify(allType))
        this.parseTypeList(allType)
      })
    },
    checkLogin(){
      getLoginStatus()
    }
  },
  mounted() {
    this.getTypes()
    if (!this.userInfo) {
      const userInfo = getUserInfo()
      if (userInfo) {
        this.checkLogin().then(res => {
          this.userInfo = userInfo
        }).catch(err => {
          console.log(err);
        })
      }
    }
  },
  computed: {
    validationEmail() {
      const reg = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
      return reg.test(this.registerForm.email)
    },
    validateConfirmPassword() {
      return this.registerForm.password === this.registerForm.confirmPassword
    },
    validationNickName() {
      return !!this.registerForm.nickName
    }
  }
}
</script>

<style scoped>

</style>
