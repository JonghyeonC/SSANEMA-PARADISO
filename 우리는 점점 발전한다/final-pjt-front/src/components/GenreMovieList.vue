<template>
  <div>
    <div class="d-flex align-items-center text-center">
      <h1>{{ genres[0]?.name }}</h1>
      <GenreMovieListItem
        v-for="movie1 in recGenre1"
        :key="`recGenre1${movie1.id}`"
        :movie1="movie1"
      />
      <span class="btn" @click="routerGenre1">MORE</span>
    </div>
    <div class="d-flex align-items-center text-center">
      <h1>{{ genres[1]?.name }}</h1>
      <GenreMovieListItem
        v-for="movie2 in recGenre2"
        :key="`recGenre2${movie2.id}`"
        :movie2="movie2"
      />
      <span class="btn" @click="routerGenre2">MORE</span>
    </div>
    <div class="d-flex align-items-center text-center">
      <h1>{{ genres[2]?.name }}</h1>
      <GenreMovieListItem
        v-for="movie3 in recGenre3"
        :key="`recGenre3${movie3.id}`"
        :movie3="movie3"
      />
      <span class="btn" @click="routerGenre3">MORE</span>
    </div>
  </div>
</template>

<script>
import _ from "lodash"
import GenreMovieListItem from '@/components/GenreMovieListItem'

export default {
  name: 'GenreMovieList',
  data() {
    return {
      allGenres: [
        [ '액션', 'ActionView' ],
        [ '애니메이션', 'AnimationView' ],
        [ '모험', 'AdventureView' ],
        [ '코미디', 'ComedyView' ],
        [ '범죄', 'CriminalView' ],
        [ '다큐멘터리', 'DocumentaryView' ],
        [ '드라마', 'DramaView' ],
        [ '가족', 'FamilyView' ],
        [ '판타지', 'FantasyView' ],
        [ '역사', 'HistoryView' ],
        [ '공포', 'HorrorView' ],
        [ '음악', 'MusicView' ],
        [ '미스터리', 'MysteryView' ],
        [ '로맨스', 'RomanceView' ],
        [ 'SF', 'SFView' ],
        [ '스릴러', 'ThrillerView' ],
        [ 'TV영화', 'TvmovieView' ],
        [ '전쟁', 'WarView' ],
        [ '서부', 'WesternView' ],
      ]
    }
  },
  components: {
    GenreMovieListItem,
  },
  computed: {
    genres() {
      return this.$store.state.genres
    },
    recGenre1() {
      if (this.$store.state.recGenre1.length > 4) {
        return _.sampleSize(this.$store.state.recGenre1, 4)
      } else {
        return this.$store.state.recGenre1
      }
    },
    recGenre2() {
      if (this.$store.state.recGenre2.length > 4) {
        return _.sampleSize(this.$store.state.recGenre2, 4)
      } else {
        return this.$store.state.recGenre2
      }
    },
    recGenre3() {
      if (this.$store.state.recGenre3.length > 4) {
        return _.sampleSize(this.$store.state.recGenre3, 4)
      } else {
        return this.$store.state.recGenre3
      }
    },
  },
  methods: {
    recGenre() {
      return this.$store.dispatch('recGenre')
    },
    routerGenre1() {
      const genre = this.allGenres.filter((data) =>{
        return this.genres[0].name === data[0]
      })
      this.$router.push({name: genre[0][1]})
    },
    routerGenre2() {
      const genre = this.allGenres.filter((data) =>{
        return this.genres[1].name === data[0]
      })
      this.$router.push({name: genre[0][1]})
    },
    routerGenre3() {
      const genre = this.allGenres.filter((data) =>{
        return this.genres[2].name === data[0]
      })
      this.$router.push({name: genre[0][1]})
    },
  },
  created() {
    this.recGenre()
  },
}
</script>

<style>

</style>