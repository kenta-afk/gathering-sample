from fastapi import APIRouter, Depends, HTTPException
from ..models.todo import Todos, Todo
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..dependencies import get_db
import logging

logger = logging.getLogger(__name__)  # main.pyの設定を継承

todo_router = APIRouter()

@todo_router.get("/todos")
async def get_todos(db: AsyncSession = Depends(get_db), response_model=Todos):
    result = await db.execute(select(Todo))
    if result is None:
        logger.info("No Todos found")
        raise HTTPException(status_code=404, detail="Todos not found")
    
    todos: Todos = result.scalars().all()

    return todos

@todo_router.patch("/todos/{todo_id}")
async def toggle_todo_completed(todo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo).where(Todo.id == todo_id))
    todo = result.scalar_one_or_none()
    
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # completedの状態を反転
    todo.completed = not todo.completed
    await db.commit()
    
    return todo