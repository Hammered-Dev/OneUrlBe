from redis import Redis
from fastapi import APIRouter

from ..models.redis_model import SettingModel

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("")
async def get_all_settings() -> SettingModel:
    r = Redis(host="localhost", decode_responses=True)
    res = r.hgetall("settings:general")
    return SettingModel.model_validate(res)


@router.put("", status_code=204)
async def update_all_settings(setting: SettingModel):
    r = Redis(host="localhost", decode_responses=True)
    r.hset("settings:general", mapping=setting.model_dump())
