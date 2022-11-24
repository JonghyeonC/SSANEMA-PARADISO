<template>
  <div class="container">
    <h2>스릴러 영화추천</h2>
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
  name: 'ThrillerView',
  components: {
    GenreMovieRecom,
  },
  computed: {
    movies() {
      return this.$store.getters.thriller_movies
    }
  }
}
</script>

<style>
.genre_recom {
  display: flex;
}
</style>