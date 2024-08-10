<template>
<v-container>
  <v-container v-if="!authenticated && !user" class="login-container">
    <Login />
  </v-container>
  <v-container v-if="authenticated && user && userFavoriteTeams.length > 0" class="d-flex flex-row flex-wrap justify-space-around container-color rounded-lg" elevation="20">
  <v-container v-if="userFavoriteTeams.length > 0">
    <div class="text-h5 mb-0 text-center">
      Favorites
    </div>
  </v-container>
  <v-container v-if="userFavoriteTeams.length && page" fluid class="d-flex flex-row flex-wrap justify-space-around">
    <UserCard
      v-for="team in userFavoriteTeams"
      :key="team.id"
      :page="page"
      :item="team"
      @selectItem="selectTeam"
    />
  </v-container>
  <v-container v-if="userFavoritePlayers.length && page" fluid class="d-flex flex-row flex-wrap justify-space-around">
    <UserCard
      v-for="player in userFavoritePlayers"
      :key="player.id"
      :page="page"
      :item="player"
      @selectItem="selectPlayer"
    />
  </v-container>
  </v-container>
  <v-container>
    <div class="text-h5 mb-0 text-center">
      Top Leagues
    </div>
    <v-container class="d-flex flex-row flex-wrap justify-space-around">
      <LeagueCard
        v-for="league in leagues"
        :key="league.id"
        :league="league"
        @selectLeague="selectLeague"
      />
    </v-container>
  </v-container>
</v-container>
  
</template>

<script>
import Login from '../components/Login.vue'
import { mapState } from 'vuex'
import LeagueCard from '../components/LeagueCard.vue'
import UserCard from '../components/UserCard.vue'
export default {
  name: 'Home',
  data: () => ({
    leagues: [
      {name: "Premier League", id: "39", location: "England" },
      {name: "La Liga", id: "140", location: "Spain"},
      {name: "Bundesliga 1", id: "78", location: "Germany"},
      {name: "Serie A", id: "135", location: "Italy"},
      {name: "Ligue 1", id: "61", location: "France"},
      {name: "MLS", id: "253", location: "United States"},
      {name: "Championship", id: "40", location: "England" },
      {name: "Segunda Division", id: "141", location: "Spain"},
      {name: "Bundesliga 2", id: "79", location: "Germany"},
      {name: "Serie B", id: "136", location: "Italy"},
      {name: "Ligue 2", id: "62", location: "France"},
    ],
    page: ''
  }),
  components: {
    Login,
    LeagueCard,
    UserCard
  },
  computed: mapState({
    user: state => state.user,
    authenticated: state => state.authenticated,
    userFavoriteTeams: state => state.userFavoriteTeams,
    userFavoritePlayers: state => state.userFavoritePlayers,
  }),
  methods: {
    async selectLeague(leagueId) {
      this.$router.push(`/league/${leagueId}`)
    },
    async selectTeam(teamId) {
      this.$router.push(`/team/${teamId}`)
    },
    async selectPlayer(playerId) {
      this.$router.push(`/player/${playerId}`)
    }
  },
}
</script>

<style scoped>
  .login-container {
    border: white 2px solid;
    border-radius: 10px;
    padding: 1.5em;
  }
  .container-color {
    background-color: #1E1E1E;
    border: 2px solid #04B88B;
  }
  .container .container-color {
    padding: 0;
  }
</style>