import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from config import TOKEN

from handlers import start, menu, specialties, test

# ===== НАСТРОЙКА ПРОКСИ =====
PROXY_HOST = "45.59.117.163"
PROXY_PORT = 8080
PROXY_LOGIN = ""
PROXY_PASSWORD = ""
PROXY_TYPE = "socks5"

dp = Dispatcher()

def register_all_handlers():
    start.register_handlers(dp)
    menu.register_handlers(dp)
    specialties.register_handlers(dp)
    test.register_handlers(dp)

async def main():
    session = AiohttpSession()
    bot = Bot(token=TOKEN, session=session)
    print("🔌 Без прокси")

    register_all_handlers()
    print("✅ Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())