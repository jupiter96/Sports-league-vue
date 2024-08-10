import Client from './api'

export const SignInUser = async data => {
  try {
    const res = await Client.post('/auth/login', data)
    // Set the current signed in users token to localstorage
    localStorage.setItem('token', res.data.token)
    return res.data.user
  } catch (error) {
    console.log(error)
  }
}

export const RegisterUser = async data => {
  try {
    const res = await Client.post('/auth/register', data)
    return res.data
  } catch (error) {
    console.log(error)
  }
}

export const CheckSession = async token => {
  try {
    // Checks if the current token if it exists is valid
    const res = await Client.get('/auth/session', {
      headers: { Authorization: token }
    })
    return res.data
  } catch (error) {
    console.log(error)
  }
}

export const UpdateUserPassword = async (userId, data) => {
  try {
    const passData = {
      old_password: data.oldPassword,
      new_password: data.newPassword
    }
    const res = await Client.put(`/auth/user/${userId}`, passData)
    return res.data
  } catch (error) {
    console.log(error)
  }
}
