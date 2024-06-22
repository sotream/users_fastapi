from fastapi import FastAPI
from app.api import user
from app.db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
