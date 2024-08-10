import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'

const darkTheme = {
  dark: true,
  colors: {
    primary: '#038564',
    secondary: '#6B0D1D',
    error: '#D13404'
  }
}

const lightTheme = {
  dark: false,
  colors: {
    primary: '#016B4F',
    secondary: '#04B88B',
    error: '#D13404'
  }
}

export default createVuetify({
  theme: {
    defaultTheme: 'darkTheme',
    themes: {
      darkTheme,
      lightTheme
  }},
  icons: {
    iconfont: 'mdi'
  }
})
