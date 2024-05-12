<template>
    <v-container fluid pa-0>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Deposit Money
            </v-col>
            <v-col cols="12" class="pb-4">
                <v-text-field hide-details="auto" class="login-text-field" onKeyPress="return ( event.charCode !=8 && event.charCode ==0 || (event.charCode >= 48 && event.charCode <= 57) && this.value.length < 8) ? true :false   " flat outlined dense solo label="Enter Amount"
                    :rules="[rules.isRequired]" v-model="depositMoney" @input="formatCurrency"></v-text-field>
            </v-col>
            <v-col cols="12" class="pb-10 pl-2 currency-words" v-if="currencyIntoWords!='Zero'">
                <span>{{ currencyIntoWords + ' Rupees'}}</span>
             </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Term Period
            </v-col>
            <v-col cols="12" class="pb-10">
                <v-select hide-details="auto" class="login-text-field" :items="termperiod" flat outlined dense solo
                    label="5 Months" :rules="[rules.isRequired]">
                </v-select>
            </v-col>
        </v-row>
        <v-row no-gutters class="pb-10">
            <v-col cols="12">
                <v-checkbox label="Terms and conditions"></v-checkbox>
            </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-center">
                <v-btn id="rzp-button1">Pay now</v-btn>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
import rules from "@/utils/rules";
import numberToText from 'number2text'

export default {
    data() {
        return {
            rules: rules,
            depositMoney: '',
            termperiod: [1,2,3,4,5]
        }
    },
    computed:{
    currencyIntoWords(){

        return numberToText(this.depositMoney.replace(/[^\w\s]/gi, ''))
    },
  },
    methods:{
        formatCurrency() {
        let value = this.depositMoney;
      // Remove non-digit characters and commas
      value = value.replace(/[^\d.]/g, '');
      value = value.replace(/\D/g, '');
      
      // Convert empty or NaN value to flat string
      if (value === '' || isNaN(parseFloat(value))) {
        this.depositMoney = '0';
        return;
      }
      
      // Format the value as a whole number without decimal points
      value = parseInt(value).toLocaleString('en-US', {
        style: 'currency',
        currency: 'INR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
      });
      
      // Update the model with formatted value
      this.depositMoney = value;
    }
    }
}
</script>   