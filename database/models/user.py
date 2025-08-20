from typing import List, Optional
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import String, BigInteger

from database.core.database import Base

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)

    purchases: Mapped[List["Purchase"]] = relationship(
        "Purchase",
        primaryjoin="User.telegram_id==foreign(Purchase.telegram_id)",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    