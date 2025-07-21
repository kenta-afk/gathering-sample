<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink> | 
    <RouterLink to="/todo">Todo</RouterLink>
  </nav>
  <RouterView /> 
</template>

<style scoped>
nav {
  margin: 20px 0;
}

nav a {
  margin: 0 10px;
  text-decoration: none;
  color: #42b883;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

nav a.router-link-active {
  color: #ff6b6b;
}
</style>
