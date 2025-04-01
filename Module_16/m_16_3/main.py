from fastapi import FastAPI, Path
from typing import Annotated

users = {'1': 'Имя: Сергей, возраст: 40'}

app = FastAPI()


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int):
    max_key = max(users.keys())
    new_key = int(max_key) + 1
    users[str(new_key)] = f'Имя: {username}, возраст: {age}'
    return {'message': f'User {new_key} is registered'}


@app.put('/user/{user_id}/{username}/{age}')
async def upd_user(user_id: str, username: str, age: int):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {'message': f'User {user_id} has been updated'}


@app.delete('/user/{user_id}')
async def del_user(user_id: str):
    del users[user_id]
    return {'message': f'User {user_id} has been deleted'}
