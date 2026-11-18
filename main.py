from fastapi import FastAPI
from sqlalchemy import text
from database.db import async_engine

app = FastAPI()

@app.get("/")
def main():
    return{"Hello": "World"}

#database version
@app.get("/db-check")
async def db_checked():
    async with async_engine.connect() as connection:
        result = await connection.execute(
            text("SELECT version();")
        )
        version = result.scalar()
    return{
        "status" : "connect",
        "database_version": version
    }