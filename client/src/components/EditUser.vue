<template>
  <v-container>
    <!-- UPDATE USER INFO -->
    <template >
      <v-form
        ref="form"
        v-model="validInfo"
        lazy-validation
        class="my-1"
      >
        <v-text-field
          v-model="updateInfo.name"
          label="Name"
        ></v-text-field>
        <v-text-field
          v-model="updateInfo.email"
          :rules="emailRules"
          label="Email"
        ></v-text-field>
        <h4 v-if="isInfoChanged" color="green">Info Changed</h4>
        <h4 v-if="isInfoReject" color="red">Info Not Changed</h4>
        <v-btn
          :disabled="!validInfo"
          color="success"
          @click="updateUserInfo"
        >
          Update Info
          </v-btn>
      </v-form>
    </template>
    <!-- UPDATE USER PASSWORD -->
    <template>
      <v-form
        ref="form"
      >
        <v-text-field
          v-model="updatePassword.oldPassword"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show1 ? 'text' : 'password'"
          label="Old Password"
          @click:append="show1 = !show1"
        ></v-text-field>
        <v-text-field
          v-model="updatePassword.newPassword"
          :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
          :type="show2 ? 'text' : 'password'"
          label="New Password"
          @click:append="show2 = !show2"
        ></v-text-field>
        <h4 v-if="isPassChanged" color="green">Password Changed</h4>
        <h4 v-if="isPassReject" color="red">Password Not Changed</h4>
        <v-btn
          :disabled="!updatePassword.oldPassword || !updatePassword.newPassword"
          color="success"
          @click="updateUserPassword"
        >
          Update Password
        </v-btn>
      </v-form>
    </template>
  <v-container class="d-flex justify-end align-center ma-0 pa-0">
      <h4 v-if="isDeleteReject" class="mx-5" color="red">User Not Deleted</h4>
      <v-btn
          color="red"
          @click="deleteUser"
        >
          Delete User
      </v-btn>
  </v-container>
  </v-container>
</template>

<script>
import {UpdateUserPassword} from '../services/Auth'
import {UpdateUser, DeleteUser} from '../services/UserServices'
import { mapActions, mapState } from 'vuex'
export default {
  name: "EditUser",
  data: () => ({
      show1: false,
      show2: false,
      isInfoChanged: false,
      isInfoReject: false,
      isPassChanged: false,
      isPassReject: false,
      isDeleteReject: false,
      validInfo: true,
      updatePassword: {
        oldPassword: '',
        newPassword: ''
      },
      updateInfo: {
        name: '',
        email: '',
      },
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
    }),

    methods: {
      async updateUserPassword () {
          const res = await UpdateUserPassword(this.user.id, {...this.updatePassword})
          if(res) {
            this.isPassChanged = true
            this.updatePassword = {oldPassword: '',newPassword: ''}
          } else {
            this.isPassReject = true
          }
      },
      async updateUserInfo () {
          const res = await UpdateUser(this.user.id, {...this.updateInfo})
          if(res) {
            this.isInfoChanged = true
            this.updateInfo = { name: '', email: ''}
          } else {
            this.isInfoReject = true
          }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
      async deleteUser () {
        console.log('delete')
        const res = await DeleteUser(this.user.id)
        if(res) {
          this.$router.push(`/`)
        } else {
          this.isDeleteReject = true
        }
      }, 
    },
    computed: mapState({
      user: state => state.user,
      authenticated: state => state.authenticated
  }),
}
</script>

<style scoped>
  .v-btn {
    margin-right: 1em;
    margin-top: 1em;
  }
  .v-form {
    margin-top: 2em;
  }
</style>