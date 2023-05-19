from aiogram import F, Bot, Dispatcher, types
from aiogram.filters import Text, Command

from aiogram.types import BotCommand, BotCommandScopeDefault

import asyncio
import logging

TOKEN = "5828168135:AAHLMf9rjdGf2d8nqmLlzfKBAO7HSgc8JzA"

admin_id = '302594040'

logger = logging.getLogger(__name__)


async def comm(bot: Bot):
    command = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),

    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())


async def start_up(bot: Bot):
    await comm(bot)
    await bot.send_message(admin_id, text='Бот запущен')


async def sd(bot: Bot):
    await bot.send_message(admin_id, text='Бот выключен')


async def echo(message: types.Message):
    print(message.text)
    await message.answer(message.text)


async def text(message: types.Message):
    await message.answer("Ты ввел текст вот такой:" + message.text)


async def on_start(message: types.Message):
    await message.reply("Начинаем работать")


async def hi_admin(message: types.Message):
    await message.reply("Привет, Админ")


async def picture(message: types.Message):
    await message.reply("Да это же картинка!")


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    bots = Bot(TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(sd)
    #

    dp.message.register(on_start, Command(commands='start'))

    # Фильтры
    dp.message.register(picture, F.photo)  # фильтр по картинке
    dp.message.register(hi_admin, F.from_user.id == int(admin_id), F.text == 'Привет')  # фильтр по id пользователя
    dp.message.register(text, Text(text='Салют'))  # фильтр по тексту

    dp.message.register(echo)

    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())