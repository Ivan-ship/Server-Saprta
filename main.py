from fastapi import FastAPI
from sqlalchemy import text
from database.db import async_engine
from auth.create_user import router as create_user

app = FastAPI()
app.include_router(create_user)

@app.get("/")
def root():
    return {"Hello world!"}