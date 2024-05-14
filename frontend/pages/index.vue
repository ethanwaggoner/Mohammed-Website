<script setup>
import NavBar from '@/components/NavBar.vue';


</script>

<template>
  <div class="background-image">
    <NavBar />
    <div class="overlay">
      <h1>Live experiences of one dude's life, relationships, hopes, and faith.</h1>
      <NuxtLink to="/blog"><button>Read Now</button></NuxtLink>
    </div>
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