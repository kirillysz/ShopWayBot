from aiogram.fsm.state import State, StatesGroup

class CalcState(StatesGroup):
    price_tg = State()