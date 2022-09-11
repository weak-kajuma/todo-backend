from typing import Optional

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: Optional[str] = Field(None, example="Donald")
    email: Optional[str] = Field(None, example="donald@example.com")
    password: Optional[str] = Field(None, example="password")


class UserCreate(UserBase):
    pass


class UserCreateResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
