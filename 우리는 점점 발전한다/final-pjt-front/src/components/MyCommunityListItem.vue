<template>
  <div>
    <li class="list-group-item">
      <router-link class="mypage-router-dec"
        :to="{
          name : 'CommunityDetail',
          params: { id: community.pk }
          }"
      >
      <span >제목: {{ community.title }}</span> /
      <span >내용: {{ community.content }}</span><br>
      </router-link>
    </li>
  </div>
  
</template>

<script>
export default {
  name: 'MyCommunityListItem',
  props: {
    community: Object,
  }
}
</script>

<style>
.mypage-router-dec{
  text-decoration: none;
  color: rgb(79, 77, 77)
}
</style>