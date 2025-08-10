from aiogram import Bot, Dispatcher
from config import token
from app.handlers import router
import asyncio

TOKEN = token

bot = Bot(token=TOKEN)

dp = Dispatcher()

dp.include_router(router)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print('Бот завершил работу')
