import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark: false,
        options: {
          customProperties: true,
        },
        themes: {
          light: {
            primary: '#3d52a0',
            secondary: '#43A047',
            accent: '#82B1FF',
            error: '#FF5252',
            info: '#2196F3',
            success: '#4CAF50',
            warning: '#FFC107'
          },
        },
      },
});
