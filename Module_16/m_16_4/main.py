from fastapi import FastAPI, Path, status, Body, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

users = []

app = FastAPI()


class User(BaseModel):
    user_id: int = None
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> User:
    if len(users):
        new_id = users[-1].user_id + 1
    else:
        new_id = 1
    new_user = User(user_id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def upd_user(user_id: int, username: str, age: int) -> User:
    try:
        for user in users:
            if user.user_id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def del_user(user_id: int) -> User:
    try:
        for index, user in enumerate(users):
            if user.user_id == user_id:
                delete_user = users.pop(index)
                return delete_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
