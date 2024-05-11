<template>
    <v-container fluid pa-0 >
        <v-container fluid pa-0>
            <v-row no-gutters>
                <v-col cols="12">
                    <div style="width:100%;height:40%;padding-bottom:100%;position:absolute;top: 0;border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;  background-color: transparent;background: transparent;"><iframe  src="https://giphy.com/embed/b9VhM0ZMjUVMYn8OYx" width="100%" height="100%" style="position:absolute;border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;" frameBorder="0" class="giphy-embed money-gif" ></iframe></div>              
                  </v-col>
            </v-row>
        </v-container>
        <v-container fluid pa-0 class="align-self-center px-4 pt-4 pb-4 " style="position: absolute; bottom: 0;">
            <v-row no-gutters>
                <v-col cols="12" class="text-center">
                </v-col>
            </v-row>
        <v-row no-gutters  class="pb-7">
            <v-col cols="12">
                <h6 class="login-text text-center">SIGN IN TO YOUR ACCOUNT</h6>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col class="12 pb-4 font-[500]">Email Address</v-col>
           <v-col cols="12" class="pb-10">
                <v-text-field hide-details="auto" class="login-text-field" flat outlined dense solo label="ex: johndoe@gmail.com" :rules="[rules.isRequired && rules.isEmail]"></v-text-field>
           </v-col>
           <v-row no-gutters>
            <v-col cols="6" class="text-left pb-4 font-[500]">Password</v-col>
            <v-col cols="6" class="text-right pb-4 font-[500]">Forgot password ?</v-col>

           </v-row>
           <v-col cols="12" class="pb-4">
            <v-text-field
            class="login-text-field"
            flat
            hide-details="auto" outlined dense solo
          v-model="password"
          :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
          :type="showPassword ? 'text' : 'password'"
          label="Password"
          @click:append="showPassword = !showPassword"
        ></v-text-field>
           </v-col>
        </v-row>
        <v-col cols="12" class="text-center">
            <v-btn color="#3d52a0" class="white--text" style="text-transform: none;">Sign in</v-btn>
        </v-col>
    </v-container>
    </v-container>
</template>
<script>
import rules from "@/utils/rules";
export default {
  data() {
    return {
        rules: rules,
      password: '',
      showPassword: false
    };
  }
};
</script>
<style>
.login-text{
    font-size: 25px !important;
    font-weight: 700;
    padding-bottom: 20px;
}
.login-text-field{
    border-radius: 10px;
}
.savings-text{
    font-size: 20px;
    font-weight: 700;
}
.money-gif{
    pointer-events: none;

}
</style>