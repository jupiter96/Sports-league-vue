<template>
  <v-container fluid class="d-flex flex-row flex-wrap">
      <LeagueCard
        v-for="league in leagues"
        :key="league.id"
        :league="league"
        @selectLeague="selectLeague"
      />
  </v-container>
</template>

<script>
import { GetLeaguesByCountryCode } from '../services/FootballApiServices'
import { mapState, mapGetters, mapActions } from 'vuex'
import LeagueCard from '../components/LeagueCard.vue'
export default {
  name: 'Home',
  data: () => ({
    leagues: null
  }),
  components: {
    LeagueCard
  },
  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated
    }),
    ...mapGetters([
      'getFootballQueriesByCountry'
    ])

  },
  methods: {
    ...mapActions(['addQuery']),
    async getCountryLeagues(code) {
      const query = this.getFootballQueriesByCountry(code)
      if (query) {
        console.log(query, "hmmm")
        this.leagues = query.response  //.slice(0,10)
      } else {
        const leagues = await GetLeaguesByCountryCode(code)
        this.leagues = leagues.response  //.slice(0,10)
        this.addQuery(leagues)
      }
    },
    async selectLeague(leagueId) {
      this.$router.push(`/league/${leagueId}`)
    }
  },
  mounted() {
    this.getCountryLeagues(this.$route.params.code)
  }
}
</script>