from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

cors_origins = ["http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
