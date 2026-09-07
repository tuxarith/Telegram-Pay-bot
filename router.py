import asyncio
from aiogram import Dispatcher, Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import message, Message, FSInputFile
from aiogram.types import LabeledPrice
from aiogram.types import PreCheckoutQuery
from Buttons import main_inline_keyboard, github_inline_keyboard, paymenthod_inline_keyboard




router = Router()


@router.message(Command("start"))
async def start(message: Message):
    photo = FSInputFile('photo/stars.jpg')
    await message.answer_photo(photo=photo, caption= f"Привет {message.from_user.full_name}! Можешь задонатить отсюда если хочешь меня поддержать :)", reply_markup=main_inline_keyboard())

@router.message(Command("donate"))
async def donate(message: Message):
    await message.answer("Выберите способ оплаты", reply_markup=paymenthod_inline_keyboard())

@router.message(Command("back"))
async def back_stars(message: Message, bot):
    args = message.text.split()
    paymentid = args[1]
    await bot.refund_star_payment(
        user_id=message.from_user.id,
        telegram_payment_charge_id=paymentid)
    await message.answer("Возращение прошло успешно")

@router.message(Command("info"))
async def info(message: Message):
    photo = FSInputFile('photo/justcat.jpg')

    caption = ("-------ИНФОРМАЦИЯ-------\n\n"
               "Данный бот был сделан tuxarith, воспользуйтесь командой /github - чтобы попасть на гитхаб аккаунт создателя :) ")

    await message.answer_photo(
        photo=photo,
        caption=f"<blockquote>{caption}</blockquote>",
        parse_mode="HTML"
    )

@router.message(Command("github"))
async def github(message: Message):
    photo = FSInputFile('photo/black cat in a field.jpg')
    await message.answer_photo(photo=photo, reply_markup=github_inline_keyboard())

@router.message(Command("commands"))
async def commands(message: Message):
    photo = FSInputFile('photo/kitty.jpg')

    caption = ("✦\n\n----THE COMMANDS----\n\n"
               "/start - запустить бота\n"
               "/info - информация о боте\n"
               "/commands - команды для бота\n"
               "/github - гитхаб создателя :)\n "
               "/donate - задонатить\n\n"
               "                                                                                                               ✦")


    await message.answer_photo(
        photo=photo,
        caption=f"<blockquote>{caption}</blockquote>",
        parse_mode="HTML"
    )












