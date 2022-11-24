<template>
  <span class="d-flex mx-2">
    <div v-if="movie1" class="card float-start recom_card card_image">
      <figure>
        <img :src="imgSRC1" @click="goDetail1" class="image_card">
        <div class="overlay">
          <div class="description" @click="goDetail1">
            {{ movie1.title }}
          </div>
        </div>
      </figure>
    </div>
    <div v-if="movie2" class="card float-start recom_card card_image">
      <figure>
        <img :src="imgSRC2" @click="goDetail2" class="image_card">
        <div class="overlay">
          <div class="description" @click="goDetail2">
            {{ movie2.title }}
          </div>
        </div>
      </figure>
    </div>
    <div v-if="movie3" class="card float-start recom_card card_image">
      <figure>
        <img :src="imgSRC3" @click="goDetail3" class="image_card">
        <div class="overlay">
          <div class="description" @click="goDetail3">
            {{ movie3.title }}
          </div>
        </div>
      </figure>
    </div>
  </span>
</template>

<script>
export default {
  name: 'GenreMovieListItem',
  props: {
    movie1: Object,
    movie2: Object,
    movie3: Object,
  },
  computed: {
    imgSRC1(){
      return `https://image.tmdb.org/t/p/w400${this.movie1?.poster_path}`
    },
    imgSRC2(){
      return `https://image.tmdb.org/t/p/w400${this.movie2?.poster_path}`
    },
    imgSRC3(){
      return `https://image.tmdb.org/t/p/w400${this.movie3?.poster_path}`
    },
  },
  methods: {
    goDetail1() {
      this.$router.push({name: 'DetailView', params: { id: this.movie1.id }})
    },
    goDetail2() {
      this.$router.push({name: 'DetailView', params: { id: this.movie2.id }})
    },
    goDetail3() {
      this.$router.push({name: 'DetailView', params: { id: this.movie3.id }})
    },
  },
  created() {
    // console.log(this.movie)
  }
}
</script>

<style>

</style>