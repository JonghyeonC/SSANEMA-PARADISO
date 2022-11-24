<template>
  <div>
    <img v-if="this.movie" class="rounded" :src="imgSRC" :height="150" @click="goDetail">
  </div>
</template>

<script>
export default {
  name: 'LikeMovieListItem',
  props: {
    movie: Number,
  },
  computed: {
    movie_detail() {
      return this.$store.state.movies.filter((movie) => {
          return movie.id === this.movie
      })
    },
    imgSRC() {
      console.log(this.movie_detail)
      return `https://image.tmdb.org/t/p/w400${this.movie_detail[0].poster_path}`
    },
  },
  methods: {
    goDetail() {
      this.$router.push({name: 'DetailView', params: { id: this.movie }})
    },
  }
}
</script>

<style>

</style>