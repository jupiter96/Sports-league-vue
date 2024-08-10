<template>
  <v-expansion-panels >
    <v-expansion-panel>
      <v-expansion-panel-title color="primary">Player Info</v-expansion-panel-title>
      <v-expansion-panel-text >
        <v-table 
          density="compact"
          color="primary"
          dark
          width="80%"
          min-width="450"
        >
          <tbody>
            <tr>
              <td>Full Name:</td>
              <td>{{ `${player.firstname} ${player.lastname}` }}</td>
            </tr>
            <tr>
              <td>Age:</td>
              <td>{{ player.age }}</td>
            </tr>
            <tr>
              <td>Height:</td>
              <td>{{ player.height }}</td>
            </tr>
            <tr>
              <td>Weight:</td>
              <td>{{ player.weight }}</td>
            </tr>
            <tr>
              <td>Birth Date:</td>
              <td>{{ player.birth.date }}</td>
            </tr>
            <tr>
              <td>Place of Birth:</td>
              <td>{{ `${player.birth.place}, ${player.birth.country}` }}</td>
            </tr>
            <tr>
              <td>Nationality:</td>
              <td>{{ player.nationality }}</td>
            </tr>
          </tbody>
        </v-table>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>  
</template>

<script>
export default {
  name: "PlayerData",
  props: ['player']
  }
</script>

<style scoped>
  .v-data-table {
    border: 0px inset #04B88B;
    border-radius: 4px;;
    margin: 3px auto;
    width: 95%;
    min-width: 450px;
  }
  .v-expansion-panel-text {
    background-color: #038564;
  }
</style>