from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Router
from aiogram.types import LabeledPrice, message, Message, FSInputFile


ADMIN_ID = 


class get_stars(StatesGroup):
    stars = State()

class message_for_donating(StatesGroup):
    want_message = State()

FSM_router = Router()




#-------------------------------------------------------------------------------------------------------
@FSM_router.message(get_stars.stars)
async def get_stars1(message: Message, state: FSMContext):
    args = message.text.split()
    amount1 = int(args[0])

    price = [LabeledPrice(label='XTR', amount=amount1)]

    if amount1 < 1:
        await message.answer("Меньше нуля не положенно! Попробуйте вести больше нуля :3")
        return
    elif amount1 > 99999:
        await message.answer("Ты шо богач тута?")
        return
    else:
        await message.answer_invoice(
            title='На покушать :)',
            description=' ',
            prices=price,
            provider_token='',
            payload='by stars',
            photo_url="https://res.cloudinary.com/dtz0urit6/image/upload/q_auto:best,f_jpg/cloudinary-tools-uploads/bk3ftxq2inlafbob2gzf",
            photo_width=736,
            photo_height=276,
            currency='XTR'

        )

    await state.clear()
#-------------------------------------------------------------------------------------------------------

@FSM_router.message(message_for_donating.want_message)
async def fsm_message_for_donating(message: Message, state: FSMContext, bot):
    message_done = message.text
    username_be = message.from_user.username

    if message.from_user.id != ADMIN_ID:
        await bot.send_message(chat_id=ADMIN_ID, text = f'Прикрепленное сообщение!\n\n{message_done}\n\nОт: @{username_be}')


    await message.answer('Ваше сообщение было отправлено!')

    await state.clear()



