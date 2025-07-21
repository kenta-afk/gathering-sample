<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { fetchTodos, type Todo } from '../services/api';

const todos = reactive<Todo[]>([]);

onMounted(async () => {
  todos.push(...(await fetchTodos()));
});
</script>

<template>
    <h1>Todo List</h1>
    <ul>
        <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" v-model="todo.completed" />
        {{ todo.task }}
        </li>
    </ul>
</template>
