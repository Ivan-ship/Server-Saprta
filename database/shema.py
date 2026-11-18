from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    language_code: str | None = None

class Subscribe(BaseModel):
    sub_id : int
    start_date: date
    end_date: date
    url: str
    id: int
    price: int
    plan: str