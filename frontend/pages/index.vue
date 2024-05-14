<script setup>
import { ref, computed } from 'vue';
import { useBlogStore } from '@/stores/blogStore';
import NavBar from '@/components/NavBar.vue';
import { useRouter } from 'vue-router';


const blogStore = useBlogStore();
blogStore.fetchBlogs();

const currentPage = ref(0);
const itemsPerPage = 3;

const totalPages = computed(() => Math.ceil(blogStore.blogs.length / itemsPerPage));

const next = () => {
  if (currentPage.value < totalPages.value - 1) {
    currentPage.value++;
  }
};

const prev = () => {
  if (currentPage.value > 0) {
    currentPage.value--;
  }
};

const router = useRouter();

const goToBlog = () => {
  router.push('/blog');
};
</script>

<template>
  <div class="background-image">
    <NavBar />
    <div class="overlay">
      <h1>Live experiences of one dude's life, relationships, hopes, and faith.</h1>
      <NuxtLink to="/blog"><button>Read Now</button></NuxtLink>
    </div>
  </div>
  <div class="carousel-container">
    <button @click="prev" class="carousel-control prev">&lt;</button>
    <div class="carousel">
      <div
        class="carousel-item"
        v-for="(blog, index) in blogStore.blogs.slice(currentPage * itemsPerPage, currentPage * itemsPerPage + itemsPerPage)"
        :key="index"
      >
        <img :src="blog.image" alt="Blog Image" />
        <p>{{ new Date(blog.created_at).toLocaleDateString() }}</p>
        <h2>{{ blog.title }}</h2>
      </div>
    </div>
    <button @click="next" class="carousel-control next">&gt;</button>
  </div>
</template>

<style scoped>
.background-image {
  background-image: url('@/assets/homepageMohammed.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100%;
  justify-content: center;
  text-align: center;
  color: white;
}

.overlay {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-size: 5em;
  margin: 10%;
}

button {
  background-color: darkorange;
  color: black;
  border: none;
  padding: 10px 20px;
  font-size: 1.5em;
  cursor: pointer;
}

button:hover {
  background-color: darkorange;
}
</style>