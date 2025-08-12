from fastapi import APIRouter, HTTPException
from sqlmodel import select

from ..models.urls import UrlDB, BaseUrl
from ..models.responses import AllUrlResponse, AddUrlMess, BaseMessage
from ..services.database import SessionDep

router = APIRouter(prefix="/manage", tags=["Dashboard"])


@router.get("/urls")
async def get_all_urls(session: SessionDep) -> AllUrlResponse:
    state = select(UrlDB)
    res = session.exec(state).all()
    return AllUrlResponse(urls=list(res))


@router.post("/urls")
async def add_new_url(url_record: BaseUrl, session: SessionDep) -> AddUrlMess:
    state = select(UrlDB).where(UrlDB.target == url_record.target)
    res = session.exec(state).first()
    if res:
        raise HTTPException(400, "Target already exists")

    db_data = UrlDB.model_validate(url_record)
    session.add(db_data)
    session.commit()
    return AddUrlMess(
        message="Successfully add a new redrict record",
        alias=url_record.target,
        location=url_record.location,
    )


@router.delete("/urls/{target}", status_code=204)
async def delete_url(target: str, session: SessionDep):
    state = select(UrlDB).where(UrlDB.target == target)
    res = session.exec(state).first()
    if not res:
        raise HTTPException(404)

    session.delete(res)
    session.commit()


@router.put("/urls", status_code=204)
async def update_url(url_record: BaseUrl, session: SessionDep):
    state = select(UrlDB).where(UrlDB.target == url_record.target)
    res = session.exec(state).first()
    if not res:
        raise HTTPException(404)
    res.target = url_record.target
    res.location = url_record.location
    session.add(res)
    session.commit()
