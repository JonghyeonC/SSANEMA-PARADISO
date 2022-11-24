<template>
  <div class="container">
    <h2>TV영화 영화추천</h2>
    <div>
      <GenreMovieRecom
      v-for="movie in movies"
      :key="`TVMovie${movie.id}`"
      :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import GenreMovieRecom from '@/components/GenreMovieRecom'

export default {
  name: 'TvmovieView',
  components: {
    GenreMovieRecom,
  },
  computed: {
    movies() {
      return this.$store.getters.tvmovie_movies
    }
  }
}
</script>

<style>
.genre_recom {
  display: flex;
}
</style>