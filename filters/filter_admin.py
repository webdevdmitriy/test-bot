from aiogram.filters import BaseFilter
from aiogram.types import Message


# кастомный фильтр
class Admin(BaseFilter):
    async def __call__(self, message: Message):
        return message.from_user.id == 302594040 or 907499115
