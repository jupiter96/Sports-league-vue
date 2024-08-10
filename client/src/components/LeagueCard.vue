<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <v-card
        color="primary"
        dark
        width="425"
        :elevation="hover ? 24 : 6"
        class="ma-2 pa-1"
        @click="$emit('selectLeague', league.id)"
      >
        <div 
          class="d-flex flex-no-wrap justify-space-between"
          
          >
          <div class="d-flex flex-column">
            <v-card-title
              v-text="league.name"
            ></v-card-title>
            <v-card-subtitle v-text="league.location"></v-card-subtitle>
          </div>
          <v-avatar
            class="ma-3"
            size="125"
            tile
          >
            <v-img 
            contain 
            :src="`https://media.api-sports.io/football/leagues/${league.id}.png`"
            elevation="10"
            @click="$emit('selectLeague', league.id)"
            ></v-img>
          </v-avatar>
        </div>
      </v-card>
    </template>
  </v-hover>
</template>

<script>
export default {
  name: 'Home',
  emits: ["selectLeague"],
  props: {
    league: {}
  },
  methods: {
    selectLeague(leagueId) {
      this.$emit('selectLeague', leagueId)
    }
}
}
</script>

<style scoped>
  .v-avatar:hover {
    cursor: pointer;
  }
</style>