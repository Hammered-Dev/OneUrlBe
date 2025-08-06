from fastapi import APIRouter
from sqlmodel import select

from ..models.urls import UrlDB
from ..models.responses import AllUrlResponse
from ..services.database import SessionDep

router = APIRouter(prefix="/manage", tags=["Dashboard"])


@router.get("/urls")
async def get_all_urls(session: SessionDep):
    state = select(UrlDB)
    res = session.exec(state).all()
    return AllUrlResponse(urls=list(res))
