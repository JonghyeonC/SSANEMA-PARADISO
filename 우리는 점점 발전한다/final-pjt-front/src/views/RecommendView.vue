<template>
  <div class="container">
    <h1>{{ user.username }}님을 위한 추천 영화</h1>
    <h3 v-if="!user?.like_movies.length">{{ user.username }}님의 취향에 대한 정보가 없습니다.</h3>
    <div v-if="user?.like_movies.length">
      <RecommendMovieItem 
        v-for="movie in movies"
        :key="`getrecmovie-${movie?.id}`"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = "http://127.0.0.1:8000"
import RecommendMovieItem from '@/components/RecommendMovieItem.vue'

export default {
  name: 'RecommendView',
  components: {
    RecommendMovieItem
  },

  computed: {
    movies() {
      return this.$store.getters.getRecommendMovie
    },
    user() {
      return this.$store.state.user
    } 
  },
  created() {
    this.getRecommendGenre(),
    this.getRecommendMovies()
  },
  methods: {
    getRecommendMovies() {
      axios({
        method: 'get',
        url: `${API_URL}/api/accounts/recommend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then((res) => {
        this.$store.state.user = res.data
        // console.log(res.data)
      })
      .catch((err) => console.log(err))   
    },
    getRecommendGenre() {
      this.$store.dispatch('GETRECOMMENDGENRE')
    }
  }
}
</script>

<style>

</style>