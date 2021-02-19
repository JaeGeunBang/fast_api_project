from typing import Optional, Set

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []

# 아래 처럼 description을 쓰거나

"""
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
# Line로 쓰고 싶다면 함수안에 쓴다.
@app.post("/items/", response_model=Item,
          tags=["items"],
          summary="Create an item222",
          description="Create an item with all the information, name, description, price, tax and a set of unique tags",
          response_description="The created item",)
async def create_item(item: Item):
    return item


@app.get("/items/", tags=["items"], deprecated=True)
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]