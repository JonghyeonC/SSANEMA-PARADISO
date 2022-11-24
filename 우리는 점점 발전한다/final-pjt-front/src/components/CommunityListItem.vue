<template>
  <div>
    <div class="listWrap">
      <table class="tbList">
        <colgroup>
          <col width="7%"/>
          <col width="*"/>
          <col width="10%"/>
          <col width="15%"/>
        </colgroup>
        <tr>
          <th>no</th>
          <th>제목</th>
          <th>작성자</th>
          <th>날짜</th>
        </tr>
        <tr>
          <td>{{ community.id }}</td>
          <td><router-link
              :to="{
              name : 'CommunityDetail',
              params: { id: community.id }
              }"
              class="title"
              >
              {{ community.title }}
              </router-link>
          </td>
          <router-link :to="{ name: 'MyPageView' }" v-if="community.user.username === this.$store.state.user.username" class="text-name">{{ community.user.username }}</router-link>
          <router-link :to="{ name: 'ProfileView', params:{ username: community.user.username } }" v-if="community.user.username !== this.$store.state.user.username" class="text-name">{{ community.user.username }}</router-link>
          <td>{{ community.created_at.substring(0, 10) }}</td>
        </tr>
      </table>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name : "CommunityListItem",
  props: {
    community: Object,
  }
}
</script>

<style>
.tbList td.txt_left{text-align:left;}
.title{
  text-decoration: none;
  color:blue
}
</style>