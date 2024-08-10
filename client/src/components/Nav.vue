<template>
  <div>
    <v-app-bar
        app
        color="secondary"
        dark
      >
      <router-link to="/">
        <v-toolbar-title >SportsVue</v-toolbar-title>
      </router-link>
      <v-spacer></v-spacer>
      <router-link v-if="authenticated && user" :to="`/user/${user.id}`">
        <v-btn icon>
          <v-icon>mdi-account-star</v-icon>
        </v-btn>
      </router-link>
      <router-link to="/">
        <v-btn icon>
          <v-icon>mdi-home</v-icon>
        </v-btn>
      </router-link>
    <v-menu>
      <template v-slot:activator="{ props }">
          <v-btn
            icon
            v-bind="props"
          >
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
      </template>
      <v-list>
          <v-list-item v-if="authenticated && user" @click="goToUserPage(user.id)">
            <v-list-item-title>User Page</v-list-item-title>
          </v-list-item>
        <v-list-item v-if="!authenticated && !user" @click="signIn">
          <v-list-item-title>Sign In</v-list-item-title>
        </v-list-item>
        <v-list-item v-if="!authenticated && !user" @click="register">
          <v-list-item-title>Register</v-list-item-title>
        </v-list-item>
        <v-list-item v-else @click="signOut">
          <v-list-item-title>Sign Out</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    </v-app-bar>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
export default {
  name: "Nav",
  data: () => ({
      drawer: false,
      group: null,
    }),
  watch: {
    group () {
        this.drawer = false
      },
    },
  computed: mapState({
    user: state => state.user,
    authenticated: state => state.authenticated
  }),
  methods: {
    ...mapActions(['toggleAuthenticated','setUser']),
    goToUserPage(userId) {
      this.$router.push(`/user/${userId}`)
    },
    signOut() {
      localStorage.removeItem('token')
      this.setUser(null)
      this.toggleAuthenticated(false)
      this.$router.push(`/`)
    },
    signIn() {
      this.$router.push(`/`)
    },
    register() {
      this.$router.push(`/register`)
    }
  },
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap');
  a {
    text-decoration: none;
  }
  .v-application a {
    color: white;
    font-family: 'Alfa Slab One', cursive;
  }
  .v-toolbar {
    padding: 4px 16px;
  }
</style>