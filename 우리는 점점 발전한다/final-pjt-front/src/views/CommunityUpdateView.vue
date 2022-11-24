<template>
  <div class="container">
    <br>
    <h1>게시판 수정</h1>
    <br>
    <div class="AddWrap">
      <form @submit.prevent="updateCommunity(community)">
        <table class="tbAdd">
          <colgroup>
            <col width="15%"/>
            <col width="*"/>
          </colgroup>
          <tr>
            <th><label for="title">제목 : </label></th> 
            <td><input type="text" id="title" v-model.trim='community.title'><br></td>
          </tr>
          <tr>
            <th><label for="content">내용 : </label></th>
            <td><textarea id="content" v-model.trim='community.content'></textarea></td>
          </tr>
        </table>
        <div class="btnWrap">
          <router-link :to="{ name: 'CommunityView' }"><button class="btn btn-outline-primary">목록</button></router-link>
          <button class="btn btn-outline-success">수정</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'CommunityUpdate',
  data() {
    return {
      community: [],
    }
  },
  created() {
    this.getCommunityDetail()
  },
  methods: {
    getCommunityDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${this.$route.params.id}/`,
      })
      .then(res => {
        // console.log(res)
        this.community = res.data
      })
      .catch(err => console.log(err))
    },
    updateCommunity(community) {
      const communityItem = {
        title : community.title,
        content : community.content
      }
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/community/${community.id}/`,
        data: communityItem,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.push({ name: 'CommunityDetail', params: { id: `${community.id}` }})
      })
      .catch(err => {
        console.log(err)
      })
    }
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