import Axios from 'axios'

const API_KEY = import.meta.env.VITE_VUE_APP_FOOTBALL_KEY

const FootballClient = Axios.create({
  baseURL: 'https://v3.football.api-sports.io',
  headers: {
    'x-rapidapi-host': 'v3.football.api-sports.io',
    'x-rapidapi-key': API_KEY
  }
})

export default FootballClient
