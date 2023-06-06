import types

from aiogram import F, Bot, Dispatcher, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import BotCommand, CallbackQuery, BotCommandScopeDefault
from aiogram.filters import Text, Command



from keyboards.inline import kb_confirm
from other.db_connect import Request



class States(StatesGroup):
    first_name = State()
    last_name = State()
    telephone = State()
    complete = State()

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

admin_id = '302594040'

async def start_up(bot: Bot):
    await comm(bot)
    await bot.send_message(admin_id, text = 'Бот запущен')

async def sd(bot: Bot):
    await bot.send_message(admin_id, text = 'Бот выключен')


async def on_start(message: types.Message, state: FSMContext, request: Request):
    await message.answer("Введите необходимые данные. \nВведите имя")
    await request.add_user(message)
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
                         f"Подтвердите или отмените",
                        # Инлайн кнопки
                         reply_markup=kb_confirm
    )

async def confirm(call: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None) # Скрытие инлайн кнопок
    await bot.answer_callback_query(call.id, 'Подтвердили данные', show_alert=True)
    await call.answer('Данные приняты')
    await state.clear()

async def cancel(call: CallbackQuery, state: FSMContext):
    await call.answer('Данные отклонены. Введите новые данные!')
    await state.clear()



def register_fsm(dp: Dispatcher):
    dp.message.register(on_start, Command(commands='start'))
    dp.message.register(first_name, States.first_name)
    dp.message.register(last_name, States.last_name)
    dp.message.register(teplehone, States.telephone)

    # Инлайн кнопки
    dp.callback_query.register(confirm, States.complete, F.data == 'confirm')
    dp.callback_query.register(cancel, States.complete, F.data == 'cancel')
