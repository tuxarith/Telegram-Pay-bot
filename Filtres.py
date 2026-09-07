import asyncio
from aiogram.types import CallbackQuery
from aiogram import F
from aiogram.types import message, Message, FSInputFile
from Buttons import main_inline_keyboard, github_inline_keyboard, paymenthod_inline_keyboard, want_you_toleave_message_inline_keyboard
from aiogram import Router
from aiogram.types import LabeledPrice
from aiogram.types import PreCheckoutQuery
from FSM import get_stars, message_for_donating
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from FSM import get_stars1
ADMIN_ID = 8437409579
callback_router = Router()


#-------------------------------------------------------------------------------------------------------

                               #For Commands
@callback_router.callback_query(lambda c: c.data == 'commands')
async def get_callback_commands(callback):
    photo = FSInputFile('photo/kitty.jpg')
    caption = ("✦\n\n----THE COMMANDS----\n\n"
               "/start - запустить бота\n"
               "/info - информация о боте\n"
               "/commands - команды для бота\n"
               "/github - гитхаб создателя :)\n "
               "/donate - задонатить\n\n"
               "                                                                                                               ✦")

    await callback.message.answer_photo(
        photo=photo,
        caption=f"<blockquote>{caption}</blockquote>",
        parse_mode="HTML"
    )
    await callback.answer()


@callback_router.callback_query(lambda c: c.data == 'info')
async def get_callback_info(callback):
    photo = FSInputFile('photo/justcat.jpg')

    caption= ("-------ИНФОРМАЦИЯ-------\n\n"
                         "Данный бот был сделан tuxarith, воспользуйтесь командой /github - чтобы попасть на гитхаб аккаунт создателя :) ")

    await callback.message.answer_photo(
        photo=photo,
        caption=f"<blockquote>{caption}</blockquote>",
        parse_mode="HTML"
    )

    await callback.answer()
#-------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------
@callback_router.callback_query(lambda c: c.data == 'donate')
async def get_callback_donate(callback):

    await callback.message.answer("Выберите способ оплаты", reply_markup=paymenthod_inline_keyboard())


    await callback.answer()
#-------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------
                             #For Star and trust
@callback_router.callback_query(lambda c: c.data == 'donate_stars')
async def get_callback_donate_stars(callback, state: FSMContext):
    await state.set_state(get_stars.stars)
    await callback.message.answer("Скинь скока хочешь задонить")

    await callback.answer()

@callback_router.callback_query(lambda c: c.data == 'donate_trust')
async def get_callback_donate_trust(callback, state: FSMContext):
    await callback.message.answer('Упссс! Этот способ оплаты еще дорабатывается, подождите всего лишь немножка :3')
    await callback.answer()

#-------------------------------------------------------------------------------------------------------

@callback_router.callback_query(lambda c: c.data == 'yes')
async def get_callback_yes(callback, state: FSMContext):
    await state.set_state(message_for_donating.want_message)
    await callback.message.answer('Хорошо, тогда напишите что-нибудь')
    await callback.answer()

@callback_router.callback_query(lambda c: c.data == 'no')
async def get_callback_no(callback, state: FSMContext):

    await callback.message.answer('Хорошо, на этом все')
    await callback.answer()


#-------------------------------------------------------------------------------------------------------
                         #Checkout and successful
@callback_router.pre_checkout_query()
async def pre_checkout(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)





@callback_router.message(F.successful_payment)
async def successfull_payment(message: Message, bot, state: FSMContext):
    photo = FSInputFile('photo/Meanwhile _..jpg')
    username_be = message.from_user.username
    username_nikname = message.from_user.first_name
    username_id = message.from_user.id

    payment = message.successful_payment
    payment_id = payment.telegram_payment_charge_id

    amount = payment.total_amount
    photo_for_admin = FSInputFile('photo/photo_for_admin.png')







    await message.answer_photo(photo=photo, caption=f'Ваш айди оплаты: {payment_id}')
    await message.answer('Хотите внести предложение к оплате?', reply_markup=want_you_toleave_message_inline_keyboard())

    if message.from_user.id != ADMIN_ID:
     await bot.send_photo(chat_id=ADMIN_ID, photo=photo_for_admin, caption=f'💰 Тебе пришел донат!\n\n'
                                                                                 f'ID: {username_id}\n'
                                                                                 f'Username: @{username_be}\n'
                                                                                 f'Nikname: {username_nikname}\n'
                                                                                 f'⭐ Stars: {amount}\n'

                                )
















