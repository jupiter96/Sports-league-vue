<template>
  <v-container>
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="newUser.name"
          :rules="[v => !!v || 'Name is required']"
          label="Name"
          required
        ></v-text-field>

        <v-text-field
          v-model="newUser.email"
          :rules="emailRules"
          label="Email"
          required
        ></v-text-field>

        <v-text-field
          v-model="newUser.password"
          :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[value => !!value || 'Password is required']"
          :type="show ? 'text' : 'password'"
          label="Password"
          @click:append="show = !show"
        ></v-text-field>

        <v-btn
          :disabled="!valid"
          color="success"
          @click="validate"
        >
          Register
        </v-btn>

        <v-btn
          color="error"
          class="mr-4"
          @click="reset"
        >
          Reset Form
        </v-btn>
      </v-form>
  </v-container>
</template>

<script>
import {RegisterUser} from '../services/Auth'
export default {
  name: "Register",
  data: () => ({
      show: false,
      valid: true,
      newUser: {
        name: '',
        email: '',
        password: '',
      },
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
    }),

    methods: {
      validate () {
        if (this.$refs.form.validate()) {
          RegisterUser({...this.newUser})
          this.newUser = {name: '',email: '',password: ''}
          this.$router.push(`/`)
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
}
</script>

<style scoped>
  .v-btn {
    margin-right: 1em;
    margin-top: 1em;
  }
</style>