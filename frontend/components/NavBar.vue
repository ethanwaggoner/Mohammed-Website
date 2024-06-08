<script setup lang="ts">


</script>

<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <NuxtLink to="/"><img src="@/assets/logo.png" alt="Logo" /></NuxtLink>
    </div>
    <div class="navbar-menu">
      <ul class="navbar-nav">
        <li class="home-underline" ><NuxtLink to="/">Home</NuxtLink></li>
        <li><NuxtLink to="/about">About</NuxtLink></li>
        <li><NuxtLink to="/blog">Blog</NuxtLink></li>
        <li><NuxtLink to="/media">Media</NuxtLink></li>
        <li><NuxtLink to="/contact">Contact</NuxtLink></li>
      </ul>
      <div class="social-media">
        <a href="https://www.instagram.com/mosnotesofficial/" target="_blank">
          <FontAwesomeIcon class=icon-white :icon="['fab', 'instagram']" />
        </a>
        <a href="https://www.facebook.com/mosnotesofficial" target="_blank">
          <FontAwesomeIcon class=icon-white :icon="['fab', 'facebook']" />
        </a>
        <a href="https://twitter.com/monotesofficial" target="_blank">
          <FontAwesomeIcon class=icon-white :icon="['fab', 'twitter']" />
        </a>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: transparent;
  padding: 1rem;
  margin: 0 5% 0 5%;
}

.navbar-logo img {
  max-height: 150px;
}

.navbar-menu {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.navbar-nav {
  list-style: none;
  display: flex;
  gap: 1rem;
  margin: 0;
  padding: 0;
}

.navbar-nav li a {
  text-decoration: none;
  color: white;
  font-size: 20px;
}

.home-underline {
  color: white;
  text-decoration: underline;
  text-underline-offset: 10px;
}

.social-media {
  display: flex;
  gap: 1rem;
}

.social-media a {
  text-decoration: none;
}

.icon-white {
  color: white;
}

</style>
