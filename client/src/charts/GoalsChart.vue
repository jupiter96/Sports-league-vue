<template>
  <Radar :data="data" :options="options" />
</template>

<script>

import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
} from 'chart.js'
import { Radar } from 'vue-chartjs'

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
)

export default {
  name: 'GoalsChart',
  props:['goalData'],
  components: {
    Radar
  },
  methods: {
    getChartConfig() {
      return ({
        data: {
        labels: this.goalData.labels,
        datasets: [
          {
            label: 'Team Goals',
            backgroundColor: 'rgba(4, 184, 139, 0.2)',
            borderColor: '#04B88B',
            pointBackgroundColor: '#04B88B',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#04B88B',
            data: this.goalData.goalDataTeam
          },
          {
            label: 'Opponent Goals',
            backgroundColor: 'rgba(255,99,132,0.2)',
            borderColor: 'rgba(255,99,132,1)',
            pointBackgroundColor: 'rgba(255,99,132,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(255,99,132,1)',
            data: this.goalData.goalDataOpp
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
      })
    }
  },
  data() {
    return this.getChartConfig()
  }
}

</script>
