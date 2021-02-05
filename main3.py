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