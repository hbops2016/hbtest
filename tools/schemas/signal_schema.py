from datetime import datetime
from typing import Dict
from pydantic import BaseModel
from api import schemas


class SignalSchema(BaseModel):
    operation_name: str = None
    operation_data: Dict = None
    operation_environment:str = "dev"
    operation_api_res: str = ""

    class Config:
        orm_mode = True


class SignalCreateSchema(SignalSchema):
    pass
