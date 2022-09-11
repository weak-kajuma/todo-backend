from fastapi import APIRouter, Depends
from typing import List
import api.schemas.user as user_schema
from sqlalchemy.ext.asyncio import AsyncSession
import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()


@router.get("/users", response_model=List[user_schema.User])
async def list_users():
    return [user_schema.User(id=1, name="kazuma")]


@router.post("/tasks", response_model=user_schema.UserCreateResponse)
async def create_task(
    task_body: user_schema.UserCreate, db: AsyncSession = Depends(get_db)
):
    return await task_crud.create_task(db, task_body)


@router.put("/users/{user_id}", response_model=user_schema.UserCreateResponse)
async def update_user(user_id: int, user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=user_id, **user_body.dict())


@router.delete("/users/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return