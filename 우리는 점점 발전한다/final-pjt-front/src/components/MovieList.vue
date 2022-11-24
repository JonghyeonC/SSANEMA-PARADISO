<template>
  <div>
    <!-- <p>{{ movies }}</p> -->
    <div class="d-flex">   
      <div class="tong d-flex align-items-center text-center">
        <h3 class="mt-4">이번 달과 같은 달에 개봉한 영화</h3>
      </div>
      <swiper :options="swiperOptions" class="align-self-center">
        <MovieItem
          v-for="movie in month_filter"
          :key="`month${movie.id}`"
          :month_movie = "movie"
        />
        <div class="swiper-pagination" slot="pagination"></div>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
    </div>
    <div class="d-flex">
      <div class="tong d-flex align-items-center text-center">
        <h3 class="mt-4">가볍게 볼 수 있는 짧은 영화</h3>
      </div>
      <swiper :options="swiperOptions" class="align-self-center">
        <MovieItem
          v-for="movie in short_runtime"
          :key="`runtime${movie.id}`"
          :short_runtime = "movie"
        />
        <div class="swiper-pagination" slot="pagination"></div>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
    </div>
    <div class="d-flex">
      <div class="tong d-flex align-items-center text-center">
        <h3 class="mt-4">영화 목록 출력</h3>
      </div>
      <swiper v-once :options="swiperOptions" class="align-self-center">
        <MovieItem
          v-for="movie in movies"
          :key="`all${movie.id}`"
          :movie="movie"
        />
        <div class="swiper-pagination" slot="pagination"></div>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
    </div>
    <GenreMovieList/>
  </div>
</template>

<script>
import MovieItem from '@/components/MovieItem.vue'
import GenreMovieList from '@/components/GenreMovieList'
import _ from "lodash"
import 'swiper/dist/css/swiper.css'
import { swiper } from 'vue-awesome-swiper'

export default {
  name: 'MovieList',
  components: {
    MovieItem,
    GenreMovieList,
    swiper,
  },
  data() {
    return {
      swiperOptions : {
        slidesPerView: 7,
        spaceBetween: 0,
        freeMode: true,
        loop: false,
        autoplay: {
          delay: 2500,
          disableOnInteraction: false
        },
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev'
        }
      }
    }
  },
  computed: {
    movies() {
      return _.sampleSize(this.$store.state.movies, 30)
    },
    month_filter() {
      // console.log(this.$store.getters.month_filter)
      return this.$store.getters.month_filter
    },
    short_runtime() {
      return this.$store.getters.short_runtime
    },
  },
}
</script>

<style>
.swiper-slide{
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.swiper-container {
  height : 300px;
  width : 100%;
}
.tong {
  background-image: url(@/image/filmtong.png);
  background-size: 150px 560px;
  background-position: center;
  background-repeat: no-repeat;
  margin-bottom: 18px;
  height: 490px;
  width: 160px;
}
.movieImg {
  transition: all 0.2s linear;
}
.movieImg:hover {
  transform: scale(1.1);
}
</style>