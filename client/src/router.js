// import Vue from 'vue'
// import VueRouter from 'vue-router'
import Home from './pages/Home'
import Register from './pages/Register'
import Country from './pages/Country'
import League from './pages/League'
import Team from './pages/Team'
import User from './pages/User'
import Player from './pages/Player'

import store from './store/index'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/register', component: Register, name: 'Register' },
  { path: '/country/:code', component: Country, name: 'Country' },
  { path: '/league/:league_id', component: League, name: 'League' },
  { path: '/team/:team_id', component: Team, name: 'Team' },
  { path: '/user/:user_id', component: User, name: 'User' },
  { path: '/player/:player_id', component: Player, name: 'Player' }
]

// Vue.use(VueRouter)

// const router = new VueRouter({ routes, mode: 'history' })

// // router.beforeEach((to, from, next) => {
// //   if (
// //     (to.name !== 'Login' || to.name !== 'Register') &&
// //     !store.getters.isAuthenticated
// //   )
// //     next({ name: 'Home' })
// //   else next()
// // })

// export default router


import { createRouter, createWebHistory } from 'vue-router/auto'

const router = createRouter({
  history: createWebHistory()
})

routes.forEach(route => {
  router.addRoute(route)
})

// router.beforeEach((to, from, next) => {
//   console.log(to)
//   console.log(from)
//   console.log(next)


//   const checkLocataion = (to.name !== 'Login' || to.name !== 'Register') && to.name !== 'Home'
//   const checkAuth = store.getters.isAuthenticated
//   console.log(checkLocataion)
//   console.log(checkAuth)
//   if (checkLocataion && !checkAuth) {
//     next({ name: 'Home' })
//   } else next()
// })

export default router