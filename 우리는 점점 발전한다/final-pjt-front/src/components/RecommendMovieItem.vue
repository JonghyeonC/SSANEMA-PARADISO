<template>
  <div class="card float-start recom_card card_image" style="width: 18rem;" @click="goDetail">
    <img v-if="movie" class="rounded" :src="imgSRC" height="410px" @click="goDetail">
  </div>
</template>

<script>
export default {
name: 'RecommendMovieItem',
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
    this.$router.push({name: 'DetailView', params: { id: this.movie?.id }})
  },
}
}
</script>

<style>

</style>