<template>
  <div class="container">
    <form @submit.prevent="CreateComment">
      <input v-model.trim='content' class="form-control form-control-lg" type="text" placeholder="댓글 작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'CommentCreateForm',
  data() {
    return {
      content : null,
    }
  },
  methods: {
    CreateComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세용~~')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/comments_create/`,
        data: {
          content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$store.commit('GET_MOVIE_COMMENT', this.$route.params.id)
        this.content = null
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>