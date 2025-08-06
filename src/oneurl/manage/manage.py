from fastapi import APIRouter
from sqlmodel import select

from ..models.urls import UrlDB, BaseUrl
from ..models.responses import AllUrlResponse, AddUrlMess
from ..services.database import SessionDep

router = APIRouter(prefix="/manage", tags=["Dashboard"])


@router.get("/urls")
async def get_all_urls(session: SessionDep) -> AllUrlResponse:
    state = select(UrlDB)
    res = session.exec(state).all()
    return AllUrlResponse(urls=list(res))


@router.post("/url")
async def get_new_url(url_record: BaseUrl, session: SessionDep):
    db_data = UrlDB.model_validate(url_record)
    session.add(db_data)
    session.commit()
    return AddUrlMess(
        message="Successfully add a new redrict record",
        alias=url_record.target,
        location=url_record.location,
    )
