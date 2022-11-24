import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    allgenres: [],
    genres: [],
    like_genres: [],
    communities: [],
    recGenre1: null,
    recGenre2: null,
    recGenre3: null,
    token: null,
    login: false,
    authError: null,
    isAuthError: false,
    user: null,
    community_comment: [],
    movie_comment: [],
  },
  getters: {
    // 로그인
    isLogin(state) {
      return state.token ? true : false
    },
    // 회원가입시 유효성 검사
    isAuthError: state => state.isAuthError,
    authError: state => state.authError,
    
    // 회원 맞춤 영화
    getRecommendMovie(state) {
      const getRecommendMovie = []
      for (const genre_id in state.user.genre_recommend_dict) {
        // console.log(genre_id)
        const recMovie = state.movies.filter((movie) => {
          // console.log(movie.genres)
          if (movie.genres.includes(Number(genre_id))) {
            return !getRecommendMovie.includes(movie)
          }
        })
        // console.log(recMovie)
        getRecommendMovie.push(..._.sampleSize(recMovie, state.user.genre_recommend_dict[genre_id]))
      }
      return getRecommendMovie
    },
    // 오늘과 같은 달에 개봉한 영화
    month_filter(state) {
      return state.movies.filter((movie) => {
        const today = new Date()
        const movie_date = new Date(movie.release_date)
        return movie_date.getMonth()+1 === today.getMonth() + 1
      })
    },
    // 상영시간 짧은 영화
    short_runtime(state) {
      return state.movies.filter((movie) => {
        return Number(movie.runtime) <= 90 
      })
    },
    // 장르별 영화
    action_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(28)
      })
    },
    adventure_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(12)
      })
    },
    animation_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(16)
      })
    },
    comedy_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(35)
      })
    },
    criminal_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(80)
      })
    },
    documentary_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(99)
      })
    },
    drama_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(18)
      })
    },
    family_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(10751)
      })
    },
    fantasy_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(14)
      })
    },
    history_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(36)
      })
    },
    horror_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(27)
      })
    },
    music_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(10402)
      })
    },
    mystery_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(9648)
      })
    },
    romance_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(10749)
      })
    },
    sf_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(878)
      })
    },
    thriller_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(53)
      })
    },
    tvmovie_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(10770)
      })
    },
    war_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(10752)
      })
    },
    western_movies(state){
      return state.movies.filter((movie) => {
        return movie.genres.includes(37)
      })
    },
  },

  mutations: {
    GET_USER(state, user) {
      state.user = user
    },
    GET_COMMUNITY(state, communities) {
      state.communities = communities
      // console.log(state.login)
    },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_GENRES(state, genres) {
      state.genres = genres
    },
    GET_ALLGENRES(state, genres) {
      state.allgenres = genres
    },
    REC_GENRE(state) {
      const recGenre1 = state.movies.filter((movie) => {
        return movie.genres.includes(state.genres[0].id)
      })
      const recGenre2 = state.movies.filter((movie) => {
        return movie.genres.includes(state.genres[1].id)
      })
      const recGenre3 = state.movies.filter((movie) => {
        return movie.genres.includes(state.genres[2].id)
      })
      state.recGenre1 = recGenre1
      state.recGenre2 = recGenre2
      state.recGenre3 = recGenre3
    },
    SAVE_TOKEN(state, token){
      state.token = token
      state.login = true
      console.log(state.login)
      router.push({ name: 'HomeView'})
    },
    LOGOUT(state) {
      state.token = null
      state.login = false
      state.user = null
      // console.log(state.login)
      router.go()
    },
    SET_AUTH_ERROR: (state, error) => {
      state.authError = error
      state.isAuthError = true
    },
    GET_COMMENT(state, community_id) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${community_id}/comments/`,
        headers: {
          Authorization: `Token ${state.token}`
        },
      })
      .then((res) => {
        state.community_comment = res.data
      })
      .catch((err) => console.log(err))   
    },
    GET_MOVIE_COMMENT(state, movie_id) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movie_id}/comments/`,
        headers: {
          Authorization: `Token ${state.token}`
        },
      })
      .then((res) => {
        state.movie_comment = res.data
      })
      .catch((err) => console.log(err))   
    },
    MovieLike(state, genres) {
      for (let genre of genres) {
        state.like_genres.push(genre)
      }
    },
    MovieDislike(state, genres) {
      for (let genre of genres) {
        state.like_genres.pop(genre)
      }
    },
    // 회원 맞춤 장르
    GETRECOMMENDGENRE(state) {
      axios({
        method: 'get',
        url: `${API_URL}/api/accounts/recommend/`,
        headers: {
          Authorization: `Token ${state.token}`
        },
      })
      .then((res) => {
        state.user = res.data
        // console.log(res.data)
      })
      .catch((err) => console.log(err))   
    },
  },
  actions: {
    getUser(context) {
      // console.log('in')
      axios({
        method: 'get',
        url: `${API_URL}/api/accounts/mypage/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then(res=> {
        // console.log('next')
        // console.log(res, context)
        context.commit('GET_USER', res.data)
      })
      .catch(err => {
          // console.log(1)
          console.log(err)
        })
    },
    getCommunity(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/`,
      })
        .then(res=> {
          context.commit('GET_COMMUNITY', res.data)
        })
        .catch(err => console.log(err))
    },
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/`,
      })
        .then(res=> {
          // console.log(res, context)
          context.commit('GET_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    },
    getGenre(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/genre/`,
      })
        .then(res=> {
          const data = _.sampleSize(res.data, 3)
          // console.log(data)
          context.commit('GET_GENRES', data)
        })
        .catch(err => console.log(err))
    },
    getAllGenre(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/genre/`,
      })
        .then(res=> {
          context.commit('GET_ALLGENRES', res.data)
        })
        .catch(err => console.log(err))
    },
    recGenre(context) {
      setTimeout(() => {
        context.commit('REC_GENRE')
      }, 500)
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
          context.commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    
  },
  modules: {
  }
})
