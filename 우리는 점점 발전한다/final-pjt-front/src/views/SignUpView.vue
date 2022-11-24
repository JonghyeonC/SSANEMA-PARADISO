<template>
  <div class="container">
    <div class="sign_title">
      <h1 class="mb-3">회원가입</h1>
    </div>
    <form class="sign_form" @submit.prevent="signUp">
      <div class="col-md-12 mb-3">
        <label for="username">사용자이름</label>
        <input type="text" class="form-control" id="username" placeholder="username" v-model="username" required>
        <div class="invalid-feedback">
          이름을 입력해주세요.
        </div>
      </div>
      <div class="col-md-12 mb-3">
        <label for="email">이메일</label>
        <input type="text" class="form-control" id="email" placeholder="필수 아님">
        <div class="invalid-feedback">
          이메일을 제대로 입력해주세용!
        </div>
      </div>
      <div class="col-md-12 mb-3">
        <label for="password1">비밀번호 : </label>
        <input type="password" class="form-control" id="password1" v-model="password1" placeholder="비밀번호" required>
      </div>
      <div class="col-md-12 mb-3">
        <label for="password2">비밀번호 확인 : </label>
        <input type="password" class="form-control" id="password2" v-model="password2" placeholder="비밀번호 확인" required>
      </div>
      <div class="signbtn">
        <button class="btn btn-outline-primary btn-lg">가입 완료</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username,
        password1,
        password2
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>
<style>
.signbtn {
  display: flex;
  justify-content: right;
}
.sign_form {
  width: 648px;
  margin: auto;
}
.sign_title {
  width: 648px;
  margin: auto;
}
</style>
