from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_confirm = InlineKeyboardMarkup(inline_keyboard=[
                              [
                                 InlineKeyboardButton(
                                    text='Подвердить',
                                    callback_data='confirm'
                                 ),
                                InlineKeyboardButton(
                                    text='Отменить',
                                    callback_data='cancel'
                                 ),
                                  InlineKeyboardButton(
                                    text='Перейти на сайт',
                                    url = 'https://vk.com'
                                 )
                             ]
                         
                         ]
                            
                         )