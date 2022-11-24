<template>
  <div class="container">
    <h2>판타지 영화추천</h2>
    <div>
      <GenreMovieRecom
      v-for="movie in movies"
      :key="`animations${movie.id}`"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import GenreMovieRecom from '@/components/GenreMovieRecom'

export default {
  name: 'FantasyView',
  components: {
    GenreMovieRecom,
  },
  computed: {
    movies() {
      return this.$store.getters.fantasy_movies
    }
  }
}
</script>

<style>
.genre_recom {
  display: flex;
}
</style>