<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <v-card
        elevation="0"
        fluid
        color="#1E1E1E"
        dark
        width="150px"
        class="ma-2 pa-1"
      >
    <div class="d-flex flex-column align-center">
      <v-avatar
        class="ma-.5"
        size="125"
        tile
      >
        <v-img
          class="rounded-xl"
          contain 
          :src="item.image"
        ></v-img>
      </v-avatar> 
    </div>
    <v-fade-transition>
          <v-overlay
            class="rounded-xl"
            v-if="hover"
            absolute
            color="#036358"
          >
          <v-container class="d-flex flex-column justify-space-around">
            <v-btn
              color="primary"
              class="mb-6"
              @click="selectItem(item.api_id)"
            >Go To Page</v-btn>
            <v-btn
            v-if="page === 'User'"
              @click="removeItem(item)"
            >Remove</v-btn>
          </v-container>
          </v-overlay>
        </v-fade-transition>
      </v-card>
    </template>
  </v-hover>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'UserCard',
  props: ['item', 'page'],
  methods: {
    data: () => ({
      overlay: false,
    }),
    selectItem(itemId) {
      this.$emit('selectItem', itemId)
    },
    removeItem(player) {
      this.$emit('removeItem', player)
    }
    },
  computed: {
    ...mapState({
      user: state => state.user,
      authenticated: state => state.authenticated,
    })
  },
}
</script>

<style scoped>
  .rounded-circle{
    border: 3px solid #04B88B;
  }
  .v-overlay__content {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>