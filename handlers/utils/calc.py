from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram import Router
from aiogram import F

from states.calc import CalcState

from src.parse.pairs import parse_kzt_to_rub

router = Router()

@router.message(F.text == "💰Калькулятор")
async def handle_calc(message: Message, state: FSMContext):
    await message.answer("Сейчас посчитаем... Напишите цену товара в КЗТ")

    await state.set_state(CalcState.price_tg)

@router.message(CalcState.price_tg)
async def return_calc(message: Message, state: FSMContext):
    try:
        price = float(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число.")
        return
    
    await state.update_data(price_tg=price)
    pair_price = await parse_kzt_to_rub()

    price_no_return_kzt = int(price + (price * 0.1))
    price_with_return_kzt = int(price + (price * 0.2))

    price_no_return = round(price_no_return_kzt * pair_price, 2)
    price_with_return = round(price_with_return_kzt * pair_price, 2)

    await message.answer(
        f"Итоговая цена (без возврата) = {price_no_return}Р ({price_no_return_kzt}КЗТ)\n"
        f"Итоговая цена (с возвратом) = {price_with_return}Р ({price_with_return_kzt}КЗТ)"
    )

    await state.clear()
