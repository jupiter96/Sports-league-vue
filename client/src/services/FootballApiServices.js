import FootballClient from './FootballApi'
// import 'dotenv/config'

export const GetLeagues = async () => {
  // try {
  const res = await FootballClient.get(
    `https://v3.football.api-sports.io/leagues`
  )
  return res.data
  // } catch (error) {
  //   throw error
  // }
}

export const GetLeaguesByCountryCode = async code => {
  // try {
  const res = await FootballClient.get(
    `https://v3.football.api-sports.io/leagues?code=${code}&&season=2023`
  )
  return res.data
  // } catch (error) {
  //   throw error
  // }
}

export const GetTeamsByLeagueId = async leagueId => {
  const res = await FootballClient.get(
    `https://v3.football.api-sports.io/teams?league=${leagueId}&&season=2023`
  )
  return res.data
}
