from fastapi import FastAPI, Depends, APIRouter
from mysql.connector import cursor
from routers.db import get_db
import json


# app = FastAPI()
db_router = APIRouter(
        prefix = "/users",
        tags = ["users"])

# def get_db(db: cursor.MySQLCursor = Depends(get_db)):
#     return db

@db_router.get("")
async def get_users(db: cursor.MySQLCursor = Depends(get_db)):
    
    query = "SELECT * FROM users"
    db.execute(query)
    result = db.fetchall()
    if result:
        return {"users": result}
    else:
        return {"error": "User not found"}
    
@db_router.get("/{user_id}")
async def get_user(user_id: int,
                   db: cursor.MySQLCursor = Depends(get_db)):
    query = "SELECT * FROM users WHERE id = %s"
    db.execute(query, (user_id,))
    result = db.fetchall()
    if result:
        return {"user_id": result[0][0], "username": result[0][1]}
    else:
        return {"error": "User not found"}
    
@db_router.get("/user_name/{user_name}")
async def insert_user(user_name: str,
                      db: cursor.MySQLCursor = Depends(get_db)):
    query = "INSERT INTO users (name) VALUES (%s)"
    db.execute(query, (user_name,))
    result = db.fetchone()
    db.execute("COMMIT")
    return {"user_name": user_name}

