<script setup>
import { ref, onMounted, computed } from 'vue';
import { useBlogStore } from '@/stores/blogStore';
import NavBar from "~/components/NavBar.vue";

const blogStore = useBlogStore();
const backgroundImage = ref('/images/background2.jpg');

const blogs = computed(() => blogStore.getBlogs);
const allTags = computed(() => {
  const tagSet = new Set();
  blogs.value.forEach(blog => {
    if (blog.tags && Array.isArray(blog.tags)) {
      blog.tags.forEach(tag => tagSet.add(tag));
    }
  });
  return Array.from(tagSet);
});

onMounted(async () => {
  console.log('Fetching blogs...');
  await blogStore.fetchBlogs();
  console.log('Blogs:', blogs.value);
});

const handleTagSelect = async (tag) => {
  await blogStore.toggleTag(tag);
};

const loadNewerPosts = async () => {
  if (blogStore.getCurrentPage > 1) {
    await blogStore.fetchBlogs(blogStore.getCurrentPage - 1);
  }
};

const loadOlderPosts = async () => {
  if (blogStore.getCurrentPage < blogStore.getTotalPages) {
    await blogStore.fetchBlogs(blogStore.getCurrentPage + 1);
  }
};

const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};
</script>


<template>
  <div class="blog-page">
    <div class="hero-section" :style="{ backgroundImage: `url(${backgroundImage})` }">
      <div class="nav">
        <NavBar />
      </div>
      <div class="overlay">
        <h1>"Before you speak, let your words pass through three gates:</h1>
        <h1>Is it true?</h1>
        <h1>Is it necessary?</h1>
        <h1>Is it kind?"</h1>
        <p><em>-Rumi</em></p>
      </div>
    </div>

    <div class="tag-filter">
      <h3>Filter by Tags:</h3>
      <div class="tag-list">
        <span
          v-for="tag in allTags"
          :key="tag"
          @click="handleTagSelect(tag)"
          :class="{ 'selected': blogStore.getSelectedTags.includes(tag) }"
          class="tag"
        >
          {{ tag }}
        </span>
      </div>
    </div>

    <div v-if="blogStore.isLoading" class="loading">
      Loading...
    </div>

    <div v-else-if="blogStore.getError" class="error">
      {{ blogStore.getError }}
    </div>

    <div v-else-if="blogs.length > 0" class="blog-grid">
      <div v-for="blog in blogs" :key="blog.id" class="blog-item">
        <img :src="blog.image" :alt="blog.title" />
        <div class="blog-content">
          <h2>{{ blog.title }}</h2>
          <p>{{ blog.excerpt }}</p>
          <div class="blog-meta">
            <span class="date">{{ formatDate(blog.created_at) }}</span>
            <div v-if="blog.tags && blog.tags.length > 0" class="tags">
              <span
                v-for="tag in blog.tags"
                :key="tag"
                class="tag"
                :class="{ 'selected': blogStore.getSelectedTags.includes(tag) }"
                @click="handleTagSelect(tag)"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="no-blogs">
      <p>No blogs available.</p>
    </div>

    <div class="pagination">
      <button @click="loadNewerPosts" :disabled="blogStore.getCurrentPage === 1">&lt; Newer Posts</button>
      <button @click="loadOlderPosts" :disabled="blogStore.getCurrentPage === blogStore.getTotalPages">Older Posts &gt;</button>
    </div>
  </div>
</template>

<style scoped>
.hero-section {
  height: 100vh;
  background-size: cover;
  background-position: center;
  color: white;
  text-align: start;
  margin-bottom: 40px;
}

.overlay {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 10%;
}

.overlay p {
  align-self: flex-end;
  font-size: 1.5rem;
}

.hero-section h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

.tag-filter {
  margin: 20px 10%;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 10px;
}

.blog-grid {
  margin: 10%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 40px;
}

.blog-item {
  display: flex;
  flex-direction: column;
}

.blog-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 8px;
}

.blog-content {
  padding: 20px 0;
}

.blog-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.tags {
  display: flex;
  gap: 10px;
}

.tag {
  background-color: #f0f0f0;
  padding: 5px 10px;
  border-radius: 15px;
  font-size: 0.8rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.tag.selected {
  background-color: #007bff;
  color: white;
}

.pagination {
  display: flex;
  justify-content: space-between;
  margin: 40px 10%;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.loading, .error, .no-blogs {
  text-align: center;
  margin: 20px 0;
  font-size: 1.2rem;
}

.error {
  color: red;
}
</style>