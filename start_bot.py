import asyncio
import logging

from aiogram import Dispatcher, Bot

# from filters.filter_admin import Text
from handlers.echo import  register_echo
from handlers.fsm import start_up, sd, register_fsm

TOKEN = "5828168135:AAHLMf9rjdGf2d8nqmLlzfKBAO7HSgc8JzA"

logger = logging.getLogger(__name__)



def handlers(dp):
    register_fsm(dp)
    register_echo(dp)

async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    bots = Bot(TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_up)
    dp.shutdown.register(sd)

    handlers(dp)

    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())