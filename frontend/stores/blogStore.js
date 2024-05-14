import { defineStore } from 'pinia';
import { useNuxtApp } from '#app';

export const useBlogStore = defineStore('blog', {
  state: () => ({
    blogs: [],
    totalPages: 0,
    currentPage: 1,
    pageSize: 6,
    loading: false,
    error: null,
    searchResults: [],
  }),
  getters: {
    getBlogs: (state) => state.blogs,
    getTotalPages: (state) => state.totalPages,
    getCurrentPage: (state) => state.currentPage,
    isLoading: (state) => state.loading,
    getError: (state) => state.error,
    getSearchResults: (state) => state.searchResults,
  },
  actions: {
    async fetchBlogs(page = 1) {
      this.loading = true;
      this.error = null;
      const { $axios } = useNuxtApp();
      try {
        const response = await $axios.get(`/api/blogs/?page=${page}&page_size=${this.pageSize}`);
        this.blogs = response.data.results;
        this.totalPages = Math.ceil(response.data.count / this.pageSize);
        this.currentPage = page;
      } catch (error) {
        this.error = error.response?.data?.detail || error.message;
      } finally {
        this.loading = false;
      }
    },
    async searchBlogs(query) {
      this.loading = true;
      this.error = null;
      const { $axios } = useNuxtApp();
      try {
        const response = await $axios.get(`/api/blogs/?search=${query}`);
        this.searchResults = response.data.results;
      } catch (error) {
        this.error = error.response?.data?.detail || error.message;
      } finally {
        this.loading = false;
      }
    },
  },
});
