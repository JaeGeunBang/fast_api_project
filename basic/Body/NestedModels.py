from typing import List, Set, Optional

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: list = []
    tags2: List[str] = [] # list = [] 와 달리 Type parameter를 넣고싶을
    tags3: Set[str] = set() # set도 있음.
    image: Optional[Image] = None # Nested Model
    images: Optional[List[Image]] = None # List of Nested Model


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results