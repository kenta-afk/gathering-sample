from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(255), nullable=False)
    completed = Column(Boolean, default=False)

class Todos():
    todos: list[Todo]