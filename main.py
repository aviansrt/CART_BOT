import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router

# инициализация бота с токеном
bot = Bot(token=TOKEN)
# инициализация диспетчера без аргументов
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")