from uuid import UUID

from datetime import datetime
from pydantic import BaseModel, ConfigDict

class PurchaseBase(BaseModel):
    name: str
    price: int
    user_id: UUID

class PurchaseCreate(PurchaseBase): pass

class PurchaseRead(PurchaseBase):
    id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
