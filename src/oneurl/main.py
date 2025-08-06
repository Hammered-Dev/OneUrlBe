from fastapi import FastAPI
from .url.url import router as url_router

app = FastAPI()


app.include_router(url_router)
