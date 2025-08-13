from ..models.urls import UrlDB
from ..services.database import SessionDep
from ..models.responses import BaseUrl

from fastapi import APIRouter, HTTPException
from sqlmodel import select

router = APIRouter(tags=["Redrict Url"], prefix="/rd")


@router.get("/{target}")
def redrict(target: str, session: SessionDep) -> BaseUrl:
    state = select(UrlDB).where(UrlDB.target == target)
    res = session.exec(state).first()

    if not res:
        raise HTTPException(404, "Target not found")

    return BaseUrl.model_validate(res)
