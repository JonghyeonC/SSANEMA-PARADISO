<template>
  <div class="container">
    <div class="homeword rounded d-flex">
      <div class="col-5 align-items-center mt-5">
        <h3 class="mt-5">오늘은 어떤 영화가 보고싶으신가요?</h3>
        <div>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'ActionView' }">액션</router-link></button>      
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'AnimationView' }">애니메이션</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'AdventureView' }">모험</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'ComedyView' }">코미디</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'CriminalView' }">범죄</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'DocumentaryView' }">다큐멘터리</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'DramaView' }">드라마</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'FamilyView' }">가족</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'FantasyView' }">판타지</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'HistoryView' }">역사</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'HorrorView' }">공포</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'MusicView' }">음악</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'MysteryView' }">미스터리</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'RomanceView' }">로맨스</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'SFView' }">SF</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'ThrillerView' }">스릴러</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'TvmovieView' }">TV영화</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'WarView' }">전쟁</router-link></button>
          <button type="button" class="btn btn-outline-secondary mx-2 my-2"><router-link class="genrebtn" :to="{ name: 'WesternView' }">서부</router-link></button>
        </div>
      </div>
      <div class="col-7 container">
        <form @submit.prevent="getSearch" class="d-flex flex-row p-3 searchmt">
          <input class="form-control me-4" type="text" placeholder="Search" v-model="searchObj">
          <button type="submit" class="btn btn-secondary me-4">Search</button>
        </form>
      </div>
    </div>
    <MovieList/>
    <hr>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'HomeView',
  components: {
    MovieList,
  },
  data() {
    return {
      searchObj: null,
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getMovies()
    this.getUser()
  },
  methods: {
    getSearch() {
      if (this.searchObj !== '') {
        this.$router.push({name: 'Search', params: { content: this.searchObj }})
        this.$router.go()
        this.searchObj = ''
      }
    },
    getUser() {
      // console.log('create')
      return this.$store.dispatch('getUser')
    },
    getMovies(){
        this.$store.dispatch('getMovies')
        this.$store.dispatch('getGenre')
    }
  }
}
</script>

<style>
.homeword {
  height: 500px;
  /* background-color: gray; */
  background-image: url(@/image/플레이트.png);
  background-position: right;
  background-repeat: no-repeat;
  background-size: 800px 500px;
}
.genrebtn {
  text-decoration: none;
  color: rgb(83, 83, 83)
}
.searchmt {
  margin-top: 240px;
}
</style>
