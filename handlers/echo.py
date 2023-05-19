from aiogram import F, Bot, Dispatcher, types

from filters.filter_admin import Admin


async def echo(message: types.Message):
    print(message.text)
    await message.answer(message.text)

async def hi_admin(message: types.Message):
    await message.answer("Здравствуй, админ!")

def register_echo(dp: Dispatcher):
    # кастомный фильтр
    dp.message.register(hi_admin, Admin())

