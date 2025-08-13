from redis import Redis
from fastapi import APIRouter

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("")
async def get_all_settings():
    r = Redis(host="localhost", decode_responses=True)
    res = r.hgetall("settings:general")
    print(res)
