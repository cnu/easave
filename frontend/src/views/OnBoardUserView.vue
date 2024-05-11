<template>
    <div>
        <v-stepper non-linear class="stepper-class" color="#EDE8F5" flat>
            <v-stepper-header>
                <v-stepper-step editable step="1">
                    Personal Information
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step editable step="2">
                    KYC and Verfication
                </v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="3" editable>
                    Credit History
                </v-stepper-step>
                <v-divider></v-divider>

                <v-stepper-step editable step="4">
                    Savings and investments
                </v-stepper-step>
                <v-divider></v-divider>

                <v-stepper-step editable step="5">
                    Payments
                </v-stepper-step>
            </v-stepper-header>
            <v-stepper-content step="1">
                <p class="stepper-start-heading">Personal Information</p>
                <personal-information></personal-information>
            </v-stepper-content>
            <v-stepper-content step="2">
                <p class="stepper-start-heading">KYC and Verification</p>
                <KYCVerification></KYCVerification>
            </v-stepper-content>
            <v-stepper-content step="3">
                <p class="stepper-start-heading">Credit History</p>
                <CreditHistory></CreditHistory>
            </v-stepper-content>
        </v-stepper>
    </div>
</template>
<script>
import rules from "@/utils/rules";
import PersonalInformation from '@/components/PersonalInformation.vue'
import KYCVerification from '@/components/KYCVerification.vue'
import CreditHistory from '@/components/CreditHistory.vue'

export default {
    data() {
        return {
            date: '',
            menu: false,
            e1: 1,
            rules: rules
        }
    },
    components:{
        PersonalInformation,
        KYCVerification,
        CreditHistory
    }
}
</script>
<style>
.stepper-class {
    background-color: #EDE8F5;
}
.stepper-subheadings{
    font-weight: 500;
}
.stepper-start-heading{
    font-size: 25px;
    font-weight: 700;
    text-align: center;
}
</style>