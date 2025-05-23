from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    adress = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(text='calories')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_weight(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост.')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_growth(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Введите свой вес.')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def send_calories(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    call = 10 * int(data["growth"]) + 6.25 * int(data["weight"]) - 5 * int(data["age"])
    await message.answer(f'Ваше суточное потребление калорий равно {call}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
