<script setup>
import { ref, computed } from 'vue';
import { useBlogStore } from '@/stores/blogStore';
import NavBar from '@/components/NavBar.vue';
import { useRouter } from 'vue-router';
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";


const blogStore = useBlogStore();
blogStore.fetchBlogs();

const searchQuery = ref('');

const searchBlogs = () => {
  if (searchQuery.value) {
    blogStore.searchBlogs(searchQuery.value);
  } else {
    blogStore.searchResults = [];
  }
};

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

const getAbsoluteImageUrl = (relativeUrl) => {
  if (relativeUrl.startsWith('http')) {
    return relativeUrl;
  }
  return `http://127.0.0.1:8000${relativeUrl}`;
};
</script>

<template>
  <div class="background-image">
    <NavBar />
    <div class="overlay1">
      <h1>Live experiences of one dude's life, relationships, hopes, and faith.</h1>
      <NuxtLink to="/blog"><button>Read Now</button></NuxtLink>
    </div>
  </div>
  <h2>Latest Archives</h2>
  <div class="carousel-container">
    <button @click="prev" class="carousel-control prev">&lt;</button>
    <div class="carousel">
      <div
        class="carousel-item"
        v-for="(blog, index) in blogStore.blogs.slice(currentPage * itemsPerPage, currentPage * itemsPerPage + itemsPerPage)"
        :key="index"
      >
        <img :src="getAbsoluteImageUrl(blog.image)" alt="Blog Preview" />
        <p>{{ new Date(blog.created_at).toLocaleDateString() }}</p>
        <h3>{{ blog.title }}</h3>
        <NuxtLink to="/blog"><button>Read More -></button></NuxtLink>
      </div>
    </div>
    <button @click="next" class="carousel-control next">&gt;</button>
  </div>
  <div class="hero-section">
    <img src="../assets/images/homepagePrayer.png" class="hero-background" alt="Hero Background" />
    <div class="overlay2">
      <h1>Mo’s Notes aims to unravel the complexities of our world.</h1>
      <p>Chronicling one person’s lived experiences.</p>
      <NuxtLink to="/about"><button>Learn More</button></NuxtLink>
    </div>
  </div>
  <BottomBar />
</template>


<style scoped>
.background-image {
  background-image: url('../assets/images/homepageMohammed.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh;
  width: 100%;
  justify-content: center;
  text-align: center;
  color: white;
}

.overlay1 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-size: 5em;
  margin: 10%;
}

h2 {
  font-size: 2em;
  color: black;
  margin-left: 15%;
}

button {
  background-color: darkorange;
  color: black;
  border: none;
  padding: 20px 40px;
  font-size: 1.2em;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: black;
  color: white;
}

.carousel-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
  scale: .9;
}

.carousel {
  display: flex;
  overflow: hidden;
  width: 80%;
}

.carousel-item {
  flex: 0 0 33.3333%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  box-sizing: border-box;
}

.carousel-item img {
  width: 100%;
  height: 40vh;
  border-radius: 10px;
}

.carousel-control {
  background: none;
  border: none;
  font-size: 2em;
  cursor: pointer;
  color: darkorange;
}

.carousel-control:hover {
  color: darkorange;
}

.hero-section {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 75vh;
  background-color: #dda758;
}

.hero-section img {
  scale: .75;
}

.hero-background {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
}

.overlay2 {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 20px;
  background-color: rgba(255, 193, 45, 0.8);
  max-width: 600px;
  border-radius: 10px;
}

.overlay2 h1 {
  font-size: 2.5em;
  color: black;
  margin-bottom: 10px;
}

.overlay2 p {
  font-size: 1.2em;
  color: black;
  margin-bottom: 20px;
}




</style>