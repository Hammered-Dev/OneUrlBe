from pydantic import BaseModel


class SettingModel(BaseModel):
    delay: int
