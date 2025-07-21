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