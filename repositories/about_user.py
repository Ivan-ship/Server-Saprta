from database.model import User
from sqlalchemy import select
from fastapi import HTTPException

class AboutUser:
    def __init__(self, session):
        self.session = session

    async def about_user(self, tg_id: int):
        stmp = select(User).where(User.id == tg_id)
        res = await self.session.execute(stmp)
        user = res.scalar_one_or_none()
        if user is None:
            raise HTTPException(
                status_code=404,
                detail="Данный пользователь не найден!"
            )
        return {
            "id": user.id,
            "username": user.username
        }
