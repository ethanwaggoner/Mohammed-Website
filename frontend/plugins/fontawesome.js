import { library } from '@fortawesome/fontawesome-svg-core';
import { faInstagram, faFacebook, faTwitter } from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default defineNuxtPlugin((nuxtApp) => {
  library.add(faInstagram, faFacebook, faTwitter);
  nuxtApp.vueApp.component('FontAwesomeIcon', FontAwesomeIcon);
});
