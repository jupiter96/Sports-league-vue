<template>
  <v-container v-if="data" fluid >
      <v-row class="d-flex justify-center align-center" elevation="10">
          <v-card
            color="primary"
            dark
            width="80%"
            min-width="450"
          >
            <div 
              class="d-flex flex-no-wrap justify-space-between align-center mx-5"
              >
              <div>
                <v-card-title
                  class="text-h5 text-truncate"
                  v-text="data.team.name"
                ></v-card-title>
                <v-card-subtitle v-text="data.league.name"></v-card-subtitle>
              </div>
              <v-spacer></v-spacer>
              <v-avatar
                class="ma-3"
                size="100"
                tile
              >
                <v-img 
                contain 
                :src="data.team.logo"
                elevation="10"
                ></v-img>
              </v-avatar>
            </div>
          </v-card>
      </v-row>
      <v-row class="d-flex justify-center align-center mb-10" elevation="5" >
        <v-card
          color="#eee"
          fluid
          width="80%"
          min-width="450">
        <v-container v-if="data" fluid >
          <v-row class="d-flex justify-center align-center py-10" >
            <Form 
              :form="data.form"
            />
          </v-row>
          <v-row class="d-flex justify-center align-center " >
            <GoalsChart
              v-if="loadCharts"
              :goalData="goalRadarData"
            />
          </v-row>
          <v-row class="d-flex justify-center align-center " >
            <TeamStats v-if="data" :data="data" />
          </v-row>
        </v-container>
      </v-card>
      </v-row>
      <v-container v-if="players && favorites" fluid class="d-flex flex-row flex-wrap justify-space-around">
        <PlayerCard
          v-for="player in players"
          :key="player.player.id"
          :player="player"
          :isFavorite="favorites.includes(player.player.id)"
          :teamLogo="data.team.logo"
          @selectPlayer="selectPlayer"
          @favoritePlayer="favoritePlayer"
        />
      </v-container>
  </v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import { mapCacheActions } from 'vuex-cache';
import { AddPlayerToUser } from '../services/PlayerServices'
import PlayerCard from '../components/PlayerCard.vue'
import Form from '../components/Form.vue'
import GoalsChart from '../charts/GoalsChart.vue'
import TeamStats from '../components/TeamStats.vue'

export default {
  name: 'Team',
  data: () => ({
    favorites: null,
    players: null,
    data: null,
    goalRadarData: {
      labels: [],
      goalDataTeam: [],
      goalDataOpp: [],
    },
    tableData: {
      tableItems: [],
      tableHeaders: [],
    },
    loadCharts: false
  }),
  components: {
    PlayerCard,
    Form,
    GoalsChart,
    TeamStats
  },
  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated,
      userFavoritePlayers: state => state.userFavoritePlayers,
    })
  },
  methods: {
    ...mapActions(['addPlayerToUserFavorites']),
    ...mapCacheActions(['FETCH_QUERY_BY_TEAM_ID']),
    async getTeamPlayersAndStats(teamId) {
      let results = await this.FETCH_QUERY_BY_TEAM_ID(teamId)
      this.players = results.players
      this.data = results.data.data.response
      this.setGoalsChartData()
      this.favorites = await this.checkFavorites()
    },
    setGoalsChartData() {
      let formattedLabels = Object.keys(this.data.goals.for.minute)
      this.goalRadarData.labels = formattedLabels.map(label => label +=" Minutes")
      for (const time in this.data.goals.for.minute) {
        const total = this.data.goals.for.minute[time].total
        if (!total) {
          this.goalRadarData.goalDataOpp.push(0)
        } else {
          this.goalRadarData.goalDataTeam.push(total)
        }
      }
      for (const time in this.data.goals.against.minute) {
        const total = this.data.goals.against.minute[time].total
        if (!total) {
          this.goalRadarData.goalDataOpp.push(0)
        } else {
          this.goalRadarData.goalDataOpp.push(total)
        }
      }
      this.loadCharts = true
    },

    selectPlayer(playerId) {
      this.$router.push(`/player/${playerId}`)
    },
    async favoritePlayer(player) {
      const data = {
        "name": player.name,
        "image": `https://media.api-sports.io/football/players/${player.id}.png`,
        "api_id": player.id,
        "user_id": this.user.id
      }
      const res = await AddPlayerToUser(data)
      this.addPlayerToUserFavorites(res.data.payload)
      this.favorites.push[res.data.payload]
    },
    favArray(){
      let newArray = []
      if (this.userFavoritePlayers.length > 0 && this.players) {
        this.userFavoritePlayers.forEach(obj => {
          this.players.forEach(obj2 =>{
            if(parseFloat(obj.api_id) === obj2.player.id) {
              newArray.push(obj2.player.id)
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
    userFavoritePlayers: async function () {
      this.favorites = await this.checkFavorites()
    }
  },
  async mounted() {
    this.getTeamPlayersAndStats(this.$route.params.team_id)
  }

}
</script>

<style scoped>
  .team {
    height: 100px;
  }
</style>