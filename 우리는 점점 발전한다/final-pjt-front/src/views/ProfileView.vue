<template>
  <div class="mypage container">
    <img src="@/image/profile.png" alt="" :height="100">
    <div class="maypage_middle container">

      <div class="user-basic col-1">
        <p>감독 : {{ user?.username }}</p>
        <p>팔로우 : {{ followings_count }}</p>
        <p>팔로워 : {{ followers_count }}</p>
        <button type="button" @click="follow" class="btn btn-outline-secondary">{{ follow_check? '언팔': '팔로우'}}</button>
        <!-- <button @click="follow">{{ follow_check? 'unfollow': 'follow'}}</button> -->
      </div>
      <div class="user_info col-11 p-4 container">
        <div class="accordion" id="accordionExample" >
          <LikeMovieList 
            :movies_id="user?.like_movies"
            :profile=false
          />
          <hr class="mypage_hr">
          <MyRankedMovieList 
            :movie_ids="user?.ranks"
            :profile=false
          />
          <hr class="mypage_hr">
          <MyCommentList
            :comments="user?.comments"
            :profile=false
          />
          <hr class="mypage_hr">
          <MyCommunityList 
            :community_set="user?.community_set"
            :profile=false
          />
          <hr class="mypage_hr">
          <MyCommunityCommentList
            :community_comment="user?.community_comment"
            :profile=false
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LikeMovieList from '@/components/LikeMovieList'
import MyCommunityList from '@/components/MyCommunityList'
import MyCommentList from '@/components/MyCommentList'
import MyRankedMovieList from '@/components/MyRankedMovieList'
import MyCommunityCommentList from '@/components/MyCommunityCommentList'

import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"

export default {
  name: 'ProfileView',
  components: {
    LikeMovieList,
    MyCommunityList,
    MyCommentList,
    MyRankedMovieList,
    MyCommunityCommentList,
  },
  data() {
    return {
      user: null,
    }
  },
  created() {
    this.getProfile()
  },
  props: {
    username() {
      return this.$route.params.username
    }
  },
  computed: {
    followings_count() {
      return this.user?.followings.length
    },
    followers_count() {
      return this.user?.followers.length
    },
    me() {
      return this.$store.state.user
    },
    follow_check() {
      const checking = (element) => element.username === this.me.username;
      return this.user?.followers.some(checking)
    }
  },
  methods: {
    getProfile() {
      axios({
        method: 'get',
        url: `${API_URL}/api/accounts/profile/${this.username}/`,
      })
      .then(res => {
        console.log(res)
        this.user = res.data
      })
      .catch(err => console.log(err))
    },
  
    follow() {
      axios({
        method: 'post',
        url: `${API_URL}/api/accounts/follow/${this.username}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(res => {
        console.log(res)
        this.user = res.data
        // this.community = res.data
      })
      .catch(err => console.log(err))
    },
    
  }
}
</script>

<style>

</style>