// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@pinia/nuxt"],
  plugins: [
      "~/plugins/fontawesome.js",
      "~/plugins/axios.js",
  ],
  css: ['@/assets/main.css'],
    ssr: true,
});