<script setup lang="ts">
import { ref } from 'vue';
</script>

<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <NuxtLink to="/"><img src="../assets/images/logo.png" alt="Logo" /></NuxtLink>
    </div>
    <div class="navbar-menu">
      <ul class="navbar-nav">
        <li class="home-underline"><NuxtLink to="/">Home</NuxtLink></li>
        <li><NuxtLink to="/about">About</NuxtLink></li>
        <li><NuxtLink to="/blog">Blog</NuxtLink></li>
        <li class="dropdown">
          <a href="#">Media</a>
          <ul class="dropdown-menu">
            <li><NuxtLink to="/media">Media List</NuxtLink></li>
            <li><NuxtLink to="/education">Educational Advocacy</NuxtLink></li>
            <li><NuxtLink to="/research">Research</NuxtLink></li>
          </ul>
        </li>
        <li><NuxtLink to="/contact">Contact</NuxtLink></li>
      </ul>
      <div class="social-media">
        <a href="https://www.instagram.com/mosnotesofficial/" target="_blank">
          <FontAwesomeIcon class="icon-white" :icon="['fab', 'instagram']" />
        </a>
        <a href="https://www.facebook.com/mosnotesofficial" target="_blank">
          <FontAwesomeIcon class="icon-white" :icon="['fab', 'facebook']" />
        </a>
        <a href="https://twitter.com/monotesofficial" target="_blank">
          <FontAwesomeIcon class="icon-white" :icon="['fab', 'twitter']" />
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

.navbar-nav li {
  position: relative;
}

.navbar-nav li a {
  text-decoration: none;
  color: white;
  font-size: 20px;
}

.dropdown:hover .dropdown-menu {
  display: block;
}

.dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  background-color: darkgreen;
  padding: 0.5rem;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  list-style: none;
}

.dropdown-menu li a {
  color: white;
  font-size: 18px;
  padding: 0.5rem 1rem;
  display: block;
  text-decoration: none;
}

.dropdown-menu li a:hover {
  background-color: #007800;
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
