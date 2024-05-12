<template>
    <v-container pa-0 fluid>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Full Name
            </v-col>
            <v-col cols="12" class="pb-10">
                <v-text-field hide-details="auto" class="login-text-field" flat outlined dense solo label="ex: John Doe"
                    :rules="[rules.isRequired]"></v-text-field>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Email
            </v-col>
            <v-col cols="12" class="pb-10">
                <v-text-field hide-details="auto" class="login-text-field" v-model="userEmail" flat outlined dense
                        solo label="ex: johndoe@gmail.com" :rules="[rules.isRequired && rules.isEmail]"></v-text-field>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Set New Password
            </v-col>
            <v-col cols="12" class="pb-10">
                    <v-text-field class="login-text-field" flat hide-details="auto" outlined dense solo
                        v-model="password" :append-icon="showPassword ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="showPassword ? 'text' : 'password'" label="Password"
                        @click:append="showPassword = !showPassword"></v-text-field>
                </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Confirm Password
            </v-col>
            <v-col cols="12" class="pb-10">
                    <v-text-field class="login-text-field" flat hide-details="auto" outlined dense solo
                        v-model="confirmPassword" :append-icon="showConfirmPassword ? 'mdi-eye-off' : 'mdi-eye'"
                        :type="showConfirmPassword ? 'text' : 'password'" label="Confirm Password"
                        @click:append="showConfirmPassword = !showConfirmPassword"></v-text-field>
                </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="6" class="text-left"><v-btn color="primary" disabled>Back</v-btn></v-col>
            <v-col cols="6" class="text-right"><v-btn color="primary">Create Account </v-btn></v-col>
        </v-row>
    </v-container>
</template>
<script>
import rules from "@/utils/rules";

export default {
    data() {
        return {
            date: '',
            userEmail: '',
            password: '',
            showPassword: false,
            confirmPassword: '',
            showConfirmPassword: false,
            menu: false,
            e1: 1,
            rules: rules,
            industries: [
                'Manufacturing',
                'Engineering',
                'Electronics',
                'Retail',
                'Healthcare',
                'Other']
        }
    },
    computed:{
        confirmPasswordRule() {
      return [
        value => !!value || 'Please confirm your password',
        value => value === this.password || 'Passwords do not match'
      ];
    }
    }
}
</script>