import useAxios from '@/composables/useAxios';

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.provide('axios', useAxios());
});