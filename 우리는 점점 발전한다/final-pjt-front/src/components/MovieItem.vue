<template>
  <swiperSlide class="film">
    <img class="rounded p-2 movieImg" v-if="this.movie" :src="imgSRC" :height="200" @click="goDetail">
    <img class="rounded p-2 movieImg" v-if="this.month_movie" :src="imgSRC_1" :height="200" @click="goDetail_1">
    <img class="rounded p-2 movieImg" v-if="this.short_runtime" :src="imgSRC_2" :height="200" @click="goDetail_2">
  </swiperSlide>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiperSlide } from 'vue-awesome-swiper'

export default {
  name: 'MovieItem',
  props: {
    movie: Object,
    month_movie: Object,
    short_runtime: Object,
  },
  components: {
    swiperSlide,
  },
  computed: {
    imgSRC(){
      return `https://image.tmdb.org/t/p/w400${this.movie?.poster_path}`
    },
    imgSRC_1() {
      return `https://image.tmdb.org/t/p/w400${this.month_movie?.poster_path}`
    },
    imgSRC_2() {
      return `https://image.tmdb.org/t/p/w400${this.short_runtime?.poster_path}`
    }
  },
  methods: {
    goDetail() {
      this.$router.push({name: 'DetailView', params: { id: this.movie.id }})
    },
    goDetail_1() {
      this.$router.push({name: 'DetailView', params: { id: this.month_movie.id }})
    },
    goDetail_2() {
      this.$router.push({name: 'DetailView', params: { id: this.short_runtime.id }})
    },
  }
}
</script>

<style>
  .film {
    background-size: 420px;
    background-image: url('@/image/filmdark.png');
  }
</style>