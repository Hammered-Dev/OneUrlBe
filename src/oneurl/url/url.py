from ..models.urls import UrlDB
from ..services.database import SessionDep

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from sqlmodel import select

router = APIRouter(tags=["Redrict Url"], prefix="/rd")


@router.get("/{target}")
def redrict(target: str, session: SessionDep) -> RedirectResponse:
    state = select(UrlDB).where(UrlDB.target == target)
    res = session.exec(state).first()

    if not res:
        raise HTTPException(404, "Target not found")

    return RedirectResponse(res.location)
