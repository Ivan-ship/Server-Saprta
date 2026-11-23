from fastapi import FastAPI
from sqlalchemy import text
from database.db import async_engine
from auth.create_user import router as create_user
from src.about_account import router as about_account

app = FastAPI()
app.include_router(create_user)
app.include_router(about_account)

@app.get("/")
def root():
    return {"Hello world!"}