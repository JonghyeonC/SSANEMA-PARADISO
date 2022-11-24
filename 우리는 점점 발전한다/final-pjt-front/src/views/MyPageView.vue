<template>
  <div class="mypage container">
    <img src="@/image/mypage.png" alt="" :height="100">
    <div class="maypage_middle d-flex">
      <div class="user-basic col-1">
        <!-- <h1>MyPage</h1> -->
        <p>감독 : {{ user?.username }}</p>
        <p>팔로우 : {{ user?.followings.length}}</p>
        <p>팔로워 : {{ user?.followers.length}}</p>
      </div>
      <div class="user_info col-11 p-4 container">
        <div class="accordion" id="accordionExample" >
          <LikeMovieList 
            :movies_id="user?.like_movies"
            :profile=true
          />
          <hr class="mypage_hr">
          <MyRankedMovieList 
            :movie_ids="user?.ranks"
            :profile=true
          />
          <hr class="mypage_hr">
          <MyCommentList
            :comments="user?.comments"
            :profile=true
          />
          <hr class="mypage_hr">
          <MyCommunityList 
            :community_set="user?.community_set"
            :profile=true
          />
          <hr class="mypage_hr">
          <MyCommunityCommentList
            :community_comment="user?.community_comment"
            :profile=true
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LikeMovieList from '@/components/LikeMovieList'
import MyCommunityList from '@/components/MyCommunityList'
import MyCommunityCommentList from '@/components/MyCommunityCommentList'
import MyCommentList from '@/components/MyCommentList'
import MyRankedMovieList from '@/components/MyRankedMovieList'

export default {
  name: 'MyPageView',
  components: {
    LikeMovieList,
    MyCommunityList,
    MyCommentList,
    MyCommunityCommentList,
    MyRankedMovieList,
  },
  computed: {
    user() {
      return this.$store.state.user
    },
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      // console.log('create')
      return this.$store.dispatch('getUser')
    },
  }
  
}
</script>

<style>
/* .container {
  } */
.mypage{
  background-color: black;
  color: aliceblue;
  margin: 0;
  background-image: url("@/image/projector.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
  background-color: transparent;
  padding: 25px;
  height: 80vh;
}
.maypage_middle{
  display: flex;
  flex-direction: row;
}
.user-basic{
  display: flex;
  flex-direction: column;
  width: calc(100% / 6);
  margin: 10px;
  padding: 10px;
}
.user_info{
  display: flex;
  flex-direction: column;
  margin: 10px;
  padding: 10px;
  overflow-x: hidden;
  height: 60vh;
}
.mypage_hr{
  background-color: white;
  color: white;
  border: 0;
  border-top: 5px solid;
  opacity: 0.25;
}
</style>