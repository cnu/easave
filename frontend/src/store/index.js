import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    onBoardUser: {},
    userData: {},
  },
  getters: {
    getterOBUser: (state) =>{
      return state.onBoardUser
    },
    getterUserData: (state) =>{
      return state.userData
    }
  },
  mutations: {
    SET_ONBOARD_USER(state , data)
    {
      state.onBoardUser = Object.assign(state.onBoardUser, data)
    },
    SET_USER_DATA(state , data){
      state.userData = Object.assign(state.userData , data)
    }
  },
  actions: {
  },
  modules: {
  }
})
