<template>
  <div>
    <div v-if="!community_set?.length">
      <h3>작성한 게시글</h3>
      <div v-if="profile">
        <p class="empty-case">작성한 게시글이 없습니다. 리뷰를 작성하러 가시겠습니까?</p>
        <button type="button" class="btn btn-outline-light "><router-link :to="{ name: 'CommunityView' }" class="go-tinder ">Let's Go</router-link></button>
      </div>
    </div>
    <div class="accordion" id="accordionExample" v-if="community_set?.length">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button class="accordion-button mypage-accordian" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            작성한 게시물
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <ul class="list-group">
              <MyCommunityListItem
                v-for="community in community_set"
                :key="community.id"
                :community="community"
              />
            </ul>
          </div>
        </div>
      </div>
    </div>
    <!-- <h3>내가 쓴 게시물</h3>
    <MyCommunityListItem
      v-for="community in community_set"
      :key="community.id"
      :community="community"
    /> -->
  </div>
</template>

<script>
import MyCommunityListItem from '@/components/MyCommunityListItem'

export default {
  name: 'MyCommunityList',
  components: {
    MyCommunityListItem,
  },
  props: {
    community_set: Array,
    profile: Boolean,
  },
}
</script>

<style>

</style>