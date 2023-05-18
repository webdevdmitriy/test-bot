import logging
from aiogram import F, Bot, Dispatcher, types
from aiogram.filters import Text, Command
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.types import BotCommand, BotCommandScopeDefault, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, \
    KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

import asyncio

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


# Текстовые кнопки
# one_time_keyboard=True далять клавиатуру после нажатия
# input_field_placheolder= 'Подсказка' текст выводимый вместе с кнопками
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                               keyboard=[
                                   [
                                       # Отправить свой номер телефона
                                       KeyboardButton(text='Кнопка  Отправить свой контакт', request_contact=True),
                                       # Отправить свою геопозицию
                                       KeyboardButton(text='Кнопка Отправить геопозицию', request_location=True),
                                       KeyboardButton(text='Кнопка 3')
                                   ],
                                   [
                                       KeyboardButton(text='Кнопка 5')
                                   ]
                               ]
                               )


async def on_start(message: types.Message, state: FSMContext):
    await message.answer("Вот такие кнопочки", reply_markup=keyboard)


async def text_button(message: types.Message, state: FSMContext):
    await message.answer("Нажата " + message.text)


# Удаление кнопок
async def del_button(message: types.Message, state: FSMContext):
    await message.answer("Убираю кнопки", reply_markup=ReplyKeyboardRemove)


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    bots = Bot(TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(sd)

    dp.message.register(del_button, F.text == 'del')
    dp.message.register(text_button, F.text.startswith('Кнопка'))
    dp.message.register(on_start, Command(commands='start'))

    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())