from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

from keyboards.reply import menu_kb

router = Router()

@router.message(CommandStart())
async def greeting(message: Message):
    sticker_id = "CAACAgIAAxkBAAEPB9toh4g6h5H3AAFkWPF8NERoLOsx4K8AAgEBAAJWnb0KIr6fDrjC5jQ2BA"
    await message.answer_sticker(sticker=sticker_id)

    await message.answer(
        """*Добро пожаловать в ShopWay!*
Мы помогаем покупать и доставлять товары из *Казахстана* прямо в ваши руки — быстро, безопасно и по честным ценам.

📦 Что мы можем для вас сделать:
    1. Найти и выкупить товар по вашей заявке
    2. Организовать доставку до вашего города
    3. Проконсультировать по ценам и наличию""",
parse_mode="Markdown",
reply_markup=menu_kb)
