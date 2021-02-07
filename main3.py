from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Schema Extra - Example (default request body를 제공해줌)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# Field, example로 제공해줄수도 있음
from pydantic import Field

class Item2(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)

# 함수의 파라미터로 제공해줄수도 있음
@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Item = Body(
            ...,
            example= {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            },
        ),
):
    result = {"item_id": item_id, "item": item}
    return results

# Extra Data Types
## UUID - Universally Unique Identifier
## datetime.datetime - 날짜 + 시간 (str)
## datetime.date = 날짜 (str)
## datetime.time = 시간 (str)
## datetime.timedelta = float 형태의 total seconds
## frozenset = set?
## bytes = string 형태의 바이트
## decimal = float 형태의 decimal 값

from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: Optional[datetime] = Body(None),
        end_datetime: Optional[datetime] = Body(None),
        repeat_at: Optional[time] = Body(None),
        process_after: Optional[timedelta] = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }