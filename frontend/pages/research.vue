<script setup lang="ts">

import NavBar from "~/components/NavBar.vue";
</script>

<template>
 <div class="background-image">
    <NavBar />
    <div class="overlay1">
      <h1>“The world is divided into men who have wit and no religion and men who have religion and no wit.”</h1>
      <p><em>- Avicenna (Ibn Sina)</em></p>
    </div>
  </div>
  <div class="hero-section">

  </div>
</template>

<style scoped>
.background-image {
  background-image: url('/images/researchbackground.jpg');
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
  font-size: 4em;
  margin: 10%;
}

p {
  font-size: 1em;
}
</style>