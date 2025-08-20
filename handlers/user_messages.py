from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram import F

from database.crud.user import UserCrud
from database.core.database import get_db

from database.crud.purchase import PurchaseCrud
from database.schemas.purchase import PurchaseCreate

from states.item import ItemState
from datetime import datetime

from constants import BOT as bot
from config import config

router = Router()
user_crud = UserCrud()
purchase_crud = PurchaseCrud()

@router.message(F.text == "👤Профиль")
async def get_profile(message: Message):
    async for db in get_db():
        user = await user_crud.get_user(db=db, telegram_id=int(message.from_user.id))
    
    if user is None:
        await message.answer("Пользователь не найден. Зарегистрируйтесь через /start")
        return

    text = (
        f"👤 Ваш профиль:\n"
        f"Telegram ID: {user.telegram_id}\n"
        f"Username: @{user.username}\n"
        f"Покупки: {user.purchases}\n"
    )
    await message.answer(text)

@router.message(F.text == "🎈Заказать")
async def create_order(message: Message, state: FSMContext):
    await state.set_state(ItemState.name)
    await message.answer("Введите название товара, который хотите заказать:")

@router.message(ItemState.name)
async def process_item_name(message: Message, state: FSMContext):
    item_name = message.text
    await state.update_data(name=item_name)

    await state.set_state(ItemState.link)
    await message.answer("Введите ссылку на товар (если есть):")

@router.message(ItemState.link)
async def process_item_link(message: Message, state: FSMContext):
    item_link = message.text

    data = await state.get_data()
    item_name = data.get("name")

    purchase_data = PurchaseCreate(
        telegram_id=message.from_user.id,
        link=item_link,
        item_name=item_name,
        created_at=datetime.now()
    )

    async for db in get_db():
        new_purchase = await purchase_crud.add_purchase(
            db=db, purchase_data=purchase_data
        )

    await message.answer("Заказ принят в обработку! Ожидайте ответа от менеджера.")

    for manager_id in config.MANAGER_IDS.split(","):
        await bot.send_message(
            int(manager_id), 
            f"Пользователь @{message.from_user.username} заказал: {item_name} - {item_link}"
        )