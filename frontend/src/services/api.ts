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
