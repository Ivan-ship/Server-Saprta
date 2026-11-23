from fastapi import APIRouter, Depends
from repositories.about_user import AboutUser
from database.shema import User
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_session

router = APIRouter()

@router.get("/users/{tg_id}")
async def about_account(tg_id: int, session: AsyncSession = Depends(get_session)):
    repository = AboutUser(session)
    user = await repository.about_user(tg_id)
    return user