<template>
    <v-container pa-0 fluid >
        <p class="font-[700]">Previous Loan Details :</p>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                Amount of loan
            </v-col>
            <v-col cols="12" class="pb-4">
             <v-text-field hide-details="auto" class="login-text-field"  v-model="currencyValue"
          label="Enter Amount"
          onKeyPress="return ( event.charCode !=8 && event.charCode ==0 || (event.charCode >= 48 && event.charCode <= 57) && this.value.length < 11) ? true :false   " 
          @input="formatCurrency" flat outlined dense solo
                    :rules="[rules.isRequired]"></v-text-field>
            </v-col>
            <v-col cols="12" class="pb-10 pl-2 currency-words" v-if="currencyIntoWords!='Zero'">
                <span>{{ currencyIntoWords + ' Rupees' }}</span>
             </v-col>
        </v-row>
        <v-row no-gutters>
            <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                How Many Months Remaining ?
            </v-col>
            <v-col cols="12" class="pb-10 px-2 pt-6">
                <v-slider
                :thumb-size="24"
          thumb-label="always"
            v-model="slider"
            class="align-center"
            :max="60"
            :min="0"
            hide-details
          >
          </v-slider>
            </v-col>
        </v-row>
        <v-row no-gutters>
                        <v-col cols="12" class="text-left pb-3 stepper-subheadings">
                            How many previous missed payments? 
                        </v-col>
                        <v-col cols="12" class="pb-10">
                            <v-text-field hide-details="auto" class="login-text-field" onKeyPress="return ( event.charCode !=8 && event.charCode ==0 || (event.charCode >= 48 && event.charCode <= 57) && this.value.length < 2) ? true :false   " flat outlined dense solo
                                 :rules="[rules.isRequired]"></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row no-gutters>
                        <v-col cols="6" class="text-left" ><v-btn color="primary" disabled>Back</v-btn></v-col>
                        <v-col cols="6" class="text-right"><v-btn color="primary">Continue</v-btn></v-col>
                    </v-row>
    </v-container>
</template>
<script>
import numberToText from 'number2text'
import rules from "@/utils/rules";
export default {
  data() {
    return {
        slider: 0,
      currencyValue: '',
      rules: rules,
    };
  },
  computed:{
    currencyIntoWords(){

        return numberToText(this.currencyValue.replace(/[^\w\s]/gi, ''))
    },
  },
  methods: {
    formatCurrency() {
        let value = this.currencyValue;
      // Remove non-digit characters and commas
      value = value.replace(/[^\d.]/g, '');
      value = value.replace(/\D/g, '');
      
      // Convert empty or NaN value to flat string
      if (value === '' || isNaN(parseFloat(value))) {
        this.currencyValue = '0';
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
      this.currencyValue = value;
    }
  }
};
</script>