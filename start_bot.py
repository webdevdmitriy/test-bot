import asyncio
import logging

from aiogram import Dispatcher, Bot
import psycopg_pool

# from filters.filter_admin import Text
from handlers.echo import  register_echo
from handlers.fsm import start_up, sd, register_fsm
from middleware.db_middleware import DbSession

TOKEN = "5828168135:AAHLMf9rjdGf2d8nqmLlzfKBAO7HSgc8JzA"

# Для psycopg.pool, чтобы не было ошибок
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

logger = logging.getLogger(__name__)

def handlers(dp):
    register_fsm(dp)
    register_echo(dp)



# Подключение к БД Postagre
async def create_pool(user, password, database, host):
    return psycopg_pool.AsyncConnectionPool(f"host={host} port=5432 dbname={database} user={user} password={password} connect_timeout=10")


async def start():
    logging.basicConfig(
        level=logging.INFO
    )
    bots = Bot(TOKEN)
    dp = Dispatcher()

    pooling = await create_pool('postgres', '12345', 'users', '127.0.0.1')

     # Middleware
    dp.message.middleware(DbSession(pooling))

    dp.startup.register(start_up)
    dp.shutdown.register(sd)

    handlers(dp)

    await dp.start_polling(bots)


if __name__ == '__main__':
    asyncio.run(start())