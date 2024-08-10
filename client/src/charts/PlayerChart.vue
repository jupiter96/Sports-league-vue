<template>
  <Bar :data="data" :options="options" />
</template>

<script>

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { Bar } from 'vue-chartjs'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
)

export default {
  name: 'RadarChart',
  props:['radarData'],
  components: {
    Bar
  },
  methods: {
    getChartConfig() {
      return ({
        data: {
        labels: this.radarData.labels,
        datasets: [
          {
            label: this.radarData.labelSet1,
            backgroundColor: 'rgba(4, 184, 139, 0.2)',
            borderColor: '#04B88B',
            pointBackgroundColor: '#04B88B',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#04B88B',
            data: this.radarData.dataSet1
          },
          {
            label: this.radarData.labelSet2,
            backgroundColor: 'rgba(255,99,132,0.2)',
            borderColor: 'rgba(255,99,132,1)',
            pointBackgroundColor: 'rgba(255,99,132,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(255,99,132,1)',
            data: this.radarData.dataSet2
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