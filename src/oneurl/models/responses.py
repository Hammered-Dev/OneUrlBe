from pydantic import BaseModel

from .urls import BaseUrl


class AllUrlResponse(BaseModel):
    urls: list[BaseUrl]
