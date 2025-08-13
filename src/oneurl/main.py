import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from .url.url import router as url_router
from .manage.manage import router as manage_router
from .services.database import create_and_check_db
from .models.urls import UrlDB

load_dotenv()


@asynccontextmanager
async def init(app: FastAPI):
    create_and_check_db()
    yield


app = FastAPI(lifespan=init, docs_url=None, title="OneUrl", redoc_url=None)

app.include_router(url_router)
app.include_router(manage_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

cors_origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]

env_origins = os.getenv("CORS_ALLOWED_ORIGINS")
if env_origins:
    cors_origins += env_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html(req: Request):
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    oauth2_redirect_url = app.swagger_ui_oauth2_redirect_url
    if oauth2_redirect_url:
        oauth2_redirect_url = root_path + oauth2_redirect_url
    return get_swagger_ui_html(
        openapi_url=openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=oauth2_redirect_url,
        init_oauth=app.swagger_ui_init_oauth,
        swagger_favicon_url="/static/favicon.ico",
        swagger_ui_parameters=app.swagger_ui_parameters,
    )


@app.get("/redoc", include_in_schema=False)
async def redoc_ui_html(req: Request):
    root_path = req.scope.get("root_path", "").rstrip("/")
    openapi_url = root_path + app.openapi_url
    return get_redoc_html(
        openapi_url=openapi_url,
        title=app.title + " - Redoc UI",
        redoc_favicon_url="/static/favicon.ico",
    )
