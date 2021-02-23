from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

"""
dataModel은 pydantic의 BaseModel을 상속 받는다
- 아래 필드 타입에 맞지 않으면 에러가 발생함
"""
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/items2/")
async def create_item2(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request Body + Path Parameter
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# Request Body + Path + Query Parameter
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
