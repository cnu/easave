<template>
    <v-container fluid pa-0>
        <v-row no-gutters>
                        <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                            Aadhar 
                        </v-col>
                        <v-col cols="12" class="pb-10">
                            <v-text-field hide-details="auto" class="login-text-field" flat outlined dense solo
                                label="112321231234" :rules="[rules.isRequired]"></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row no-gutters>
                        <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                            PAN
                        </v-col>
                        <v-col cols="12" class="pb-10">
                            <v-text-field hide-details="auto" class="login-text-field" flat outlined dense solo
                                label="ABCTY1234D" :rules="[rules.isRequired]"></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row no-gutters>
                        <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                            Upload Image
                        </v-col>
                        <v-col cols="12" class="pb-10">
                            <input type="file" id="selfie" name="selfie" accept="image/*" capture="user" />
                        </v-col>
                    </v-row>
                    <v-row no-gutters>
                        <v-col cols="6" class="text-left" ><v-btn color="primary" >Back</v-btn></v-col>
                        <v-col cols="6" class="text-right"><v-btn color="primary">Continue</v-btn></v-col>
                    </v-row>
    </v-container>
</template>
<script>
import rules from "@/utils/rules";

export default {
    data() {
        return {
            rules: rules
        }
    },
}
</script>