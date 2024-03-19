<script setup lang="ts">

</script>

<template>
  <nav class="navbar">
    <ul class="navbar-nav">
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/media">Media</a></li>
      <li><a href="/contact">Contact</a></li>
    </ul>
    <div class="social-media">
      <a href="https://instagram.com" target="_blank">Instagram Icon</a>
      <a href="https://facebook.com" target="_blank">Facebook Icon</a>
      <a href="https://twitter.com" target="_blank">Twitter Icon</a>
    </div>
    <div class="donate">
      <button>Donate</button>
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

.navbar-nav {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.navbar-nav li a {
  text-decoration: none;
  color: #000;
}

.social-media {
  display: flex;
  gap: 1rem;
}

.social-media a {
  text-decoration: none;
}

.donate button {
  background-color: orange;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
}

</style>
