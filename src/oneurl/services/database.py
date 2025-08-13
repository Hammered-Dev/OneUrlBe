import os

from sqlmodel import SQLModel, create_engine, Session
from typing import Annotated
from fastapi import Depends
from dotenv import load_dotenv

from ..models.urls import UrlDB, BaseUrl

load_dotenv()

db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT", "5432")
username = os.getenv("POSTGRES_USRNAME", "postgres")
password = os.getenv("POSTGRES_PASS")
dbname = os.getenv("POSTGRES_DBMANE", "postgres")

engine = create_engine(
    f"postgresql://{username}:{password}@{db_host}:{db_port}/{dbname}"
)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def create_and_check_db():
    SQLModel.metadata.create_all(engine)
