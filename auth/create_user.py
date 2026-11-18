from fastapi import APIRouter, Depends
from repositories.create_user import CreateUser
from database.shema import User
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_session

router = APIRouter()

@router.post("/create-user")
async def create_user(tg_user: User, session: AsyncSession = Depends(get_session)):
    repository = CreateUser(session)
    user = await repository.create_user(tg_user)
    return {
        "message": "Успешная пегистрация",
        "user_id": user.id
    }