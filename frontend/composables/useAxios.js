import { parseCookies } from 'cookie';

export default defineNuxtPlugin((nuxtApp) => {
  const axios = nuxtApp.$axios.create({
    baseURL: 'https://www.mohammedkhalid.com',
    withCredentials: true,
  });

  axios.interceptors.request.use((config) => {
    // Conditionally handle SSR and client-side
    if (process.server) {
      const req = nuxtApp.ssrContext.req;
      const cookies = parseCookies(req.headers.cookie);
      const csrfToken = cookies['csrftoken'];
      if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
      }
    } else {
      // Client-side handling with useCookie
      const csrfToken = useCookie('csrftoken').value;
      if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
      }
    }
    return config;
  });

  axios.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(error)
  );

  nuxtApp.provide('axios', axios);
});
