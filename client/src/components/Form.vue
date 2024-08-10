<template>
  <v-row
    align="center"
    justify="center"
  >
  <div class="text-h5 mb-0 px-5 text-truncate">
    Current Form:
  </div>
  <div
    v-for="(form,i) in formArray"
    :key="i"
  >
    <v-icon v-if="form === 'W'" color="green">mdi-alpha-w-circle</v-icon>
    <v-icon  v-else-if="form === 'L'" color="red">mdi-alpha-l-circle</v-icon>
    <v-icon v-else color="#BDBDBD">mdi-alpha-d-circle</v-icon>
    <div class="mx-2"></div>
  </div>
  </v-row>
</template>

<script>
export default {
  name: "Form",
  props: ['form'],
  data: () => ({
    formArray: []
  }),
  mounted() {
    this.formArray = this.form.split('')
  }
}
</script>

<style scoped>
  .text-h5 {
    color: #04B88B;
  }
</style>