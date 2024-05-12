<template>
  <v-app  style="background-color: #adbbda !important;">
    <v-main>
      <v-container>
        <v-row justify="center" no-gutters>
          <v-col cols="12">
        <ErrorDialog></ErrorDialog>

            <!-- Your content goes here -->
            <v-card flat color="#EDE8F5" height="95vh" class="rounded-lg" style="overflow: scroll;">
              <keep-alive>
        <router-view />
      </keep-alive>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
     
    </v-main>
  </v-app>
</template>

<script>
import ErrorDialog from '@/uiComponents/ErrorDialog.vue'
export default {
  name: "App",
  data() {
    return {
   
    }
  },
  components:{
    ErrorDialog,
  },
  mounted() {

  },
  beforeRouteEnter(to, from, next) {
    next(() => {
    });
  },
};
</script>
<style>
.v-text-field.v-text-field--enclosed:not(.v-text-field--rounded) > .v-input__control > .v-input__slot, .v-text-field.v-text-field--enclosed .v-text-field__details{
  background-color: rgba(237, 232, 245, 0.5); /* Adjust the alpha value (0.5 in this case) to set the opacity */
}
</style>

