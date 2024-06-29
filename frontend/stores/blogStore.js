import { defineStore } from 'pinia';
import { useNuxtApp } from '#app';

export const useBlogStore = defineStore('blog', {
  state: () => ({
    blogs: [],
    currentBlog: null,
    totalPages: 0,
    currentPage: 1,
    pageSize: 20,
    loading: false,
    error: null,
    selectedTags: [],
  }),
  getters: {
    getBlogs: (state) => state.blogs,
    getCurrentBlog: (state) => state.currentBlog,
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
        const response = await $axios.get(`/api/blogs/?page=${page}&page_size=${this.pageSize}${tagsQuery}`);
        this.blogs = response.data;
        this.totalPages = Math.ceil(response.data.count / this.pageSize);
        this.currentPage = page;
        console.log('Blogs fetched:', this.blogs);
      } catch (error) {
        console.error('Error fetching blogs:', error);
        this.error = error.response?.data?.detail || error.message;
      } finally {
        this.loading = false;
      }
    },

    async fetchBlogBySlug(slug) {
      console.log('Fetching blog with slug:', slug);
      this.loading = true;
      this.error = null;
      const { $axios } = useNuxtApp();
      try {
        const response = await $axios.get(`/api/blogs/${slug}/`);
        console.log('Blog fetched:', response.data);
        this.currentBlog = response.data;
        console.log('Current blog set:', this.currentBlog);
      } catch (error) {
        console.error('Error fetching blog:', error);
        this.error = error.response?.data?.detail } finally {
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
        async postComment(blogSlug, commentData) {
      const { $axios } = useNuxtApp();
      try {
        const response = await $axios.post(`/api/comments/`, {
          ...commentData,
          blog_slug: blogSlug
        });
        if (this.currentBlog) {
          this.currentBlog.comments.push(response.data);
          this.currentBlog.comments_count += 1;
        } else {
          console.warn('Current blog not set.');
        }
      } catch (error) {
        console.error('Error posting comment:', error);
      }
    }

  },
});