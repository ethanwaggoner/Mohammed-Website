import { definePiniaStore } from 'pinia'
import { useCookie } from '#app'
import { useAxios } from '@/composables/useAxios'
export const useUserStore = definePiniaStore('user', {
  state: () => ({
    user: null,
    isLoggedIn: false,
    isLoading: false,
    authCheckComplete: false,
    error: null,
  }),
  getters: {
    isAuthenticated(state) {
      return state.isLoggedIn
    },
  },
  actions: {
    async checkAuthentication() {
      const axios = useAxios()
      this.isLoading = true
      this.error = null
      try {
        await axios.get('/api/check-session/')
        this.isLoggedIn = true
      } catch (error) {
        this.error = error.data || 'Session check failed'
        this.isLoggedIn = false
      } finally {
        this.isLoading = false
        this.authCheckComplete = true
      }
    },
    async login(email, password) {
      if (!email || !password) {
        this.error = 'Email and password are required'
        return
      }
      const axios = useAxios()
      this.isLoading = true
      this.error = null
      try {
        const { data } = await axios.post('/api/login/', { email, password })
        this.isLoggedIn = true
        this.user = data.username
        useCookie('user', JSON.stringify(this.user))
      } catch (error) {
        this.error = error.data || 'Login failed'
        this.isLoggedIn = false
      } finally {
        this.isLoading = false
      }
    },
    async logout() {
      const axios = useAxios()
      this.isLoading = true
      this.error = null
      try {
        await axios.get('/api/logout/')
        useCookie('csrftoken', null, { maxAge: -1 })
        this.isLoggedIn = false
        useCookie('user', null, { maxAge: -1 })
        this.user = null
      } catch (error) {
        this.error = error.data || 'Logout failed'
      } finally {
        this.isLoading = false
      }
    },
  },
})