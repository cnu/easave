import Vue from 'vue'
import App from './App.vue'
import './index.css'
import vuetify from './plugins/vuetify'
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import router from './router'
import store from './store'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAsiAJzfNhZWEHsKHZljk3eNdWoSxVYnpI",
  authDomain: "hacktivators-7dc70.firebaseapp.com",
  projectId: "hacktivators-7dc70",
  storageBucket: "hacktivators-7dc70.appspot.com",
  messagingSenderId: "699987884268",
  appId: "1:699987884268:web:0c16ad2e1fe1d1d41f0dc9",
  measurementId: "G-2ZEKJEF42Q"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
Vue.use(app, analytics)

Vue.config.productionTip = false;

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
