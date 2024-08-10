<template>
  <v-container>
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="existingUser.email"
          :rules="emailRules"
          label="Email"
          required
        ></v-text-field>
        <v-text-field
          v-model="existingUser.password"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show ? 'text' : 'password'"
          label="Password"
          @click:append="show = !show"
        ></v-text-field>
        <div class="button-container">
          <v-btn
            :disabled="!valid"
            color="success"
            @click="validate"
          >
            Login
          </v-btn>
          <v-btn
            color="primary"
            @click="registerPage"
          >
            Register
          </v-btn>
        </div>
        <v-list-subheader v-if="loginFailed" class="error--text">Login Failed</v-list-subheader>
      </v-form>
  </v-container>
</template>

<script>
import { SignInUser } from "../services/Auth"
import { mapActions, mapState } from 'vuex'
export default {
  name: "Login",
  data: () => ({
      show: false,
      valid: true,
      loginFailed: false,
      existingUser: {
        email: '',
        password: '',
      },
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
  }),
  methods: {
    ...mapActions(['setUser','toggleAuthenticated']),
    validate () {
      if (this.$refs.form.validate()) {
        this.handleLogin()
      }
    },
    async handleLogin() {
      const payload = await SignInUser(this.existingUser)
      if (payload){
        this.setUser(payload)
        this.toggleAuthenticated(true)
        this.loginFailed = false;
      } else {
        this.loginFailed = true;
      }
    },
    // handeLogIn(user, isAuthenticated) {
    //   this.$emit('handleLogIn', user, isAuthenticated)
    // },
    registerPage() {
      this.$router.push('/register')
    },
  },
  computed: mapState({
    user: state => state.user,
    authenticated: state => state.authenticated
  }),
}
</script>

<style scoped>
  .button-container {
    display: flex;
    justify-content: space-between;
  }
</style>