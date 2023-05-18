# Текстовые кнопки
# one_time_keyboard=True далять клавиатуру после нажатия
# input_field_placheolder= 'Подсказка' текст выводимый вместе с кнопками
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
    keyboard=[
        [
            # Отправить свой номер телефона
            KeyboardButton(text='Кнопка  Отправить свой контакт',request_contact=True),
            # Отправить свою геопозицию
            KeyboardButton(text='Кнопка Отправить геопозицию',request_location=True),
            KeyboardButton(text='Кнопка 3')
        ],
        [
            KeyboardButton(text='Кнопка 5')
        ]
    ]
)