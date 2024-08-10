<template>
  <v-container v-if="data" fluid >
    <v-row class="d-flex justify-center align-center" elevation="10">
        <v-card
            color="primary"
            dark
            width="80%"
            min-width="450"
        > 
            <v-row class="d-flex" justify="center" align="center">
                <v-card
                    variant="flat"
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
                        v-text="data.player.name"
                        ></v-card-title>
                        <v-card-subtitle v-text="data.statistics[0].team.name"></v-card-subtitle>
                    </div>
                    <v-spacer></v-spacer>
                    <v-avatar
                        class="ma-3"
                        size="100"
                        tile
                    >
                        <v-img
                        class="rounded-circle" 
                        contain 
                        :src="data.player.photo"
                        elevation="10"
                        ></v-img>
                    </v-avatar>
                    </div>
                </v-card>
            </v-row>
            <v-row class="d-flex chart-container" justify="center" align="center">
                <v-card
                    variant="elevated"
                    elevation="1"
                    color="#eeeeee"
                    dark
                    width="100%"
                    min-width="450"
                >
                    <v-container v-if="data" fluid >
                        <v-row class="d-flex justify-center align-center chart" >
                            <PlayerChart
                                v-if="loadCharts"
                                :radarData="goalRadarData"
                            />
                        </v-row>
                        <v-row class="d-flex justify-center align-center" >
                            <PlayerData :player="data.player"/>
                        </v-row>
                    </v-container>
                </v-card>
            </v-row>
      </v-card>
    </v-row>
  </v-container>

</template>

<script>
import { mapState, mapActions } from 'vuex'
import { mapCacheActions } from 'vuex-cache';
import { AddPlayerToUser } from '../services/PlayerServices'
import PlayerData from '../components/PlayerData.vue'
import PlayerChart from '../charts/PlayerChart.vue'

export default {
  name: 'Player',
  data: () => ({
    isFavorite: false,
    data: null,
    goalData: {},
    goalRadarData: {
        labelSet1: "", 
        labelSet2: "",
        dataSet1: [],
        dataSet2: [],
        dataMax: 0,
        labels: []
    },
    tableData: {
      tableItems: [],
      tableHeaders: [],
    },
    loadCharts: false
  }),
    components: {
      PlayerData,
      PlayerChart,
      // PlayerStats
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
    ...mapCacheActions(['FETCH_QUERY_BY_PLAYER_ID']),

    round5(number) {
        return Math.ceil(number / 5) * 5;
    },

    array5(length) {
        Array.from({length:length}, (_, i) => (i + 1) * 5);
    },
 
    buildGoalData(data) {
        const goals = data.goals.total || 0
        const assists = data.goals.assists || 0
        const conceded = data.goals.conceded || 0
        const saved = data.goals.saves || 0

        return {
            position: data.games.position,
            league: {
                id: data.league.id,
                logo: data.league.logo,
                name: data.league.name,
                teamId: data.team.id,
                teamLogo: data.team.logo,
                teamName: data.team.name
            },
            goalStats: {
                goals: goals,
                assists: assists
            },
            saveStats: {
                conceded: conceded,
                saved: saved
            }
        }
    },

    async getPlayerStats(teamId) {
      let results = await this.FETCH_QUERY_BY_PLAYER_ID(teamId)
      this.data = results
      this.setGoalsChartData()
      this.isFavorite = await this.checkFavorites()
    },
    
    setGoalsChartData() {
        this.data.statistics.forEach((obj) => {
            if(!obj.league.id || obj.league.name.includes("Friendlies")) {
                return
            }
            console.log(obj.league)
            const leagueId = obj.league.id.toString()
            this.goalData[leagueId] = this.buildGoalData(obj)

            if(obj.games.position == "Goalkeeper") {
                this.goalRadarData.labelSet1 = "Conceded", 
                this.goalRadarData.labelSet2 = "Saved",
                this.goalRadarData.dataSet1.push(obj.goals.conceded || 0),
                this.goalRadarData.dataSet2.push(obj.goals.saved || 0),
                this.goalRadarData.labels.push(`${obj.league.name} (${obj.team.name})`)
            } else {
                console.log(obj.goals.total)
                this.goalRadarData.labelSet1 = "Goals", 
                this.goalRadarData.labelSet2 = "Assists",
                this.goalRadarData.dataSet1.push(obj.goals.total || 0),
                this.goalRadarData.dataSet2.push(obj.goals.assists || 0),
                this.goalRadarData.labels.push(`${obj.league.name} (${obj.team.name})`)
            }
        })

        this.goalRadarData.dataSet1 = this.goalRadarData.dataSet1.slice(0,4)
        this.goalRadarData.dataSet2 = this.goalRadarData.dataSet2.slice(0,4)
        this.goalRadarData.labels = this.goalRadarData.labels.slice(0,4)
        this.loadCharts = true
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
    checkFavorites() {
      if (this.userFavoritePlayers.length > 0) {
        for (let i = 0; i < this.userFavoritePlayers.length; i++) {
          if(parseFloat(this.userFavoritePlayers[i].api_id) === this.data.player.id) {
            return true
          }
        }
        }
      return false
    }
  },
  watch: {
    userFavoritePlayers: async function () {
      this.isFavorite = await this.checkFavorites()
    }
  },
  async mounted() {
    this.getPlayerStats(this.$route.params.player_id)
  }
}

</script>

<style scoped>
  .rounded-circle{
    border: 3px solid rgb(80, 80, 80);
  }

  .chart-container {
    padding: 12px 12px;
  }

  .chart {
    padding: 0 0 10px 0;
  }
</style>CC