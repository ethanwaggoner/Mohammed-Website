import { defineStore } from 'pinia';
import { useNuxtApp } from '#app';

export const useBlogStore = defineStore('blog', {
  state: () => ({
    blogs: [],
    totalPages: 0,
    currentPage: 1,
    pageSize: 20,
    loading: false,
    error: null,
    selectedTags: [],
  }),
  getters: {
    getBlogs: (state) => state.blogs,
    getTotalPages: (state) => state.totalPages,
    getCurrentPage: (state) => state.currentPage,
    isLoading: (state) => state.loading,
    getError: (state) => state.error,
    getSelectedTags: (state) => state.selectedTags,
  },
  actions: {
    async fetchBlogs(page = 1) {
      this.loading = true;
      this.error = null;
      const { $axios } = useNuxtApp();
      const tagsQuery = this.selectedTags.length > 0 ? `&tags=${this.selectedTags.join(',')}` : '';
      try {
        console.log(`Fetching blogs for page ${page} with tags: ${tagsQuery}`);
        const response = await $axios.get(`/api/blogs/?page=${page}&page_size=${this.pageSize}${tagsQuery}`);
        console.log('API response:', response.data);
        this.blogs = response.data;
        this.totalPages = Math.ceil(response.data.count / this.pageSize);
        this.currentPage = page;
        console.log('Blogs state:', this.blogs);
      } catch (error) {
        console.error('API error:', error.response?.data?.detail || error.message);
        this.error = error.response?.data?.detail || error.message;
      } finally {
        this.loading = false;
      }
    },
    async toggleTag(tag) {
      const index = this.selectedTags.indexOf(tag);
      if (index > -1) {
        this.selectedTags.splice(index, 1);
      } else {
        this.selectedTags.push(tag);
      }
      await this.fetchBlogs(1);
    },
  },
});
