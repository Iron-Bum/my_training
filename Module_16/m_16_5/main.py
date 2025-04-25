from fastapi import FastAPI, Path, status, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="template")

users_db = []


class User(BaseModel):
    user_id: int = None
    username: str
    age: int


@app.get('/')
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users_db})


@app.get(path='/users/{user_id}')
async def get_users(user_id: int, request: Request) -> HTMLResponse:
    try:
        for user in users_db:
            if user.user_id == user_id:
                return templates.TemplateResponse('users.html', {'request': request, 'user': user})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> User:
    if len(users_db):
        new_id = users_db[-1].user_id + 1
    else:
        new_id = 1
    new_user = User(user_id=new_id, username=username, age=age)
    users_db.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def upd_user(user_id: int, username: str, age: int) -> User:
    try:
        for user in users_db:
            if user.user_id == user_id:
                user.username = username
                user.age = age
                return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def del_user(user_id: int) -> User:
    try:
        for index, user in enumerate(users_db):
            if user.user_id == user_id:
                delete_user = users_db.pop(index)
                return delete_user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')
