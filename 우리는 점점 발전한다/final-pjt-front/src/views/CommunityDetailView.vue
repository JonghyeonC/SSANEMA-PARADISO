<template>
  <div class="container">
    <br>
    <h1>게시글 상세보기</h1>
    <div class="AddWrap">
      <form>
        <table class="tbAdd">
          <colgroup>
            <col width="15%"/>
            <col width="*"/>
          </colgroup>
          <tr>
            <th>작성자</th>
            <td>
              <router-link :to="{ name: 'MyPageView' }" v-if="community?.username === this.$store.state.user.username" class="detail_name">{{ community?.username }}</router-link>
              <router-link :to="{ name: 'ProfileView', params:{ username: community?.username } }" v-if="community?.username !== this.$store.state.user.username" class="detail_name">{{ community?.username }}</router-link>
            </td>
          </tr>
          <tr>
            <th>제목</th>
            <td>{{ community?.title }}</td>
          </tr>
          <tr>
            <th>내용</th>
            <td>{{ community?.content }}</td>
          </tr>
          <tr>
            <th>작성시간</th>
            <td>{{ community?.created_at.substring(0,4) }}년 {{ community?.created_at.substring(5,7) }}월 {{ community?.created_at.substring(8,10) }}일 {{ community?.created_at.substring(11,13) }}:{{ community?.created_at.substring(14,16) }}:{{ community?.created_at.substring(17,19) }}</td>
          </tr>
          <tr>
            <th>수정시간</th>
            <td>{{ community?.updated_at.substring(0,4) }}년 {{ community?.updated_at.substring(5,7) }}월 {{ community?.updated_at.substring(8,10) }}일 {{ community?.updated_at.substring(11,13) }}:{{ community?.updated_at.substring(14,16) }}:{{ community?.updated_at.substring(17,19) }}</td>
          </tr>
        </table>
      </form>
    </div>
    <div class="btnWrap">
      <div v-if="community?.username === this.$store.state.user.username">
        <button class="btn btn_detail btn-outline-success" @click="updateCommunity(community)">수정</button>
        <button class="btn btn_detail btn-outline-danger" @click="deleteCommunity(community)">삭제</button>
      </div>
      <button class="btn btn_detail btn-outline-primary"><router-link :to="{ name: 'CommunityView' }" class="community_go">목록</router-link></button>
    </div>
    <br>
    <CommunityCommentForm/>
    <CommunityCommentList/>
  </div>
</template>

<script>
import CommunityCommentForm from '@/components/CommunityCommentForm'
import CommunityCommentList from '@/components/CommunityCommentList'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommunityDetail',
  components: {
    CommunityCommentForm,
    CommunityCommentList
  },
  data() {
    return {
      community: null,
      // comment_content: '',
      // comments: [],
    }
  },
  methods: {
    // 게시글
    getCommunityDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${this.$route.params.id}/`,
      })
      .then(res => {
        this.community = res.data
      })
      .catch(err => console.log(err))
    },
    updateCommunity(community) {
      this.$router.push({ name: 'CommunityUpdate', params: { id: `${community.id}`}})
    },
    deleteCommunity(community) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/${community.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        if (res.statusText === 'No Content') {
          this.$router.push({ name: 'CommunityView' })
        }
      })
    },
  },
    created() {
    this.getCommunityDetail()
    this.$store.commit('GET_COMMENT', this.$route.params.id)
  },
}
</script>

<style>
.tbAdd{border-top:1px solid #888;}
.tbAdd th, .tbAdd td{border-bottom:1px solid #eee; padding:5px 0; }
.tbAdd td{padding:10px 10px; box-sizing:border-box; text-align:left;}
.tbAdd td.txt_cont{height:300px; vertical-align:top;}
.btnWrap{text-align:center; margin:20px 0 0 0;}
.btnWrap a{margin:0 10px;}
.btnWrap {
  display: flex;
  justify-content: right;
}
.detail_name {
  text-decoration: none;
  color: black;
  font-weight: 550;
}
.btn_detail {
  margin-right: 10px;
  width: 80px;
}
.community_go {
  text-decoration: none;
}
</style>