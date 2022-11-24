<template>
  <div>
    <div v-for="(errors, field) in authError" :key="field">
      <p>{{ field }}</p>
        <p v-for="(error, idx) in errors" :key="idx">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name : 'AccountErrorList',
  computed : {
    ...mapGetters(['authError'])
  }
}
</script>

<style>

</style>
