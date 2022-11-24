<template>
  <div id="app">
    <div class="d-flex flex-row-reverse text-end">
      <button @click="changColor" class="btn btn-secondary fixed1">깔라</button>
    </div>
    <div class="navcontainer">
      <nav>
        <TopBar
          :old_color="old_color"
        />
      </nav>
    </div>
    <div class="allmargin">
      <router-view :class="{'oldColor': old_color}"></router-view>
    </div>
  </div>
</template>

<script>
import TopBar from '@/components/TopBar'

export default {
  name: 'App',
  data() {
    return {
      old_color: true
    }
  },
  components: {
    TopBar,
  },
  methods: {
    LogOut() {
      this.$store.commit('LOGOUT')
    },
    changColor() {
      this.old_color = !this.old_color
    }
  }
}
</script>


<style>
@font-face {
  font-family: 'EF_Rebecca';
  src: url(@/fonts/EF_Rebecca.ttf);
}
#all {
  font-family: EF_Rebecca;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: black;
  /* background-color: red; */
  background-image: url(@/image/old.png);
  background-position: center;
  background-attachment: fixed;
}

.fixed1{
  position: fixed;
}

.fixed2{
  position: fixed;
  width: 190vh;
}

.oldColor :not(.tinder-body){
  filter: grayscale(1);
}

.allmargin {
  margin-top: 175px;
}
/* nav {
  display: flex;
  justify-content: center;
  padding: 30px;
  width: 200px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
} */

nav a.router-link-exact-active {
  color: #42b983;
}
</style>