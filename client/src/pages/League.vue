<template>
  <v-container v-if="teams && favorites" fluid class="d-flex flex-row flex-wrap justify-space-around">
    <TeamCard
      v-for="team in teams"
      :key="team.team.id"
      :team="team.team"
      :isFavorite="favorites.includes(team.team.id)"
      @selectTeam="selectTeam"
      @favoriteTeam="favoriteTeam"
    />
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { mapCacheActions, cacheAction } from 'vuex-cache';
import {AddTeamToUser} from '../services/TeamServices'
import TeamCard from '../components/TeamCard.vue'

export default {
  name: 'League',
  data: () => ({
    teams: null,
    favorites: null
  }),
  components: {
    TeamCard
  },
  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated,
      userFavoriteTeams: state => state.userFavoriteTeams,
    }),
  },
  methods: {
    ...mapActions(['addTeamToUserFavorites']),
    // ...mapCacheActions(['FETCH_QUERY_BY_LEAGUE_ID']),
    async getLeagueTeams(leagueId) {
      console.log(this.$store.cache)
      // let results = await this.FETCH_QUERY_BY_LEAGUE_ID(leagueId)

      let results = await this.$store.cache.dispatch('FETCH_QUERY_BY_LEAGUE_ID', leagueId)

      /// Check that Cache works
      /// https://dashboard.api-football.com/
      /// https://github.com/superwf/vuex-cache
      /// https://vuex.vuejs.org/guide/plugins.html#committing-mutations-inside-plugins

      console.log(results)
      this.teams = results
      this.favorites = await this.checkFavorites()
    },
    selectTeam(teamId) {
      this.$router.push(`/team/${teamId}`)
    },
    async favoriteTeam(team) {
      const data = {
        "name": team.name,
        "image": `https://media.api-sports.io/football/teams/${team.id}.png`,
        "api_id": team.id,
        "user_id": this.user.id
      }
      const res = await AddTeamToUser(data)
      this.addTeamToUserFavorites(res.data.payload)
    },

    favArray(){
      let newArray = []
      if (this.userFavoriteTeams.length > 0 && this.teams) {
        this.userFavoriteTeams.forEach(obj => {
          this.teams.forEach(obj2 =>{
            if(parseFloat(obj.api_id) === obj2.team.id) {
              newArray.push(obj2.team.id)
            }
          })
        })
      }
      return newArray
    },
    async checkFavorites() {
      const newArray = await this.favArray()
      return newArray
    }
  },
  watch: {
    userFavoriteTeams: async function () {
      this.favorites = await this.checkFavorites()
    }
  },
  async mounted() {
    await this.getLeagueTeams(this.$route.params.league_id)
  }

}
</script>