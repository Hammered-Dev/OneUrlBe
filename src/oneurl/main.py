from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager

from .url.url import router as url_router
from .manage.manage import router as manage_router
from .services.database import create_and_check_db
from .models.urls import UrlDB


@asynccontextmanager
async def init(app: FastAPI):
    create_and_check_db()
    yield


app = FastAPI(lifespan=init)


app.include_router(url_router)
app.include_router(manage_router)
