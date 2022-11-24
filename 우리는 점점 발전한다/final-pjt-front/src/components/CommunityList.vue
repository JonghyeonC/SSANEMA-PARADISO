<template>
  <div>
    <CommunityListItem
      v-for="community in communities"
      :key="community.id"
      :community="community"
    />
  </div>
</template>

<script>
import CommunityListItem from '@/components/CommunityListItem'

export default {
  name : 'CommunityList',
  components: {
    CommunityListItem,
  },
  computed: {
    communities() {
      return this.$store.state.communities
    }
  },
  methods: {
    
  }
}
</script>

<style>

</style>