<template>
  <v-hover >
    <template v-slot:default="{ hover }" >
    <v-card
      class="mx-auto my-2"
      max-width="344"
      @click="selectCountry(country.code)"
    >
      <v-img
        :src="`https://media.api-sports.io/flags/${country.code}.svg`"
        height="200px"
      >
        
      </v-img>
        <v-fade-transition>
        <v-overlay
          v-if="hover"
          absolute
          opacity=".9"
          color="#015E45"
        >
          <v-card-title 
          class="text-h4 text--primary"
          v-text="country.name"></v-card-title>
        </v-overlay>
      </v-fade-transition>
    </v-card>
    </template>
  </v-hover>
</template>

<script>
export default {
  name: 'Home',
  props: {
    country: {}
  },
  methods: {
    selectCountry(countryId) {
      this.$emit('selectCountry', countryId)
    }
}
}
</script>