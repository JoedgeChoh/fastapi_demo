#! /usr/bin/env python3

from fastapi import APIRouter
from models.model import Todo

todo_router = APIRouter(
        prefix = '/todo',
        tags = ['todo']
        )
todo_list= []

@todo_router.post('') 
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successful"}

@todo_router.get('')
async def retreive_todos() -> dict:
    return {"todos": todo_list}

@todo_router.get('/')
async def get_default_todo() -> dict:
    if todo_list:
        return {"todo_1": todo_list[0]}
    return {"messsage": "Todo is initial"}

@todo_router.get('/{todo_id}')
async def get_single_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo_item": todo.item}
    return {"message": "Todo with suppied ID doesn't exit."}
