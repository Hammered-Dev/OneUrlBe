from ..models.urls import UrlDB, BaseUrl
from fastapi import APIRouter, Response

router = APIRouter(tags=["Redrict Url"], prefix="/redir")


@router.get("/{target}")
def redrict(target: str):
    return Response(
        status_code=301,
        headers=BaseUrl(target=target, location="https://google.com").model_dump(),
    )
