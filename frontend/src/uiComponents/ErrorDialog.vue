<template>
    <v-container>
  
      <!-- Error dialog -->
      <v-dialog v-model="showErrorDialog" max-width="200px" style="border-radius: 90% !important;">
        <v-card class="glassmorphism-dialog">
          <!-- You can add any content inside the dialog -->
          <v-card-text >
            <v-row no-gutters>
            <v-col class="text-center">
            <iframe src="https://giphy.com/embed/8L0Pky6C83SzkzU55a" width="150" height="100" frameBorder="0" class="giphy-embed" ></iframe>
            </v-col>

            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-row no-gutters class="text-center">
                <v-col>
            <v-btn color="primary" @click="showErrorDialog = false">Close</v-btn>
                </v-col>
            </v-row>
            
          </v-card-actions>
        </v-card>
      </v-dialog>
  
      <!-- Success dialog -->
      <v-dialog v-model="showSuccessDialog" max-width="200px" style="border-radius: 50% !important;">
        <v-card class="glassmorphism-dialog">
            <v-card-text >
            <v-row no-gutters>
            <v-col class="text-center pt-3">
                <iframe src="https://giphy.com/embed/tf9jjMcO77YzV4YPwE" width="150" height="100" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
            </v-col>

            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-row no-gutters class="text-center">
                <v-col>
            <v-btn color="green" class="white--text" @click="showSuccessDialog = false">Close</v-btn>
                </v-col>
            </v-row>
            
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
  </template>
  
  <script>
import { EventBus } from "@/lib/EventBus";
  export default {
    data() {
      return {
        showErrorDialog: false,
        showSuccessDialog: false,
      };
    },
    mounted(){
        var self = this
        EventBus.$on('SUCCESS' , () => self.showSuccessDialog=true)
        EventBus.$on('ERROR' , () => self.showErrorDialog=true)

    },
    watch: {
        showSuccessDialog(newValue) {
      if (newValue) {
        setTimeout(() => {
          if (this.showSuccessDialog) {
            this.showSuccessDialog = false;
          }
        }, 1000); // Close the dialog after 3 seconds (3000 milliseconds)
      }
    }
  }
  };
  </script>
  
  <style scoped>
.glassmorphism-dialog {
  background-color: rgba(255, 255, 255, 0.1) ; /* Adjust opacity as needed */
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  border-radius: 50% ;
}
  .error-dialog-title {
    background-color: #f44336;
    color: white;
  }
  .success-dialog-title {
    background-color: #4caf50;
    color: white;
  }
  </style>
  