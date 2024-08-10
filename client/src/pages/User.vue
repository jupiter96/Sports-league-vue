<template>
<v-container>
  <template>
    <v-expansion-panels :popout="true" :hover="true" class="mb-5" >
      <v-expansion-panel >
        <v-expansion-panel-title  expand-icon="mdi-account-edit" disable-icon-rotate >
          Edit User Info
        </v-expansion-panel-title>
        <v-expansion-panel-text >
          <EditUser />
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </template>
  <v-container v-if="userFavoriteTeams.length">
    <div class="text-h5 mb-0 text-center">
      Your Teams
    </div>
  </v-container>
  <v-container v-if="userFavoriteTeams.length" fluid class="d-flex flex-row flex-wrap justify-space-around container-color rounded-lg" elevation="20">
    <UserCard
      v-for="team in userFavoriteTeams"
      :key="team.id"
      :page="page"
      :item="team"
      @selectItem="selectTeam"
      @removeItem="removeTeam"
    />
  </v-container>
    <v-container v-if="userFavoritePlayers.length">
    <div class="text-h5 mb-0 text-center">
      Your Players
    </div>
  </v-container>
  <v-container v-if="userFavoritePlayers.length" fluid class="d-flex flex-row flex-wrap justify-space-around container-color rounded-lg" elevation="20">
    <UserCard
      v-for="player in userFavoritePlayers"
      :key="player.id"
      :page="page"
      :item="player"
      @selectItem="selectPlayer"
      @removeItem="removePlayer"
    />
  </v-container>
</v-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import EditUser from '../components/EditUser.vue'
import UserCard from '../components/UserCard.vue'
import { RemovePlayerFromUser } from '../services/PlayerServices'
import { RemoveTeamFromUser } from '../services/TeamServices'

export default {
  name: 'User',
  data: () => ({
    extend: false,
    page: ''
  }),
  components: {
    EditUser,
    UserCard
  },
  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated,
      userFavoriteTeams: state => state.userFavoriteTeams,
      userFavoritePlayers: state => state.userFavoritePlayers,
    })
  },
  methods: {
    ...mapActions(['removeTeamFromUserFavorites','removePlayerFromUserFavorites']),
    selectTeam(teamId) {
      this.$router.push(`/team/${teamId}`)
    },
    selectPlayer(playerId) {
      this.$router.push(`/player/${playerId}`)
    },
    async removeTeam(team) {
      const data = {
        user_id: this.user.id,
        team_id: team.id
      }
      const res = await RemoveTeamFromUser(data)
      this.removeTeamFromUserFavorites(res.team_id)
    },
    async  removePlayer(player) {
      const data = {
        user_id: this.user.id,
        player_id: player.id
      }
      const res = await RemovePlayerFromUser(data)
      this.removePlayerFromUserFavorites(res.player_id)
    }
  },
  mounted() {
    this.page=this.$router.history.current.name
  }

}
</script>

<style scoped>
  .container-color {
    background-color: #1E1E1E;
    border: 2px solid #04B88B;
  }
  .container .container-color {
    padding: none;
  }
</style>