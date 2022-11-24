<template>
  <div class="container justify-content-center">
    <ul class="list-group">
      <li class="p-2">
        <div v-if="!isEditing">
          <span  class="fs-5 align-bottom">
            <router-link class="commentdeco" :to="{ name: 'MyPageView' }" v-if="comment?.user.username === this.$store.state.user.username">{{ comment?.user.username }}</router-link>
            <router-link class="commentdeco" :to="{ name: 'ProfileView', params:{ username: comment?.user.username } }" v-if="comment?.user.username !== this.$store.state.user.username">{{ comment?.user.username }}</router-link>
            <span> : {{ comment?.content }}</span>
          </span>
          <span v-if="comment?.user.username === this.$store.state.user.username">
            <button class="float-end btn btn-dark" @click="deleteComment">삭제</button>
            <button class="float-end btn btn-dark mx-2" @click="changeComment">수정</button>
          </span>
        </div>
        <div v-if="isEditing">
          <form @submit.prevent="updateComment">
            <input v-model.trim='content' class="form-control form-control-lg" type="text">
          </form>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'CommentList',
    data() {
      return {
        content: this.comment.content,
        isEditing: false,
      }
    },
    props: {
      comment: Object,
    },
    methods: {
      deleteComment() { 
        // console.log(this.$route.params.id)
        // console.log(this.$store.state.token)
        // console.log(this.$store.state.login)
        axios({
          method: 'delete',
          url: `${API_URL}/api/v1/comments/${this.comment.id}/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$store.commit('GET_MOVIE_COMMENT', this.$route.params.id)
        })
        .catch(err => {
          console.log(err)
        })
      },
      changeComment () {
        this.isEditing = !this.isEditing
      },
      updateComment() {
        const content = this.content
        if (!content) {
          alert('내용을 입력해주세용~~')
          return
        }
        axios({
          method: 'put',
          url: `${API_URL}/api/v1/comments/${this.comment.id}/`,
          data: {
            content,
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.isEditing = false
          this.$store.commit('GET_MOVIE_COMMENT', this.$route.params.id)
        })
        .catch(err => {
          console.log(err)
        })
      }
    }
}
</script>

<style>
.commentdeco{
  text-decoration: none;
  color: rgb(59, 109, 124);
}
</style>