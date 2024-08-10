<template>
<v-hover>
  <template v-slot:default="{ hover }">
  <v-card
    fluid
      color="#191919"
      dark
      width="150px"
      :elevation="hover ? 24 : 6"
      class="ma-2 pa-1"
  >
    <div class="d-flex flex-column align-center" @click="$emit('selectPlayer', player.player.id)">
      <div>
        <v-card-subtitle
          v-text="player.player.name"
          class="text-truncate"
        ></v-card-subtitle>
      </div>
      <v-avatar
        class="ma-.5"
        size="100"
        tile
      >
        <v-img
          class="rounded-circle"
          contain 
          :src="`https://media.api-sports.io/football/players/${player.player.id}.png`"
          
        ></v-img>
      </v-avatar> 
      <v-row class="ma-2 d-flex  space-between">
        <v-btn 
          color="primary"
          icon
          @click="$emit('selectPlayer', player.player.id)"
        >
          <v-icon>mdi-information</v-icon>
        </v-btn>
        <v-btn 
          icon
          color="amber"
          v-if="authenticated && user && isFavorite"
          @click="snackbar = true"
        >
          <v-icon>mdi-star-circle</v-icon>
        </v-btn>
        <v-btn 
          icon
          color="primary"
          v-else-if="authenticated && user"
          @click="$emit('favoritePlayer', player.player)"
        >
          <v-icon>mdi-star-circle</v-icon>
        </v-btn>
        <v-btn 
          icon
          color="primary"
          v-else
          disabled
        >
          <v-icon>mdi-star-circle</v-icon>
        </v-btn>
        <v-snackbar v-model="snackbar">
          This player is already in your favorites
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
    </div>
  </v-card>
    </template>
</v-hover>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'PlayerCard',
  emits: ["selectPlayer", "favoritePlayer"],
  props: ["player", "teamLogo",'isFavorite'],
  data: () => ({
    snackbar: false
  }),
  methods: {
    selectPlayer(playerId) {
      this.$emit('selectPlayer', playerId)
    },
    favoritePlayer(player) {
      this.$emit('favoritePlayer', player)
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
  .rounded-circle{
    border: 3px solid #04B88B;
  }
  .v-card {
    border: 10px solid #04B88B;
  }
</style>