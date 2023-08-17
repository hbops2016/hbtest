from pydantic import BaseModel
from typing import Optional, Any


class ResponseSchema(BaseModel):
    code: Optional[int] = 200
    message: Optional[str] = "success"
    data: Optional[Any] = None
