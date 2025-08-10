from aiogram.fsm.state import State, StatesGroup

class ItemState(StatesGroup):
    price_tg = State()
    type_of_item = State()
    link = State()