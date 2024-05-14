import axios from 'axios';
import { parseCookies } from 'cookie';
import { useNuxtApp } from '#app';
import { useCookie } from '#imports';

export default function useAxios() {
  const nuxtApp = useNuxtApp();
  const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    withCredentials: true,
  });

  axiosInstance.interceptors.request.use((config) => {
    if (process.server) {
      const req = nuxtApp.ssrContext.req;
      const cookies = parseCookies(req.headers.cookie);
      const csrfToken = cookies['csrftoken'];
      if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
      }
    } else {
      const csrfToken = useCookie('csrftoken').value;
      if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
      }
    }
    return config;
  });

  axiosInstance.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(error)
  );

  return axiosInstance;
}
