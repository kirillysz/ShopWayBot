from aiogram import Bot, Dispatcher

from config import config
from asyncio import run

from src.log.logging import _logger
from handlers.user_commands import router as commands_router

from database.core.initial_tables import create_tables

async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(
        commands_router
    )

    await create_tables()
    _logger.info(msg="Таблицы сгенерированы")

    _logger.info(msg="Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main())