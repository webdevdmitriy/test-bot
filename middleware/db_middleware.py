from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Awaitable, Callable, Dict, TypeVar

from other.db_connect import Request


class DbSession(BaseMiddleware):
    def __init__(self, connector):
        self.connector = connector

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        async with self.connector.connection() as connect:
            data['request'] = Request(connect)
            return await handler(event, data)
      