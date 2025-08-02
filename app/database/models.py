from datetime import datetime
from typing import Optional
from enum import Enum
from sqlmodel import SQLModel, Field


class Language(str, Enum):
    ENGLISH = "en"
    RUSSIAN = "ru"


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    first_name: str = Field()
    last_name: Optional[str] = Field(default=None)
    username: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.now)
    last_activity: datetime = Field(default_factory=datetime.now)
    language: Language = Field(default=Language.ENGLISH)
    preferences: str = Field(default="")
    is_premium: bool = Field(default=False)
    is_admin: bool = Field(default=False)
