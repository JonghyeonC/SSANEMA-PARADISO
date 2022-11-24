<template>
  <div class="icheckmovie">
    <h3>평가한 영화</h3>
    <div class="d-flex overflow-auto" v-dragscroll>
      <div v-if="!movie_ids?.length && profile">
        <p class="empty-case">평가한 영화가 없습니다. 영화를 평가하러 가겠습니까?</p>
        <button type="button" class="btn btn-outline-light "><router-link :to="{ name: 'HomeView' }" class="go-tinder ">Let's Go</router-link></button>
      </div>
      <MyRankedMovieListItem
        v-for="movie_id in movie_ids"
        :key="`rank-${movie_id.idx}`"
        :movie="movie_id.movie"
      />
    </div>
  </div>
</template>

<script>
import MyRankedMovieListItem from '@/components/MyRankedMovieListItem'
import { dragscroll } from 'vue-dragscroll'

export default {
  directives: {
    dragscroll
  },
  name: 'MyRankedMovieList',
  components: {
    MyRankedMovieListItem,
  },
  props: {
    movie_ids: Array,
    profile: Boolean,
  },
}

</script>

<style>
.icheckmovie{
  margin: 10px;
}

</style>