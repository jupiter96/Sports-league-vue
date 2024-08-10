import Axios from 'axios'

export const BASE_URL =
  process.env.NODE_ENV === 'production'
    ? `${import.meta.env.VITE_VUE_APP_API_URL}/api`
    : 'http://localhost:5000/api'

const Client = Axios.create({
  baseURL:
    process.env.NODE_ENV === 'production'
      ? `${import.meta.env.VITE_VUE_APP_API_URL}/api`
      : 'http://localhost:5000/api'
})

export default Client
