import Client from './api'

export const AddTeamToUser = async data => {
  try {
    const getTeam = await Client.get(`/teamapi/${data.api_id}`)
    if (getTeam.data) {
      const userTeam = await Client.post(`/user/teams`, {
        user_id: parseFloat(data.user_id),
        team_id: getTeam.data.id
      })
      return userTeam
    } else {
      const team = await Client.post('/teams', {
        name: data.name,
        image: data.image,
        api_id: data.api_id
      })
      await Client.post('/user/teams', {
        user_id: parseFloat(data.user_id),
        team_id: team.data.id
      })
      return team
    }
  } catch (error) {
    console.log(error)
  }
}

export const RemoveTeamFromUser = async data => {
  try {
    const res = await Client.delete(`/user/teams`, { data: { ...data } })
    return res.data
  } catch (error) {
    console.log(error)
  }
}

// /user/teams
