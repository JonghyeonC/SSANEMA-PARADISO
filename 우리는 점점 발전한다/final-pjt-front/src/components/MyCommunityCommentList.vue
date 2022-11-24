<template>
  <div>
    <div v-if="!community_comment?.length">
      <h3>작성한 댓글</h3>
      <div v-if="profile">
        <p class="empty-case">작성한 댓글이 없습니다. 커뮤니티 게시판으로 이동할까요?</p>
        <button type="button" class="btn btn-outline-light "><router-link :to="{ name: 'CommunityView' }" class="go-tinder">Let's Go</router-link></button>
      </div>
    </div>
    <div class="accordion" id="accordionExample" v-if="community_comment?.length">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingThree">
          <button class="accordion-button mypage-accordian" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
            작성한 댓글
          </button>
        </h2>
        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <ul class="list-group">
              <MyCommunityCommentListItem
                v-for="comment in community_comment"
                :key="comment.id"
                :comment="comment"
              />
            </ul>
          </div>
        </div>
      </div>
    </div>
    <!-- <MyCommunityCommentListItem
      v-for="comment in community_comment"
      :key="comment.id"
      :comment="comment"
    /> -->
  </div>
</template>

<script>
import MyCommunityCommentListItem from '@/components/MyCommunityCommentListItem'

export default {
  name: 'MyCommunityList',
  components: {
    MyCommunityCommentListItem,
  },
  props: {
    community_comment: Array,
    profile: Boolean,
  },

}
</script>

<style>

</style>