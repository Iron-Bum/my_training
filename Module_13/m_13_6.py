from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ''

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

rkb = ReplyKeyboardMarkup(resize_keyboard=True)
btn_rkb_1 = KeyboardButton(text='Расчитать')
btn_rkb_2 = KeyboardButton(text='Информация')
rkb.add(btn_rkb_1)
rkb.add(btn_rkb_2)


ikb = InlineKeyboardMarkup(resize_keyboard=True)
btn_ikb_1 = InlineKeyboardButton(text='Расчитать норму калорий', callback_data='calories')
btn_ikb_2 = InlineKeyboardButton(text='Формула расчёта', callback_data='formula')
ikb.add(btn_ikb_1)
ikb.add(btn_ikb_2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=rkb)


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выберите опцию: ', reply_markup=ikb)


@dp.callback_query_handler(text='formula')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г)')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст.')
    await UserState.age.set()
    await call.answer()


@dp.message_handler()
async def hi(message):
    await message.answer('Введите команду /start, что бы начть общение')


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
