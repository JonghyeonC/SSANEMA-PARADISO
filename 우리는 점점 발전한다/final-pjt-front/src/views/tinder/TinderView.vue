<template>
  <div class="tinder-view">
    <TinderMain/>
  </div>
</template>

<script>
import TinderMain from '@/components/tinder/TinderMain'
// import _ from 'lodash'

export default {
  name: 'TinderView',
  components: {
    TinderMain,
  },
  computed: {
    // movies() {
    //   return _.sampleSize(this.$store.state.movies, 20)
    // }
  }
}
</script>

<style>
/* .tinder-body {
  height: 100%;
} */

.tinder-view {
  margin: 0;
  /* background-color: #20262e; */
  overflow: hidden;
}
</style>