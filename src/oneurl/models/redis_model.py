from pydantic import BaseModel


class SettingModel(BaseModel):
    delays: int
