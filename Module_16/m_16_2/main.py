from fastapi import FastAPI, Path
from typing import Annotated # облегчает работу с валидацией данных, особенно когда есть не именованные параметры

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Добро пожаловать'}


@app.get('/user/admin')
async def admin():
    return {'message': 'Вы вошли как админ'}


@app.get('/user/{user_id}')
async def id_users(user_id: int = Path(ge=1, le=100, description="Enter User ID")):
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/{username}/{age}')
async def user_log(
        username: Annotated[str, Path(
            min_length=5, max_length=20, description="Enter username"
        )],
        age: int = Path(
            ge=18, le=120, description="Enter age"
        )
):
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

