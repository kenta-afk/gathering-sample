<script setup lang="ts">
import { onMounted, reactive } from 'vue';
import { fetchTodos, updateTodo, type Todo } from '../services/api';

const todos = reactive<Todo[]>([]);

const handleToggle = async (todo: Todo) => {
  try {
    const updatedTodo = await updateTodo(todo.id);
    // ローカルの状態を更新
    const index = todos.findIndex(t => t.id === todo.id);
    if (index !== -1) {
      todos[index] = updatedTodo;
    }
  } catch (error) {
    console.error('Failed to toggle todo:', error);
    // エラーが発生した場合、元の状態に戻す
    todo.completed = !todo.completed;
  }
};

onMounted(async () => {
  todos.push(...(await fetchTodos()));
});
</script>

<template>
    <h1>Todo List</h1>
    <ul>
        <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" v-model="todo.completed" @change="handleToggle(todo)" />
        {{ todo.task }}
        </li>
    </ul>
</template>
