<template>
  <div class="container">
    <div class="login_title">
      <h1 class="mb-3">로그인</h1>
    </div>
    <form class="login_form" @submit.prevent="logIn">
      <div class="col-md-12">
        <label for="username">username : </label>
        <input type="text" class="form-control" id="username" v-model="username" placeholder="username" required><br>
      </div>
      <div class="col-md-12">
        <label for="password">password : </label>
        <input type="password" class="form-control" id="password" v-model="password" placeholder="비밀번호" required><br>
      </div>
      <div class="loginbtn">
        <button class="btn btn-outline-primary btn-lg">로그인</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password,
      }
      this.$store.dispatch('logIn', payload)
    }
  }
}
</script>

<style>
.loginbtn {
  display: flex;
  justify-content: right;
}
.login_form {
  width: 648px;
  margin: auto;
}
.login_title {
  width: 648px;
  margin: auto;
}
</style>