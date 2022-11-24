<template>
  <div>
    <li class="list-group-item">
      <router-link class="mypage-router-dec"
        :to="{
          name : 'CommunityDetail',
          params: { id: comment.community}
          }"
      >
      <span >내용: {{ comment.content }}</span><br>
      </router-link>
    </li>
  </div>
  
</template>

<script>
export default {
  name: 'MyCommunityCommentListItem',
  props: {
    comment: Object,
  }
}
</script>

<style>
.mypage-router-dec{
  text-decoration: none;
  color: rgb(79, 77, 77)
}
</style>