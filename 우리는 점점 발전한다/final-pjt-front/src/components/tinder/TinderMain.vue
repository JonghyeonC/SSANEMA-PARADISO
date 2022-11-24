<template>
  <div id="tinder-app" class="tinder-body">
    <div class="container d-flex justify-content-between mt-5 p-5">
      <img src="@/image/bad.png" height="300" width="300">
      <img src="@/image/good.png" height="300" width="300">
    </div>
    <Tinder
      ref="tinder"
      key-name="title"
      :queue.sync="queue"
      :offset-y="10"
      :super-threshold="0.3"
      @submit="onSubmit"
    >
      <template slot-scope="scope">
        <div
          class="pic"
          :style="{ 'background-image': `url(https://image.tmdb.org/t/p/w400${scope.data.item.poster_path})` }"
        >
          <span class="info" @click="openDetail(scope.data.item)">
            <span class="title"
              >{{ scope.data.item.title }}
              <span class="year">{{ scope.data.item.release_date }}</span></span
            >
            <span class="rating">★{{ scope.data.item.vote_average }}</span>
            <span class="categories">
              <span v-for="(item, key) in scope.data.item.categories" :key="key"
                >{{ item
                }}{{
                  key !== scope.data.item.categories.length - 1 ? ", " : ""
                }}
              </span>
            </span>
          </span>
        </div>
      </template>
      <img class="like-pointer" slot="like" src="@/image/좋아요.png">
      <img class="nope-pointer" slot="nope" src="@/image/싫어요.png">
      <img class="super-pointer" slot="super" src="@/image/좋아요.png">
    </Tinder>
    <div class="btns">
      <img src="./assets/nope.png" @click="decide('nope')" />
      <img src="./assets/like.png" @click="decide('like')" />
    </div>
    <div class="modal-info"  v-if="modalShow">
      <div class="modal-content">
        <span class="close" @click="closeModal">×</span>
        <p class="item">{{ item.title }}</p>
        <div class="d-flex p-3">
          <img :src="`https://image.tmdb.org/t/p/w400${this.item.poster_path}`" :width="200" alt="">
          <p class="ms-4">{{ item.overview }}.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import Tinder from "vue-tinder";
// import source from "@/components/tinder/movies";
const API_URL = "http://127.0.0.1:8000"
import axios from 'axios'

export default {
  name: "TinderMain",
  components: { Tinder },
  data: () => ({
    queue: [],
    offset: 0,
    history: [],
    modalShow: false,
    item: {},
    choice_movie: null,
  }),
  computed: {
    source() {
      return _.sampleSize(this.$store.state.movies, 20)
    }
  },
  created() {
    this.mock();
  },
  methods: {
    mock(count = 5, append = true) {
      const list = [];
      for (let i = 0; i < count; i++) {
        list.push({
          title: this.source[this.offset].title,
          item: this.source[this.offset],
        });
        this.offset++;
      }
      if (append) {
        this.queue = this.queue.concat(list);
      } else {
        this.queue.unshift(...list);
      }
    },
    scopeData(){
      return 
    },
    onSubmit({ type, item }) {
      if (this.queue.length < 3) {
        this.mock();
      }
      this.history.push(item);
      if (type === 'none') {
        this.decide('nope')
      } else {
        this.decide('like')
      }
    },
    async decide(choice) {
      if (choice === "rewind") {
        if (this.history.length) {
          this.$refs.tinder.rewind([this.history.pop()]);
        }
      } else if (choice === "help") {
        window.open("https://shanlh.github.io/vue-tinder");
      } else if (choice === "like") {
        this.$refs.tinder.decide(choice);
        // console.log(this.history)
        this.likeMovie()
      } else if (choice === "nope") {
        this.$refs.tinder.decide(choice);
        this.dislikeMovie()
      } else {
        this.$refs.tinder.decide(choice);
      }
    },
    openDetail(item) {
      this.item = item;
      this.modalShow = true;
    },
    closeModal() {
      this.modalShow = false;
    },
    
    dislikeMovie() {
      const history = this.history
      axios({
        method: 'post',
        url: `${API_URL}/api/accounts/tinder_dislike_movies/${history[history.length -1].item.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(res=> {
          this.$store.state.user = res.data
        })
        .catch(err => console.log(err))
    },
    likeMovie() {
      const history = this.history
      axios({
        method: 'post',
        url: `${API_URL}/api/accounts/tinder_like_movies/${history[history.length -1].item.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(res=> {
          this.$store.state.user = res.data
        })
        .catch(err => console.log(err))
    },
  },
};
</script>

<style>
html,
.tinder-body {
  height: 100%;
}

.tinder-body {
  margin: 0;
  overflow: hidden;
}

#tinder-app .vue-tinder {
  position: absolute;
  z-index: 1;
  left: 0;
  right: 0;
  top: 200px;
  margin: auto;
  width: calc(100% - 20px);
  height: calc(100% - 280px);
  min-width: 300px;
  max-width: 400px;
}

.nope-pointer,
.like-pointer {
  position: absolute;
  z-index: 1;
  top: 200px;
  width: 64px;
  height: 64px;
}

.nope-pointer {
  right: 10px;
}

.like-pointer {
  left: 10px;
}

.super-pointer {
  position: absolute;
  z-index: 1;
  bottom: 80px;
  left: 0;
  right: 0;
  margin: auto;
  width: 64px;
  height: 64px;
}

.pic {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.btns {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 20px;
  margin: auto;
  height: 65px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 300px;
  max-width: 355px;
}

.btns img {
  margin-right: 12px;
  box-shadow: 0 4px 9px rgba(0, 0, 0, 0.15);
  border-radius: 50%;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.btns img:nth-child(2n + 1) {
  width: 53px;
}

.btns img:nth-child(2n) {
  width: 65px;
}

.btns img:nth-last-child(1) {
  margin-right: 0;
}

.tinder-card {
  max-height: 530px;
}
/* Item Informations */
.info {
  cursor: pointer;
  position: absolute;
  bottom: 0;
  left: 0;
  padding: 10px;
  width: 100%;
  font-family: sans-serif;
  font-size: 18px;
  /* color: #fff; */
  color: white;
  text-shadow: 0 0 1px #000;
  /* -webkit-text-stroke: 1px black;*/
  background: rgb(0, 0, 0);
  background: linear-gradient(
    0deg,
    rgba(0, 0, 0, 0.9) 0%,
    rgba(0, 0, 0, 0.7) 50%,
    rgba(255, 255, 255, 0) 100%
  );
}
.title {
  text-transform: uppercase;
  color: white;
  font-size: 24px;
  width: 100%;
  display: block;
}
.year {
  font-size: 15px;
}
.rating {
  margin-right: 5px;
  display: inline-block;
}
.time {
  display: inline-block;
}
.categories {
  font-size: 16px;
  margin-top: 10px;
  display: block;
  width: 100%;
}
.categories span {
  margin: 0;
  padding: 0;
}
/* Modal Info */
.modal-info {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  z-index: 9;
}
.modal-info .modal-content {
  position: fixed;
  top: 20%;
  left: 30%;
  width: 40%;
  height: 50%;
  background: #fff;
  border-radius: 5px;
  padding: 15px;
}
.modal-info .modal-content .item {
  color: #000;
}
.modal-info .modal-content .close {
  color: #000;
  position: absolute;
  right: 10px;
  top: 5px;
  cursor: pointer;
  font-size: 50px;
}

.goodicon {
  background-image: url(@/image/good.png);
}
</style>