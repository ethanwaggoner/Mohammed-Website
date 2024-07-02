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
        await this.fetchBlogComments(slug);
        console.log('Current blog set:', this.currentBlog);
      } catch (error) {
        console.error('Error fetching blog:', error);
        this.error = error.response?.data?.detail;
      } finally {
        this.loading = false;
      }
    },

    async fetchBlogComments(blogSlug) {
  const { $axios } = useNuxtApp();
  try {
    const response = await $axios.get(`/api/blogs/${blogSlug}/comments/`);
    const comments = response.data;

    // Create a map of comments by their IDs
    const commentMap = new Map(comments.map(c => [c.id, {...c, replies: []}]));

    // Organize comments into a tree structure
    const rootComments = [];
    comments.forEach(comment => {
      if (comment.parent_id) {
        const parent = commentMap.get(comment.parent_id);
        if (parent) {
          parent.replies.push(commentMap.get(comment.id));
        }
      } else {
        rootComments.push(commentMap.get(comment.id));
      }
    });

    this.currentBlog.comments = rootComments;
  } catch (error) {
    console.error('Error fetching comments:', error);
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
          blog_slug: blogSlug,
          ...commentData
        });
        if (this.currentBlog) {
          const newComment = response.data;
          if (newComment.parent_id) {
            const addReply = (comments) => {
              for (let comment of comments) {
                if (comment.id === newComment.parent_id) {
                  if (!comment.replies) comment.replies = [];
                  comment.replies.push(newComment);
                  return true;
                }
                if (comment.replies && addReply(comment.replies)) {
                  return true;
                }
              }
              return false;
            };
            addReply(this.currentBlog.comments);
          } else {
            this.currentBlog.comments.push(newComment);
          }
          this.currentBlog.comments_count += 1;
        } else {
          console.warn('Current blog not set.');
        }
        return response.data;
      } catch (error) {
        console.error('Error posting comment:', error);
        throw error;
      }
    },

    findCommentById(commentId) {
      const findInComments = (comments) => {
        for (let comment of comments) {
          if (comment.id === commentId) return comment;
          if (comment.replies) {
            const found = findInComments(comment.replies);
            if (found) return found;
          }
        }
        return null;
      };
      return findInComments(this.currentBlog.comments);
    }
  },
});