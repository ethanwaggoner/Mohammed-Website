import { useCookie } from '#app'

export default defineNuxtPlugin((nuxtApp) => {
  const axios = nuxtApp.$axios.create({
    baseURL: 'https://www.mohammedkhalid.com',
    withCredentials: true,
  })

  axios.interceptors.request.use((config) => {
    const csrfToken = useCookie('csrftoken').value
    if (csrfToken) {
      config.headers['X-CSRFToken'] = csrfToken
    }
    return config
  })

  axios.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(error)
  )

  nuxtApp.provide('axios', axios)
})