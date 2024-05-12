<template>
    <v-container pa-0 fluid>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Buisness Name
            </v-col>
            <v-col cols="12" class="pb-10">
                <v-text-field hide-details="auto" class="login-text-field" flat outlined dense solo
                    label="ex: Harbor Haven Consulting" :rules="[rules.isRequired]"></v-text-field>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Industry
            </v-col>
            <v-col cols="12" class="pb-10">
                <v-select hide-details="auto" class="login-text-field" :items="industries" flat outlined dense solo
                    label="ex: Software" :rules="[rules.isRequired]"></v-select>
            </v-col>
        </v-row>
        <v-row no-gutters>
                        <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                            PAN
                        </v-col>
                        <v-col cols="12" class="pb-10">
                            <v-text-field hide-details="auto" class="login-text-field" onKeyPress="return ( this.value.length < 10) ? true :false   " flat outlined dense solo max="10" min="10"
                                label="ABCTY1234D" :rules="[rules.isRequired]"></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Buisness Name
            </v-col>
            <v-col cols="12" class="pb-10">
                <v-text-field hide-details="auto" class="login-text-field" flat outlined dense solo
                    label="ex: 27AAAAP0267H2ZN" :rules="[rules.isRequired]"></v-text-field>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Buisness Address
            </v-col>
            <v-col cols="12" class="pb-10">
                <v-textarea hide-details="auto" class="login-text-field" flat outlined dense solo
                    label="ex: Mr John Smith, 132, My Street, Kingston, New York 12401"
                    :rules="[rules.isRequired]"></v-textarea>
            </v-col>
        </v-row>
        
        <v-row no-gutters>
            <v-col cols="6" class="text-left"><v-btn color="primary" disabled>Back</v-btn></v-col>
            <v-col cols="6" class="text-right"><v-btn color="primary">Continue</v-btn></v-col>
        </v-row>
    </v-container>
</template>
<script>
import rules from "@/utils/rules";

export default {
    data() {
        return {
            date: '',
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
}
</script>