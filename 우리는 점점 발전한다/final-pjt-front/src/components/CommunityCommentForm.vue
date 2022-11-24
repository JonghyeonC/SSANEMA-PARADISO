<template>
  <div class="AddWrap">
    <form @submit.prevent="createComment" @key.up="createComment">
      <table class="tbAdd">
        <colgroup>
          <col width="*"/>
        </colgroup>
        <tr>
          <th><label for="comment">댓글 작성</label></th>
        </tr>
        <tr>
          <td><textarea id="content" v-model.trim="comment_content" placeholder="댓글을 작성해주세요!!"></textarea></td>
        </tr>
      </table>
        <div class="btnWrap">
          <button class="btn btn-outline-success">댓글 작성</button>
        </div>
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
      comment_content: '',
    }
  },
  methods: {
    createComment() {
      const commentItem = {
        content : this.comment_content,
        community_id: this.$route.params.id
      }
      if (commentItem.content) {
        axios({
          method: 'post',
          url: `${API_URL}/api/v1/community/${this.$route.params.id}/comments/`,
          data: commentItem,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$store.commit('GET_COMMENT', this.$route.params.id)
          this.comment_content = ''
        })
      }
    },
  }
}
</script>

<style>
table{width:100%; border-collapse:collapse;}
.wrap{width:100%;}
.container{width:800px; margin:0 auto;}
a{text-decoration:none;}

.tbAdd{border-top:1px solid #888;}
.tbAdd th, .tbAdd td{border-bottom:1px solid #eee; padding:5px 0;}
.tbAdd td{padding:10px 10px; box-sizing:border-box;}
.tbAdd td input{width:100%; min-height:30px; box-sizing:border-box; padding:0 10px;}
.tbAdd td textarea{width:100%; min-height:300px; padding:10px; box-sizing:border-box;}
.btnWrap{text-align:center; margin:20px 0 0 0;}
.btnWrap a{margin:0 10px;}
</style>