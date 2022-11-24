<template>
  <div>
    <li class="list-group-item">
      <router-link class="mypage-router-dec"
        :to="{
          name : 'DetailView',
          params: { id: comment.movie }
          }"
      >
      
      <span class="mypage-router-dec">{{ comment.content }}</span><br>
      </router-link>
    </li>
  </div>
  
</template>

<script>
export default {
  name: 'MyCommentListItem',
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