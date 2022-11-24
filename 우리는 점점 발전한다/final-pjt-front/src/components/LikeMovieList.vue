<template>
  <div class="ilikemovie">
    <h3>좋아요한 영화</h3>
    <!-- <p>{{ likeMovies }}</p> -->
    <div class="d-flex overflow-auto" v-dragscroll>
      <div v-if="!likeMovies?.length && profile">
        <p class="empty-case">좋아요한 영화가 없습니다. 영화 취향을 알려주시겠습니까?</p>
        <button type="button" class="btn btn-outline-light "><router-link :to="{ name: 'TinderView' }" class="go-tinder ">Let's Go</router-link></button>
      </div>
      <LikeMovieListItem
        v-for="movie in likeMovies"
        :key="`like-${movie.id}`"
        :movie="movie"
      />  
    </div>
  </div>
</template>

<script>
import { dragscroll } from 'vue-dragscroll'
import LikeMovieListItem from '@/components/LikeMovieListItem'

export default {
  directives: {
    dragscroll
  },
  name: 'LikeMovieList',
  props: {
    movies_id : Array,
    profile: Boolean,
  },
  components: {
    LikeMovieListItem,
  },
  computed: {
    likeMovies() {
      // console.log(typeof this.movies_id)
      const likeMovies = this.$store.state.movies.filter(movie=> {
        
        return this.movies_id?.includes(movie.id) 
      })
      return likeMovies
    }
  },
}
</script>

<style>
.ilikemovie{
  margin: 10px;
}
.empty-case{
  margin-inline: auto;
}
.go-tinder{
  text-decoration: none;
  color: white;
}
</style>