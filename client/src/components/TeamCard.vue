<template>
<v-hover>
  <template v-slot:default="{ hover }">
  <v-card
  fluid
    color="#1E1E1E"
    dark
    :elevation="hover ? 24 : 6"
    width="200px"
    class="ma-2 rounded-l"
    
  >
    <div class="d-flex flex-column align-center div-pointer" @click="$emit('selectTeam', team.id)">
      <div>
        <v-card-text
          class="text-h6 text-truncate"
          v-text="team.name"
        ></v-card-text>
      </div>
      <v-avatar
        class="ma-3"
        size="125"
        tile
      >
        <v-img 
          contain 
          :src="`https://media.api-sports.io/football/teams/${team.id}.png`"
        ></v-img>
      </v-avatar>
    </div>
    <div class="d-flex flex-column align-center">
      <v-card-actions>
        <v-row class="ma-2 d-flex  space-between">
          <v-btn 
          color="primary"
          icon
          >
            <v-icon>mdi-information</v-icon>
          </v-btn>

          <v-btn 
            icon
            color="amber"
            v-if="authenticated && user && isFavorite"
            z-indes="10"
            @click="snackbar = true"
            >
            <v-icon>mdi-star-circle</v-icon>
          </v-btn>
          
          <v-btn 
            icon
            color="primary"
            v-else-if="authenticated && user"
            @click="$emit('favoriteTeam', team)"
            z-indes="10"
            >
            <v-icon>mdi-star-circle</v-icon>
          </v-btn>

          <v-btn 
            icon
            color="grey"
            v-else
            disabled
            z-indes="10"
            >
            <v-icon>mdi-star-circle</v-icon>
          </v-btn>

        <v-snackbar v-model="snackbar">
          This team is already in your favorites
            <template v-slot:action="{ attrs }">
              <v-btn
                color="white"
                text
                v-bind="attrs"
                @click="snackbar = false"
              >
                Close
              </v-btn>
            </template>
          </v-snackbar>

        </v-row>
      </v-card-actions>
    </div>
  </v-card>
  </template>
</v-hover>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'TeamCard',
  emits: ["selectTeam", "favoriteTeam"],
  props:['team', 'isFavorite'],
  data: () => ({
    snackbar: false
  }),
  methods: {
    selectTeam(teamId) {
      this.$emit('selectTeam', teamId)
    },
    favoriteTeam(team) {
      this.$emit('favoriteTeam', team)
    }
    },
  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated,
    })
  },
}
</script>

<style scoped>
  .div-pointer {
    cursor: pointer;
  }
  .v-card-title {
    font-size:8vw
  }
</style>