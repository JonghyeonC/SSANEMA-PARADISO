<template>
  <div class="container">
    <div class='d-flex movie-data p-3 rounded' :style="{ backgroundImage: 'linear-gradient( rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5) ), url(' + backGroundImage + ')' }">
      <div>
        <img class="rounded" :src="imgSRC" alt="">
      </div>
      <div class="text-center row justify-content-center">
        <div class="row justify-content-center align-self-start">
          <span class="col-1"></span>
          <span class="col-4 fs-3 btn" @click="switchInfo" :class="{'btn-secondary': select}">INFO</span>
          <span class="col-2"></span>
          <span class="col-4 fs-3 btn" @click="switchTrailer" :class="{'btn-secondary': !select}">TRAILER</span>
          <span class="col-1"></span>
        </div>
        <div v-if="select">
          <h3>{{ movie?.title }}({{ movie?.release_date.substring(0,4) }})</h3>
          <span>{{ movie?.release_date }} | {{ movieGenre.join() }} | ★{{ movie?.vote_average }} | {{ parseInt(movie?.runtime/60) }}h {{ movie?.runtime%60 }}m</span>
          <p v-if="movie?.overview" class="p-5">내용 : {{ movie?.overview }}</p>
        </div>
        <div v-if="!select">
          <iframe class="rounded" width="560" height="315" :src="videoUrl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>
        <div class="justify-content-center align-self-end d-flex justify-content-evenly">
          <!-- <button style="width:100px" @click="deBug">DEBUG</button> -->
          <star-rating active-color="#fc0d0d" v-model="boundRating" v-if="rankedMovie === false" @rating-selected ="setRating"></star-rating>
          <star-rating active-color="#fc0d0d" v-model="boundRating" v-if="rankedMovie === true" @rating-selected ="updateRating"></star-rating>
          <button type="button" class="btn btn-danger" @click="dislikeMovie" v-if="likedMovie"><i class="bi bi-chat-heart fs-4" width="25" height="25" viewBox="0 0 16 16"></i></button>
          <button type="button" class="btn btn-outline-danger" @click="likeMovie" v-if="!likedMovie"><i class="bi bi-chat-heart fs-4" width="25" height="25" viewBox="0 0 16 16"></i></button>
        </div>
      </div>
    </div>
    <!-- <span v-for="genre in movieGenre"
    :key="`genre${genre.name}`"
    >
    {{ genre }}
    </span> -->
    <br>
    <hr>
    <p>캐스팅 정보</p>
    <div class="accordion">
      <div class="d-flex overflow-auto" v-dragscroll>
        <div v-for="person in casts" :key="`person${person.id}`">
          <div class="card d-inline-flex" style="width: 7rem; height: 12rem;">
            <img @click="personUrl(person)" :src="(personImg(person))" :height="100" class="card-img-top" alt="...">
            <div class="card-body card-color">
              <p style="font-size:xx-small">{{ person.name }}</p>
            </div>
          </div>
        </div>
      </div>
      <button v-if="casts_check" type="button" class="btn btn-light accordion-button collapsed rounded" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">더보기</button>
      <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
        <div class="accordion-body">
          <div v-for="person in casts_extend" :key="`person${person.id}`">
            <div class="card float-start" style="width: 7rem; height: 12rem;">
              <img @click="personUrl(person)" :src="(personImg(person))" :height="100" class="card-img-top" alt="...">
              <div class="card-body card-color">
                <p style="font-size:xx-small">{{ person.name }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br style="clear:both">
    <hr>
    <p>비슷한 영화</p>
    <div class="d-flex overflow-auto" v-dragscroll>
      <span v-for="s_movie in sMovies" :key="`sMovie${s_movie.id}`">
        <img class="rounded" :src="(s_imgSRC(s_movie))" :height="150" alt="" @click="sMovieGet(s_movie)">
      </span>
    </div>
    <hr>
    <CommentList
      v-for="comment in comments"
      :key="`comment${comment.id}`"
      :comment="comment"
    />
    <CommentCreateForm
      class="p-3"
    />
  </div>
</template>

<script>
import { dragscroll } from 'vue-dragscroll'
import CommentCreateForm from '@/components/CommentCreateForm'
import CommentList from '@/components/CommentList'
import axios from 'axios'
import StarRating from 'vue-star-rating'
import _ from 'lodash'
const API_URL = "http://127.0.0.1:8000"

export default {
  directives: {
    dragscroll
  },
  name: 'DetailView',
  data() {
    return{
      movie: null,
      genres: null,
      casts: null,
      casts_extend: null,
      casts_check: true,
      sMovies: null,
      select: true,
      rating: "No Rating Selected",
      currentRating: "No Rating",
      currentSelectedRating: "No Current Rating",
      boundRating: 0,
      rankedMovie: false,
      rank_id: null,
      // imgSRC: `https://image.tmdb.org/t/p/w400${this.movie.poster_path}`,
    }
  },
  components: {
    CommentCreateForm,
    CommentList,
    StarRating,
  },
  computed: {
    videoUrl() {
      return `https://www.youtube.com/embed/${this.movie?.video_url[0].key}`
    },
    imgSRC(){
      return `https://image.tmdb.org/t/p/w300${this.movie?.poster_path}`
    },
    backGroundImage() {
      return `https://image.tmdb.org/t/p/w500${this.movie?.backdrop_path}`
    },
    movieGenre() {
      const genreList = this.movie?.genres
      const genreLastList = []
      this.genres?.forEach((genre) => {
        // console.log(movie.genres)
        // console.log(genre)
        if (genreList?.includes(genre.id)) {
          genreLastList.push(genre.name)
        }
      })
      return genreLastList
    },
    likedMovie() {
      const checking = (element) => element === this.movie?.id;
      return this.$store.state.user.like_movies.some(checking)
    },
    comments() {
      return this.$store.state.movie_comment
    }
  },
  created() {
    this.getMovieDetail()
    this.getGenre()
    this.getRating()
    this.$store.commit('GET_MOVIE_COMMENT', this.$route.params.id)
    this.cast_info()
    this.sMovieList()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/`,
      })
      .then(res=>{
        // console.log(res)
        this.movie = res.data
      })
      .catch(err => console.log(err))
    },
    getGenre() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/genre/`,
        
      })
        .then(res=> {
          // console.log(res, context)
          this.genres = res.data
        })
        .catch(err => console.log(err))
    },
    dislikeMovie() {
      axios({
        method: 'post',
        url: `${API_URL}/api/accounts/like_movies/${this.movie.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(res=> {
          this.$store.state.user = res.data
          this.getMovieDetail()
        })
        // .then(()=> {
        //   this.$store.commit('MovieDislike', this.movie.genres)
        // })
        // .catch(err => console.log(err))
    },
    likeMovie() {
      axios({
        method: 'post',
        url: `${API_URL}/api/accounts/like_movies/${this.movie.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(res=> {
          this.$store.state.user = res.data
          this.getMovieDetail()
          // console.log(res)
        })
        // .then(()=> {
        //   this.$store.commit('MovieLike', this.movie.genres)
        // })
        // .catch(err => console.log(err))
    },
    personUrl(data) {
      window.open(`https://www.themoviedb.org/person/${data.id}`, "_blank")
    },
    personImg(data){
      if (data.profile_path) {
        return `https://image.tmdb.org/t/p/w400${data.profile_path}`
      } else {
        return 'https://en.pimg.jp/037/250/395/1/37250395.jpg'
      }
    },
    sMovieGet(data) {
      const sMovie = this.$store.state.movies.filter((movie) => {
        return movie.movie_id === data.id[0]
      })
      if (sMovie.length === 1) {
        this.$router.push({name: 'DetailView', params: { id: sMovie[0].id }})
        this.$router.go()
      } else {
        window.open(`https://www.themoviedb.org/movie/${data.id[0]}`, "_blank")
      }
    },
    s_imgSRC(data) {
      return `https://image.tmdb.org/t/p/w400${data.poster_path}`
    },
    deBug() {
      console.log(this.sMovies)
    },
    cast_info() {
      setTimeout(() => {
        if (this.movie?.cast_info.length <= 12) {
          this.casts_check = false
          this.casts = this.movie?.cast_info
        } else {
          this.casts_check = true
          this.casts = this.movie?.cast_info.slice(0, 12)
          this.casts_extend = this.movie?.cast_info.slice(12)
        }
      }, 100);
    },
    sMovieList() {
      setTimeout(() => {
        this.sMovies = _.sampleSize(this.movie?.similar_movies, 12)
        // this.sMovies = this.movie?.similar_movies
      }, 100);
    },
    switchInfo() {
      this.select = true
    },
    switchTrailer() {
      this.select = false
    },
    setRating(rating) {
      this.rating = rating
      const rank = this.rating
      this.boundRating = rating
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/rank/${this.movie.id}/created/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: { 
          rank,
        },
      })
      .then(res => {
        this.rankedMovie = true
        this.rank_id = res.data.id
      })
    },
    updateRating(rating) {
      this.rating = rating
      const rank = this.rating
      this.boundRating = rating
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/rank/updated/${this.movie.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: { 
          rank,
        },
      })
      .then(res => {
        this.rankedMovie = true
        console.log(res)
      })
    },
    getRating() {
      // console.log(this.movie.rank)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/rank/updated/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
      .then(res => {
        this.boundRating = res.data.rank
        this.rankedMovie = true
        // this.boundRating = res.data.rank
        // this.rating = res.data.rank
      })
    },
  }
}
</script>

<style>
.movie-data {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
.custom-text {
  font-weight: bold;
  font-size: 1.9em;
  border: 1px solid #cfcfcf;
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 5px;
  color: #999;
  background: #fff;
}
.rgba {
  background-color: gray;
}
.card-color {
  background-color: rgba(70, 131, 149, 0.5);
}
</style>