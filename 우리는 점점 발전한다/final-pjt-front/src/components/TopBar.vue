<template>
  <nav class="mb-5">
    <div class="fixed2 d-flex justify-content-between">
      <div>
        <router-link :to="{ name: 'HomeView' }" :class="{'oldColor': old_color}" class="nav-link active" aria-current="page"><img src="@/image/싸네마천국(배경제거).png" height="100" width="300"></router-link>
      </div>
      <div>
        <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar">
          <i class="bi bi-card-list bi-size align-middle"></i>
        </button>
      </div>
    </div>
    <div class="container">
      <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar" aria-labelledby="offcanvasDarkNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel">SSANEMA</h5>
        </div>
        <div class="offcanvas-body" :height="1000">
          <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
            <li class="nav-item" data-bs-dismiss="offcanvas">
            <router-link :to="{ name: 'HomeView' }" class="nav-link active" aria-current="page"><div>HomeView</div></router-link>
            </li>
            <li class="nav-item" data-bs-dismiss="offcanvas">
              <router-link :to="{ name : 'CommunityView' }" class="nav-link active" aria-current="page"><div>Community</div></router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Genre
              </a>
              <ul class="dropdown-menu dropdown-menu-dark" data-bs-dismiss="offcanvas">
                <li>
                  <router-link :to="{ name: 'ActionView' }" class="dropdown-item"><div>액션</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'AnimationView' }" class="dropdown-item"><div>애니메이션</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'AdventureView' }" class="dropdown-item"><div>모험</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'ComedyView' }" class="dropdown-item"><div>코미디</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'CriminalView' }" class="dropdown-item"><div>범죄</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'DocumentaryView' }" class="dropdown-item"><div>다큐멘터리</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'DramaView' }" class="dropdown-item"><div>드라마</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'FamilyView' }" class="dropdown-item"><div>가족</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'FantasyView' }" class="dropdown-item"><div>판타지</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'HistoryView' }" class="dropdown-item"><div>역사</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'HorrorView' }" class="dropdown-item"><div>공포</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'MusicView' }" class="dropdown-item"><div>음악</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'MysteryView' }" class="dropdown-item"><div>미스터리</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'RomanceView' }" class="dropdown-item"><div>로맨스</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'SFView' }" class="dropdown-item"><div>SF</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'ThrillerView' }" class="dropdown-item"><div>스릴러</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'TvmovieView' }" class="dropdown-item"><div>TV영화</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'WarView' }" class="dropdown-item"><div>전쟁</div></router-link>
                </li>
                <li>
                  <router-link :to="{ name: 'WesternView' }" class="dropdown-item"><div>서부</div></router-link>
                </li>
              </ul>
            </li>
            <li data-bs-dismiss="offcanvas">
              <router-link :to="{ name: 'TinderView' }" class="nav-link active" aria-current="page"><div>TinderView</div></router-link>
            </li>
            <li data-bs-dismiss="offcanvas">
              <router-link :to="{ name: 'RecommendView' }" class="nav-link active" aria-current="page"><div>RecommendView</div></router-link>
            </li>
            <li data-bs-dismiss="offcanvas">
              <router-link :to="{ name: 'SignUpView' }" class="nav-link active" aria-current="page"><div>SignUpPage</div></router-link>
            </li>
            <li data-bs-dismiss="offcanvas">
              <router-link :to="{ name: 'MyPageView'}" v-if="this.$store.state.login === true" class="nav-link active" aria-current="page"><div>MyPageView</div></router-link>  
            </li>
            <li v-if="this.$store.state.login === false" data-bs-dismiss="offcanvas">
              <!-- <span v-if="this.$store.state.login === true">|</span> -->
              <router-link :to="{ name: 'LogInView' }" class="nav-link active" aria-current="page"><div>LogInPage</div></router-link>
            </li>
            <li data-bs-dismiss="offcanvas">
              <a @click="LogOut" v-if="this.$store.state.login === true"><div>Logout</div></a>
            </li>
            <li class="mt-3">
              <form @submit.prevent="getSearch">
                <input placeholder="Search" v-model="searchObj">
                <button data-bs-dismiss="offcanvas" type="submit">Search</button>
              </form>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'TopBar',
  props: {
    old_color: Object
  },
  methods: {
    LogOut() {
      this.$store.commit('LOGOUT')
    },
    getSearch() {
      if (this.searchObj !== '') {
        this.$router.push({name: 'Search', params: { content: this.searchObj }})
        this.$router.go()
        this.searchObj = ''
      }
    }
  },
  data() {
    return {
      searchObj: null,
    }
  },
}
</script>

<style>
.bi-size {
  font-size: 70px;
}
</style>