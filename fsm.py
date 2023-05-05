
import logging
from aiogram import F, Bot, Dispatcher, types
from aiogram.filters import Text, Command
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup



from aiogram.types import BotCommand, BotCommandScopeDefault


import asyncio



class States(StatesGroup):
    first_name = State()
    last_name = State()
    telephone = State()
    complete = State()


TOKEN = "5828168135:AAHLMf9rjdGf2d8nqmLlzfKBAO7HSgc8JzA"
admin_id = '302594040'

logger = logging.getLogger(__name__)


async def comm(bot: Bot):
    command = [
        BotCommand(
            command = 'start',
            description = 'Начало работы'
        ),
        BotCommand(
            command = 'help',
            description = 'Помощь'
        ),

    ]

    await bot.set_my_commands(command, BotCommandScopeDefault())

async def start_up(bot: Bot):
    await comm(bot)
    await bot.send_message(admin_id, text = 'Бот запущен')

async def sd(bot: Bot):
    await bot.send_message(admin_id, text = 'Бот выключен')


async def on_start(message: types.Message, state: FSMContext):
    await message.answer("Введите необходимые данные. \nВведите имя")
    await state.set_state(States.first_name)

async def first_name(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели имя: " + message.text + '\nВведите фамилию')
    await state.update_data(first_name=message.text)
    await state.set_state(States.last_name)

async def last_name(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели фамилию: " + message.text + '\nВведите телефон')
    await state.update_data(last_name=message.text)
    await state.set_state(States.telephone)

async def teplehone(message: types.Message, state: FSMContext):
    await message.answer("Вы ввели телефон: " + message.text)
    await state.set_state(States.complete)
    await state.update_data(telephone=message.text)

    data = await state.get_data()
    await message.answer('Введенные данные: \n'
                         f"Имя - {data['first_name']} \n"
                         f"Фамилий - {data['last_name']} \n"
                         f"Телефон - {data['telephone']} \n"
                         f"Подтвердите или отмените"

                         )

async def complete(message: types.Message, state: FSMContext):
    await message.answer('Данные приняты')
    await state.clear()

async def cancel(message: types.Message, state: FSMContext):
    await message.answer('Данные отклонены. Введите новые данные')
    await state.clear()

async def start():
    logging.basicConfig(
        level = logging.INFO
    )
    bots = Bot(TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(sd)
 

    dp.message.register(cancel, Text(text='cancel', ignore_case =True))
    dp.message.register(on_start, Command(commands='start'))
    dp.message.register(first_name, States.first_name)
    dp.message.register(last_name, States.last_name)
    dp.message.register(teplehone, States.telephone)
    dp.message.register(complete, States.complete, Text(text='finish', ignore_case =True))



    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())
