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
    <div class="research-section">
      <h2>Research</h2>
      <div class="research-cards">
        <div class="card">
          <img src="/assets/images/research1.jpg" alt="Johns Hopkins University" />
          <h3>Johns Hopkins University</h3>
          <a href="#" class="learn-more">Learn more</a>
        </div>
        <div class="card">
          <img src="/assets/images/research2.jpg" alt="University of Pittsburgh" />
          <h3>University of Pittsburgh</h3>
          <a href="#" class="learn-more">Learn more</a>
        </div>
      </div>
    </div>
  </div>
  <BottomBar />
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

.hero-section {
  padding: 2em;
  background-color: white;
  text-align: center;
}

.research-section {
  margin-top: 2em;
  text-align: left;
}

.research-section h2 {
  font-size: 3em;
  margin-left: 1em;
}

.research-cards {
  display: flex;
  justify-content: center;
  gap: 2em;
  flex-wrap: wrap;
}


.card {
  border: 1px solid #ddd;
  padding: 1em;
  width: 400px;
  text-align: center;
}

.card:hover {
   cursor: pointer;
}

.card img {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.card h3 {
  font-size: 1.5em;
  margin: 1em 0;
  text-decoration: underline;
}

.card .learn-more {
  background-color: black;
  color: white;
  padding: 0.5em 1em;
  text-decoration: none;
}
</style>
