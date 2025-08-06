from sqlmodel import SQLModel, Field


class BaseUrl(SQLModel):
    target: str = Field(index=True)
    location: str


class UrlDB(BaseUrl, table=True):
    id: int = Field(primary_key=True)
