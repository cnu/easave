import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);


const routes = [
  {
    path: '/login',
    component: () => import("../views/LoginPage.vue"),
    name: 'Login'
  },
  {
    path: '/onboarduser',
    component: () =>  import("../views/OnBoardUserView.vue"),
    name: 'OnBoardUser'
  }
];

const router = new VueRouter({
  routes,
  mode: 'history',
});


export default router;
