export interface Todo {
  id: number;
  task: string;
  completed: boolean;
}

export async function fetchTodos(): Promise<Todo[]> {
  const res = await fetch('http://localhost:8000/todos')
  if (!res.ok) throw new Error('Error fetching todos')
  return res.json()
}

export async function updateTodo(todoId: number): Promise<Todo> {
  const res = await fetch(`http://localhost:8000/todos/${todoId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
  })
  if (!res.ok) throw new Error('Error updating todo')
  return res.json()
}
