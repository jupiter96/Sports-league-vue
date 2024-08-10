import Client from './api'

export const AddPlayerToUser = async data => {
  try {
    const getPlayer = await Client.get(`/playerapi/${data.api_id}`)
    if (getPlayer.data) {
      const userPlayer = await Client.post(`/user/players`, {
        user_id: parseFloat(data.user_id),
        player_id: getPlayer.data.id
      })
      return userPlayer
    } else {
      const player = await Client.post('/players', {
        name: data.name,
        image: data.image,
        api_id: data.api_id
      })
      await Client.post('/user/players', {
        user_id: parseFloat(data.user_id),
        player_id: player.data.id
      })
      return player
    }
  } catch (error) {
    console.log(error)
  }
}

export const RemovePlayerFromUser = async data => {
  try {
    const res = await Client.delete(`/user/players`, { data: { ...data } })
    return res.data
  } catch (error) {
    console.log(error)
  }
}

// team API /playerapi/<string:api_id>
// players
// /user/players
