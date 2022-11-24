<template>
  <div class="search container">
    <h1>검색 결과</h1>
    <div v-if="searchResult.length >= 1">
      <SearchMovie v-for="movie in searchResult" :movie="movie" :key="movie.id" />
    </div>
    <div id="result" class="row mt-5" v-else>
      <h2>검색 결과를 찾을 수 없습니다!</h2>
    </div>
  </div>
</template>

<script>
import SearchMovie from '@/components/SearchMovie'

export default {
  name: 'SearchView',
  components: {
    SearchMovie
  },
  data() {
    return {
      keyword: this.$route.params.content,
    }
  },
  methods: {
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    genres() {
      return this.$store.state.allgenres
    },
    searchResult() {
      let res = []
      for (const movie of this.movies) {
        const actors = movie.cast_info.map((cast) => {
          return cast.name
        })
        if (actors.includes(this.keyword)){
          res.push(movie)
        } else if (movie.overview.includes(this.keyword)){
          res.push(movie)
        } else if (movie.original_title.includes(this.keyword)){
          res.push(movie)
        } else if (movie.title.includes(this.keyword)){
          res.push(movie)
        }
      }
      for (const genre of this.genres){
        if (genre.name.includes(this.keyword)) {
          const genre = this.genres.filter((genre) => {
            return genre.name.includes(this.keyword)
          })
          res = res.concat(this.movies.filter((movie) => {
            return movie.genres.includes(genre[0].id)
          }))
        }
      }
      return res
    },
    getMovies(){
      return this.$store.dispatch('getAllGenre')
    }
  },
  created(){
    this.getMovies
  }
}
</script>

<style>
#result{
  text-align: center;
}
</style>