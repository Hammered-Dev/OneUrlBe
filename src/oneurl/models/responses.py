from pydantic import BaseModel

from .urls import BaseUrl


class AllUrlResponse(BaseModel):
    urls: list[BaseUrl]


class BaseMessage(BaseModel):
    message: str | None


class AddUrlMess(BaseMessage):
    alias: str
    location: str
