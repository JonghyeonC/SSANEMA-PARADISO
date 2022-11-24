<template>
  <div>
    <div class="writer">
      <router-link :to="{ name: 'MyPageView' }" v-if="comment?.user.username === this.$store.state.user.username" class="text-name">{{ comment?.user.username }}</router-link>
      <router-link :to="{ name: 'ProfileView', params:{ username: comment?.user.username } }" v-if="comment?.user.username !== this.$store.state.user.username" class="text-name">{{ comment?.user.username }}</router-link>
    </div>
    <div class="time">
      <p>{{ comment.updated_at.substring(0,4) }}년 {{ comment.updated_at.substring(5,7) }}월 {{ comment.updated_at.substring(8,10) }}일 {{ comment.updated_at.substring(11,13) }}:{{ comment.updated_at.substring(14,16) }}:{{ comment.updated_at.substring(17,19) }}</p>
    </div>
    <div v-if="isEditing" class="upcomment">
      <input type="text" v-model="content">
      <button @click="updateComment(comment)" class="btn btn-comment btn-outline-success">수정</button>
    </div>
    <div v-else class='comment-content'>
      <p>{{ comment.content}}</p>
    </div>
    <div v-if="comment?.user.username === this.$store.state.user.username" class="button-container">
      <button @click="changeStatus" v-if="isEditing==false" class="btn btn-comment btn-outline-info">수정</button>
      <button @click="deleteComment(comment)" class="btn btn-comment btn-outline-danger">삭제</button>
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
let isEditing = false

export default {
  name: 'CommunityCommentListItem',
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
    changeStatus () {
      console.log(isEditing)
      this.isEditing = !this.isEditing
    },
    deleteComment(comment) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/comments/${comment.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.$store.commit('GET_COMMENT', this.$route.params.id)
      })
      .catch(err => console.log(err))
    },
    updateComment(comment) {
      const commentItem = {
        content : this.content
      }
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/community/comments/${comment.id}/`,
        data: commentItem,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.isEditing = false
        this.$store.commit('GET_COMMENT', this.$route.params.id)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
}
</script>

<style>
.text-name {
  text-decoration: none;
  color: black;
  font-weight: 1000;
}
.upcomment {
  margin-bottom: 16px;
  height: 36px;
}
.writer {
  font-size: small;
}
.time {
  font-size: small;
}
.comment-content {
  font-size: x-large;
}
.button-container {
  display: flex;
  margin: 5px;
  justify-content: end;
}
.btn-comment {
  margin-left: 10px;
}
</style>