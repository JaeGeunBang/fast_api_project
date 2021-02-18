from datetime import datetime
from typing import Any, Dict

from pydantic.main import BaseModel


class Cluster(BaseModel):
    id: int
    name: str
    config: str
    status: str
    #metadata: Dict[str, Any]
    #create_datetime: datetime
    #modify_datetime: datetime


class PostClusterIn(BaseModel):
    name: str
    config: str
