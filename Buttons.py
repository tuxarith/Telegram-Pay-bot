import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command


#-------------------Keyboard Button----------------------

def main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text ='Информация о боте', callback_data = 'info'),
            InlineKeyboardButton(text='Команды', callback_data='commands')
        ],

        [
            InlineKeyboardButton(text='Гитхаб Создателя', web_app=WebAppInfo(url="https://github.com/tuxarith")),
            InlineKeyboardButton(text='Задонатить', callback_data = 'donate')
        ]


    ]
    )

    return keyboard

def github_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Перейти на Гитхаб Создателя', url= 'https://github.com/tuxarith')]
    ]
    )

    return keyboard

def paymenthod_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Задонатить через Trust Wallet (временно недоступно, еще в разработке)", callback_data= 'donate_trust'),
            InlineKeyboardButton(text="Задонатить telegram звездами", callback_data = 'donate_stars')
        ]
    ])
    return keyboard

def want_you_toleave_message_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Да", callback_data='yes'),
            InlineKeyboardButton(text="Нет", callback_data='no')

        ]
    ])

    return keyboard

#--------------------------------------------------------