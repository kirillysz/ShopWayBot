from aiogram import Bot, Dispatcher
from config import config

BOT = Bot(token=config.BOT_TOKEN)
DP = Dispatcher()