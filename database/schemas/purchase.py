from uuid import UUID

from datetime import datetime
from pydantic import BaseModel, ConfigDict

class PurchaseBase(BaseModel):
    item_name: str
    telegram_id: int

class PurchaseCreate(PurchaseBase): 
    created_at: datetime
    link: str

class PurchaseRead(PurchaseBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
