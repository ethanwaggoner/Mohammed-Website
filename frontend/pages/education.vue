<script setup lang="ts">
import NavBarDark from "~/components/NavBarDark.vue";
import image1 from '@/assets/images/education1.png';
import image2 from '@/assets/images/education2.png';
import image3 from '@/assets/images/education3.png';
import image4 from '@/assets/images/education4.png';
import image5 from '@/assets/images/education5.png';
import image6 from '@/assets/images/education6.png';
</script>

<template>
  <NavBarDark />
  <div class="content">
    <p>
      In September 2019, I was <span class="underline">selected</span> from nearly 100 applicants by a review board (made up of experts and advocates from across the education industry) as one of 10 student leaders around the United States for OpenStax National Student Internship Program. In this role, I have advocated on behalf of first-generation students to promote open pedagogy and revitalize campus open educational resource policy.
    </p>
    <p>
      Here are some of the highlights from my service:
    </p>
  </div>
  <div class="image-gallery">
    <div class="gallery-item">
      <img :src="image1" alt="Description 1" />
      <div class="overlay">
        <p>Description for Image 1</p>
      </div>
    </div>
    <div class="gallery-item">
      <img :src="image2" alt="Description 2" />
      <div class="overlay">
        <p>Description for Image 2</p>
      </div>
    </div>
    <div class="gallery-item">
      <img :src="image3" alt="Description 3" />
      <div class="overlay">
        <p>Description for Image 3</p>
      </div>
    </div>
    <div class="gallery-item">
      <img :src="image4" alt="Description 4" />
      <div class="overlay">
        <p>Description for Image 4</p>
      </div>
    </div>
    <div class="gallery-item">
      <img :src="image5" alt="Description 5" />
      <div class="overlay">
        <p>Description for Image 5</p>
      </div>
    </div>
    <div class="gallery-item">
      <img :src="image6" alt="Description 6" />
      <div class="overlay">
        <p>Description for Image 6</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.content {
  margin: 2em auto;
  padding: 2em;
  max-width: 800px;
  text-align: center;
  font-family: 'Times New Roman', Times, serif;
  font-size: 1.2em;
  line-height: 1.6;
}

.underline {
  text-decoration: underline;
}

.image-gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1em;
  padding: 2em;
  justify-items: center;
}

.gallery-item {
  position: relative;
  width: 300px;
  height: 200px;
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: opacity 0.3s;
}

.gallery-item:hover img {
  opacity: 0.1;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  opacity: 0;
  transition: opacity 0.3s;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 1em;
}

.gallery-item:hover .overlay {
  opacity: 1;
}
</style>
