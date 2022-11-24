<template>
  <span>
    <img v-if="this.movie" class="rounded" :src="imgSRC" :height="150" @click="goDetail">
  </span>
</template>

<script>
export default {
name: 'LikeMovieListItem',
props: {
  movie: Object,
},
computed: {
  imgSRC(){
    return `https://image.tmdb.org/t/p/w400${this.movie?.poster_path}`
  },
},
methods: {
  goDetail() {
    this.$router.push({name: 'DetailView', params: { id: this.movie.id }})
  },
}
}
</script>

<style>

</style>