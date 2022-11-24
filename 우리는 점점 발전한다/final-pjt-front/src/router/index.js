import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import CommunityView from '@/views/CommunityView'
import CommunityCreateView from '@/views/CommunityCreateView'
import CommunityDetailView from '@/views/CommunityDetailView'
import CommunityUpdateView from '@/views/CommunityUpdateView'
import DetailView from '@/views/DetailView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'
import MyPageView from '@/views/MyPageView'
import ProfileView from '@/views/ProfileView'
import SearchView from '@/views/SearchView'
import RecommendView from '@/views/RecommendView'
import TinderView from '@/views/tinder/TinderView'

import ActionView from '@/views/GenreViews/ActionView'
import AdventureView from '@/views/GenreViews/AdventureView'
import AnimationView from '@/views/GenreViews/AnimationView'
import ComedyView from '@/views/GenreViews/ComedyView'
import CriminalView from '@/views/GenreViews/CriminalView'
import DocumentaryView from '@/views/GenreViews/DocumentaryView'
import DramaView from '@/views/GenreViews/DramaView'
import FamilyView from '@/views/GenreViews/FamilyView'
import FantasyView from '@/views/GenreViews/FantasyView'
import HistoryView from '@/views/GenreViews/HistoryView'
import HorrorView from '@/views/GenreViews/HorrorView'
import MusicView from '@/views/GenreViews/MusicView'
import MysteryView from '@/views/GenreViews/MysteryView'
import RomanceView from '@/views/GenreViews/RomanceView'
import SFView from '@/views/GenreViews/SFView'
import ThrillerView from '@/views/GenreViews/ThrillerView'
import TvmovieView from '@/views/GenreViews/TvmovieView'
import WarView from '@/views/GenreViews/WarView'
import WesternView from '@/views/GenreViews/WesternView'

import store from '@/store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    name: 'HomeView',
    component: HomeView
  },

  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  
  {
    path: '/community/create',
    name: 'CommunityCreate',
    component: CommunityCreateView
  },
    
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
    
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },

  {
    path: '/mypage',
    name: 'MyPageView',
    component: MyPageView
  },

  {
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  
  {
    path: '/tinder',
    name: 'TinderView',
    component: TinderView
  },

  {
    path: '/GenreViews/Adventure',
    name: 'AdventureView',
    component: AdventureView
  }, 

  {
    path: '/GenreViews/AnimationView',
    name: 'AnimationView',
    component: AnimationView
  }, 

  {
    path: '/GenreViews/ComedyView',
    name: 'ComedyView',
    component: ComedyView
  }, 

  {
    path: '/GenreViews/CriminalView',
    name: 'CriminalView',
    component: CriminalView
  }, 

  {
    path: '/GenreViews/DocumentaryView',
    name: 'DocumentaryView',
    component: DocumentaryView
  }, 

  {
    path: '/GenreViews/DramaView',
    name: 'DramaView',
    component: DramaView
  }, 

  {
    path: '/GenreViews/FamilyView',
    name: 'FamilyView',
    component: FamilyView
  }, 
  
  {
    path: '/GenreViews/FantasyView',
    name: 'FantasyView',
    component: FantasyView
  }, 

  {
    path: '/GenreViews/HistoryView',
    name: 'HistoryView',
    component: HistoryView
  }, 

  {
    path: '/GenreViews/HorrorView',
    name: 'HorrorView',
    component: HorrorView
  }, 

  {
    path: '/GenreViews/MusicView',
    name: 'MusicView',
    component: MusicView
  }, 
  
  {
    path: '/GenreViews/MysteryView',
    name: 'MysteryView',
    component: MysteryView
  }, 

  {
    path: '/GenreViews/RomanceView',
    name: 'RomanceView',
    component: RomanceView
  }, 

  {
    path: '/GenreViews/SFView',
    name: 'SFView',
    component: SFView
  }, 

  {
    path: '/GenreViews/ThrillerView',
    name: 'ThrillerView',
    component: ThrillerView
  }, 

  {
    path: '/GenreViews/ActionView',
    name: 'ActionView',
    component: ActionView
  }, 

  {
    path: '/GenreViews/TvmovieView',
    name: 'TvmovieView',
    component: TvmovieView
  }, 

  {
    path: '/GenreViews/WarView',
    name: 'WarView',
    component: WarView
  }, 

  {
    path: '/GenreViews/WesternView',
    name: 'WesternView',
    component: WesternView
  }, 

  {
    path: '/profile/:username',
    // path: 'profile',
    name: 'ProfileView',
    props: true,
    component: ProfileView
  },
  
  {
    path: '/movies/:id',
    name: 'DetailView',
    component: DetailView,
  },

  {
    path: '/community/:id/update/',
    name: 'CommunityUpdate',
    component: CommunityUpdateView
  },

  {
    path: '/community/:id',
    name: 'CommunityDetail',
    component: CommunityDetailView
  },

  {
    path: '/search/:content',
    name: 'Search',
    component: SearchView
  },
  

]

const router = new VueRouter({
  mode: 'history',
  scrollBehavior() { 
    return { x: 0, y: 0 } 
  },
  routes
})


router.beforeEach( (to, from, next) => {
  // 로그인 여부
  // const isLoggedIn = store.getters.isLogin
  console.log(store.getters)
  const isLoggedIn = store.getters["isLogin"]
  const authPages = ['MyPageView', 'CommunityView', 'CommunityCreate', 'RecommendView', 'TinderView', 'ProfileView', 'DetailView', 'CommunityUpdate', 'CommunityDetail']
  
  const isAuthRequired = authPages.includes(to.name)
  if (isAuthRequired && !isLoggedIn) {
    // console.log(isLoggedIn)
    alert('로그인이 필요한 페이지입니다!')
    next({ name: 'LogInView'})
  } 
  next()
})


const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => {
		if (err.name !== 'NavigationDuplicated') throw err
	})
}

export default router
