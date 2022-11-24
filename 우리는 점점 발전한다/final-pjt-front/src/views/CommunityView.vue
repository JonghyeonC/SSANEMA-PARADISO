<template>
  <div class="container">
    <br>
    <div>
      <h1>자유게시판</h1>
    </div>
    <hr>
    <CommunityList
      v-if="this.$store.state.communities"
    />
    <div class="btnRightWrap">
      <router-link :to="{ name: 'CommunityCreate'}">
        <button type="button" class="btn btn-outline-secondary">글 작성하기</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import CommunityList from '@/components/CommunityList'

export default {
  name: "CommunityView",
  components : {
    CommunityList,
  },
  created() {
    this.getCommunity()
  },
  methods:{
    getCommunity() {
      return this.$store.dispatch('getCommunity')
    }
  }
}
</script>

<style>
.btnRightWrap{text-align:right; margin:10px 0 0 0;}
</style>