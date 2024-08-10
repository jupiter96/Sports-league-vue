<template>
  <v-app>
      <Nav />
      <v-main>
        <v-container fluid>
          <router-view />
        </v-container>
      </v-main>
  </v-app>
</template>

<script>
import Nav from './components/Nav.vue'
import { CheckSession } from './services/Auth'
import {GetUserFavorites} from './services/UserServices'
import { mapActions, mapState, mapGetters } from 'vuex'
export default {
  name: 'App',
  components: {
    Nav
  },
  async mounted() {
    const token = await this.getToken()
    if (token) {
      await this.checkToken(token)
      const favorites = await GetUserFavorites(this.user.id)
      if(favorites.players.length) {
        this.setUserPlayers(favorites.players)
      }
      if(favorites.teams.length) {
        this.setUserTeams(favorites.teams)
      } 
    }
  },
  methods: {
    ...mapActions(['setUser','toggleAuthenticated','setUserTeams','setUserPlayers']),
    async getToken() {
      const token = await localStorage.getItem('token')
      return token
    },
    async checkToken(token) {
      const session = await CheckSession(token)
      this.setUser(session)
      this.toggleAuthenticated(true)
    }
  },
  computed: {
    ...mapState(["user", "authenticated"])
  }
};
</script>

<style scoped>

</style>
