<template>
  <div>
    <div v-if="!comments?.length">
      <h3>작성한 영화 리뷰</h3>
      <div v-if="profile">
        <p class="empty-case">작성한 영화 리뷰가 없습니다. 리뷰를 작성하러 가시겠습니까?</p>
        <button type="button" class="btn btn-outline-light "><router-link :to="{ name: 'HomeView' }" class="go-tinder ">Let's Go</router-link></button>
      </div>
    </div>
    <div v-if="comments?.length">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button class="accordion-button mypage-accordian" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
            작성한 영화 리뷰
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
          <div class="accordion-body">
            <ul class="list-group">
              <MyCommentListItem
                v-for="comment in comments"
                :key="comment.id"
                :comment="comment"
              />
            </ul>
          </div>
        </div>
      </div>
    </div>
    <!-- <MyCommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    /> -->
  </div>
</template>

<script>
import MyCommentListItem from '@/components/MyCommentListItem'

export default {
  name: 'MyCommentList',
  components: {
    MyCommentListItem,
  },
  props: {
    comments: Array,
    profile: Boolean,
  },
}
</script>

<style>
.mypage-accordian{
  background-color: rgba(70, 131, 149, 0.5);
  color: black;
}
</style>