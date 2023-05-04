from aiogram import Bot, Dispatcher, types
import asyncio
import logging

TOKEN = "5828168135:AAHLMf9rjdGf2d8nqmLlzfKBAO7HSgc8JzA"


admin_id = '302594040'

logger = logging.getLogger(__name__)

async def start_up(bot: Bot):
    await bot.send_message(admin_id, text = 'Бот запущен')

async def sd(bot: Bot):
    await bot.send_message(admin_id, text = 'Бот выключен')


async def echo(message: types.Message):
    print(message.text)
    await message.answer(message.text)

async def start():
    logging.basicConfig(
        level = logging.INFO
    )
    bots = Bot(TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(sd)

    dp.message.register(echo)
    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())