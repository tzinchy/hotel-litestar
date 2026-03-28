from dataclasses import dataclass
from datetime import date, datetime
from enum import StrEnum
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, MappedColumn

from src.database.core import Base


class Sex(StrEnum):
    MALE = "male"
    FEMALE = "female"


class UserStatus(StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    BANNED = "banned"
    INVITED = "invited"


class CardStatus(StrEnum):
    USER_SET = "user_set"
    MANAGER_VERIFYED = "manager_verifyed"
    MANAGER_DECLINED = "manager_declined"


@dataclass
class MedCard:
    status: CardStatus
    created_at: date
    updated_at: datetime


class MedCartType(StrEnum):
    BASE = "base"
    FOOD = "food"


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[UUID] = MappedColumn(PG_UUID, primary_key=True)
    username: Mapped[str] = MappedColumn(String, nullable=False, unique=True)
    password: Mapped[str] = MappedColumn(String, nullable=False)
    first_name: Mapped[str] = MappedColumn(String, nullable=False)
    middle_name: Mapped[str | None] = MappedColumn(String, nullable=True)
    last_name: Mapped[str] = MappedColumn(String, nullable=False)
    email: Mapped[str | None] = MappedColumn(String, nullable=True)
    phone_number: Mapped[str] = MappedColumn(String, nullable=False)
    city: Mapped[str] = MappedColumn(String, nullable=False)
    sex: Mapped[Sex] = MappedColumn(String, nullable=False)
    birth_date: Mapped[date] = MappedColumn(String, nullable=False)
    account_status: Mapped[UserStatus] = MappedColumn(
        String, nullable=False, default="active"
    )
    languages: Mapped[dict] = MappedColumn(JSONB, nullable=True)
    med_cars: Mapped[dict[MedCartType, MedCard]] = MappedColumn(JSONB, nullable=False)
