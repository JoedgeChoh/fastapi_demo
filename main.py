#!/usr/bin/env python3

from fastapi import FastAPI
from routers import add_router, todo_router, db_router

app = FastAPI()
app.include_router(add_router.router)
app.include_router(todo_router.todo_router)
app.include_router(db_router.db_router)
@app.get('/')
async def welcome() -> dict:
    return  {"message": "welcome to my Page"}

# @app.get('/add/numbers')
# async def add_number():
#     return {"massage": "we are adding numbers"}
# 
# @app.get('/add/strings')
# async def add_string():
#     return {"message": "we are adding strings"}
