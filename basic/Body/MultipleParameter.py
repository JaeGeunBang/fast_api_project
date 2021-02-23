from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


# Body는 Item, User와 같이 class가 아닌 일반적인 값에 validation을 적용할수 있다.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User,
                      importance: int = Body(..., gt=0),):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


# Item과 같은 class에도 적용할수 있음. embed 적용을 넣을수 있다
@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
