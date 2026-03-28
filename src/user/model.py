from datetime import date
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, MappedColumn

from src.database.core import Base


class Sex(str, Enum):
    MALE = "male"
    FEMALE = "female"


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[UUID] = MappedColumn(uuid4(), primary_key=True)
    username: Mapped[str] = MappedColumn(String, nullable=False, unique=True)
    password: Mapped[str] = MappedColumn(String, nullable=False, min_length=8)
    first_name: Mapped[str] = MappedColumn(String, nullable=False, min_length=2)
    middle_name: Mapped[str | None] = MappedColumn(String, nullable=True)
    last_name: Mapped[str] = MappedColumn(String, nullable=False, min_length=2)
    email: Mapped[str | None] = MappedColumn(String, nullable=True)
    phone_number: Mapped[str] = MappedColumn(String, nullable=False)
    city: Mapped[str] = MappedColumn(String, nullable=False)
    sex: Mapped[Sex] = MappedColumn(String, nullable=False)
    birth_date: Mapped[date] = MappedColumn(String, nullable=False)
    languages: Mapped[dict] = MappedColumn(JSONB, nullable=True)
