import asyncio
import logging

from aiogram import Dispatcher, Bot

from handlers.fsm import start_up, sd, register_fsm

TOKEN = "5828168135:AAHLMf9rjdGf2d8nqmLlzfKBAO7HSgc8JzA"

logger = logging.getLogger(__name__)

def handlers(dp):
    register_fsm(dp)

async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    bots = Bot(TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(sd)

    handlers(dp)

    try:
        await dp.start_polling(bots)
    except:
        pass


if __name__ == '__main__':
    try:
        asyncio.run(start())
    except:
        pass