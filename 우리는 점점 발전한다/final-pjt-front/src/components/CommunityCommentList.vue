<template>
  <div>
    <p class="ms-3">댓글 {{ comments.length}}개</p>
    <hr>
    <CommunityCommentListItem 
    v-for="(comment, idx) in comments"
    :key="`comment-${idx}`"
    :comment=comment
    />
  </div>
</template>

<script>
import CommunityCommentListItem from '@/components/CommunityCommentListItem'


export default {
  name: 'CommunityCommentList',
  components: {
    CommunityCommentListItem,
  },
  computed: {
    comments() {
      return this.$store.state.community_comment
    }
  },
  methods: {
  },
}
</script>

<style>

</style>