<script setup lang="ts">

</script>

<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <img src="@/assets/logo.png" alt="Logo" />
    </div>
    <div class="navbar-menu">
      <ul class="navbar-nav">
        <li class="home-underline" ><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/media">Media</a></li>
        <li><a href="/contact">Contact</a></li>
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
      <div class="donate">
        <button>Donate</button>
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

.donate button {
  font-size: 16px;
  background-color: orange;
  border: none;
  padding: 1rem 1.5rem;
  cursor: pointer;
}

</style>
