<script setup lang="ts">

import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {useBlogStore} from "~/stores/blogStore";
import {ref} from "vue";

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
</script>

<template>
<div class="navbar2">
    <nav class="navigation">
      <NuxtLink to="/blog">Blog</NuxtLink>
      <NuxtLink to="/about">About</NuxtLink>
    </nav>
    <div class="search-bar">
      <input
        type="text"
        v-model="searchQuery"
        @input="searchBlogs"
        placeholder="Search"
      />
      <i class="fa fa-search"></i>
    </div>
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
</template>

<style scoped>
.navbar2 {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  padding-top: 5%;
}

.navigation {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.navigation a {
  text-decoration: none;
  color: black;
  font-weight: bold;
}

.navigation a:hover {
  text-decoration: underline;
}

.search-bar {
  width: 50%;
  border: 1px solid black;
  padding: 5px;
  margin-bottom: 20px;
}

.search-bar input {
  border: none;
  outline: none;
}

.search-bar .fa-search {
  margin-left: 5px;
}

.social-media {
  display: flex;
  gap: 2rem;
}

.social-media a {
  text-decoration: none;
}
.icon-white {
  color: black;
}
</style>