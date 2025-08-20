from uuid import UUID
from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from database.schemas.purchase import PurchaseBase

class UserBase(BaseModel):
    telegram_id: int
    username: str

class UserCreate(UserBase): pass

class UserRead(UserBase):
    purchases: Optional[List[PurchaseBase]] = []

    model_config = ConfigDict(from_attributes=True)