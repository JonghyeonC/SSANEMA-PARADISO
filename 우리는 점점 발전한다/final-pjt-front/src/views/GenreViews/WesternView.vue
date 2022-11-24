<template>
  <div class="container">
    <h2>서부 영화추천</h2>
    <div>
      <GenreMovieRecom
      v-for="movie in movies"
      :key="`war${movie.id}`"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import GenreMovieRecom from '@/components/GenreMovieRecom'

export default {
  name: 'WesternView',
  components: {
    GenreMovieRecom,
  },
  computed: {
    movies() {
      return this.$store.getters.western_movies
    }
  }
}
</script>

<style>
.genre_recom {
  display: flex;
}
</style>