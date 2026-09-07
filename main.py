import asyncio
from aiogram import Bot, Dispatcher, Router
from FSM import FSM_router
import os
from dotenv import load_dotenv
from router import router
from Filtres import callback_router
load_dotenv("bot-token.env")
TOKEN = os.getenv("TOKEN")

dp = Dispatcher()

dp.include_router(router)
router.include_router(callback_router)
router.include_router(FSM_router)

async def main():
    bot = Bot(token=TOKEN)

    print ('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠶⣄⣸⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡩⠭⣿⣿⣿⣒⡢
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⢣⠙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣾⣇⣼⡄
⠀⠀⠀⠀⢿⠓⢶⣤⣴⣶⣿⣿⡿⠋⠉⣝⢷⡀
⠀⠀⠀⠀⠈⢿⣿⡟⠁⠀⠮⢿⡇⠀⠀⠀⣸⣧⣒⣒⡒⠤
⠀⠀⠀⠀⢀⣈⣿⣧⡀⠀⠀⣸⣿⣶⣶⣾⣿⣿⠷⠦⣘⠁  Bot its started!
⠀⠀⠀⢊⠥⢒⡺⣿⣿⣶⣾⣿⣿⣿⣿⣿⡿⠃
⠀⠀⠀⢀⠈⠁⠀⠈⢻⣿⣿⣿⣿⡿⠿⠋⠀
⠀⠀⠀⣿⡇⠀⢠⣶⣿⣿⣷⡄
⠀⠀⠀⣿⣧⠀⣿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠈⠛⠿⣿⣿⡿⣿⡿⠿⠀ ''')

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())