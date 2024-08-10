<template>
      <v-expansion-panels >
        <v-expansion-panel>
          <v-expansion-panel-title color="primary">Fixture Stats</v-expansion-panel-title>
          <v-expansion-panel-text >
            <v-data-table-virtual
              density="compact"
              :headers="fixturesHeaders"
              :items="fixturesData"
              item-value="name"
              class="elevation-1" 
            >
            </v-data-table-virtual>
          </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
  
</template>

<script>
export default {
  name: 'TeamStats',
  props: ['data'],
  data: () => ({
    fixturesData: [],
    fixturesHeaders: [],
  }),
  methods: {
    setData() {
      this.fixturesData = [
        {
        name: 'Played',
        home: parseFloat(this.data.fixtures.played.home),
        away: parseFloat(this.data.fixtures.played.away),
        total: parseFloat(this.data.fixtures.played.total)
        },
        {
        name: 'Wins',
        home: parseFloat(this.data.fixtures.wins.home),
        away: parseFloat(this.data.fixtures.wins.away),
        total: parseFloat(this.data.fixtures.wins.total)
        },
        {
        name: 'Draws',
        home: parseFloat(this.data.fixtures.draws.home),
        away: parseFloat(this.data.fixtures.draws.away),
        total: parseFloat(this.data.fixtures.draws.total)
        },
        {
        name: 'Losses',
        home: parseFloat(this.data.fixtures.loses.home),
        away: parseFloat(this.data.fixtures.loses.away),
        total: parseFloat(this.data.fixtures.loses.total)
        },
      ]
      this.fixturesHeaders = [
        {
          title: 'Fixtures',
          key: 'name',
          align: 'start',
          
        },
        { title: 'Home', key: 'home', align: 'end'},
        { title: 'Away', key: 'away', align: 'end' },
        { title: 'Total', key: 'total', align: 'end' }
      ]
    }
  },
  mounted() {
    this.setData()
  }
}
</script>

<style scoped>
  .v-data-table {
    border: 0px inset #04B88B;
    border-radius: 4px;
  }
  .v-expansion-panel-text {
    background-color: #038564;
  }
</style>