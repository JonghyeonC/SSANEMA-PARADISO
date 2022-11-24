<template>
  <div>
    <div>
      <div class="card float-start recom_card card_image" style="width: 18rem height: 430px;">
        <figure>
          <img v-if="this.movie" :src="imgSRC" @click="goDetail" class="image_card">
          <div class="overlay">
            <div class="description" @click="goDetail">
              {{ movie.title }}
            </div>
          </div>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GenreMovieRecom.vue",
  props: {
    movie: Object,
  },
  computed: {
    imgSRC(){
      return `https://image.tmdb.org/t/p/w400${this.movie?.poster_path}`
    },
  },
  methods: {
    goDetail() {
      this.$router.push({name: 'DetailView', params: { id: this.movie.id }})
    },
  },
}
</script>

<style>
.recom_card {
  width: 290px;
  height: 470px;
  margin: 10px;
}
.card_content {
  padding: 10px;
}
.image_card {
  width: 18rem;
  height: 430px;
}
figure {
  width: 100%;
  position: relative;
}

figure img {
  display: block;
  width: 100%;
  height: auto;
} 
figure h4 {
  position: absolute;
  top: calc(100% - 50px);
  left: 0;
  width: 100%;
  height: 50px;
  color: #fff;
  background: rgba(0, 0, 0, 0.6);
  margin: 0;
} 
figure .overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  overflow: hidden;
  width: 100%;
  height: 0;
  color: #fff;
  background: rgba(0, 0, 0, 0.6);
      -webkit-transition: .6s ease;
      transition: .6s ease;
}
figure .overlay .description {
  font-size: 20px;
  position: absolute;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  text-align: center;
}

figure:hover h4 {
  display: none;
} 
figure:hover .overlay {
  display: block;
  height: 100%;
}
</style>