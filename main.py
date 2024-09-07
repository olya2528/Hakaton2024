import asyncio
from aiogram import Bot, Dispatcher
from handlers import main_menu, feedback, help, transcribe, history



import logging

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    bot = Bot(token = "7522994279:AAEA7DF6lB-JsbP-L4uGgf0hFpIkPIyFT4U")
    dp = Dispatcher()
    dp.include_router(main_menu.router)
    dp.include_router(feedback.router)
    dp.include_router(help.router)
    dp.include_router(history.router)
    dp.include_router(transcribe.router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
