<script setup lang="ts">
import { reactive } from 'vue'
import axios from 'axios'
import {useNuxtApp} from "#app";

const form = reactive({
  firstName: '',
  lastName: '',
  email: '',
  subject: '',
  message: ''
})
const { $axios } = useNuxtApp();
const submitForm = async () => {
  try {
    const response = await $axios.post('/api/contact/send/', form)
    console.log('Form submitted:', response.data)
    alert('Email sent successfully')
  } catch (error) {
    console.error('Error submitting form:', error)
    alert('There was an error sending your email.')
  }
}
</script>

<template>
  <div class="background">
    <NavBarDark />
    <div class="form-container">
      <div class="contact-form">
        <h1>Contact Me</h1>
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="firstName">Name <span>(required)</span></label>
            <div class="name-inputs">
              <input type="text" id="firstName" v-model="form.firstName" placeholder="First Name" required />
              <input type="text" id="lastName" v-model="form.lastName" placeholder="Last Name" required />
            </div>
          </div>
          <div class="form-group">
            <label for="email">Email <span>(required)</span></label>
            <input type="email" id="email" v-model="form.email" required />
          </div>
          <div class="form-group">
            <label for="subject">Subject <span>(required)</span></label>
            <input type="text" id="subject" v-model="form.subject" required />
          </div>
          <div class="form-group">
            <label for="message">Message <span>(required)</span></label>
            <textarea id="message" v-model="form.message" required></textarea>
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  </div>
  <BottomBar />
</template>

<style scoped>
.background {
  background-color: #fbb03b;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.contact-form {
  background-color: #fbb03b;
  padding: 40px;
  width: 80%;
  max-width: 800px;
  color: #000;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 5px;
}

.name-inputs {
  display: flex;
  gap: 10px;
}

.name-inputs input {
  flex: 1;
}

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

textarea {
  resize: vertical;
  height: 100px;
}

button {
  background-color: #000;
  color: #fbb03b;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  align-self: center;
}

button:hover {
  background-color: #333;
}
</style>
