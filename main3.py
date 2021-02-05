from typing import Optional

from fastapi import FastAPI, Path
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

# Body - Multiple Parameters
@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., title = "The ID of the item to get", gc=0, le=1000),
        q: Optional[str] = None,
        item: Optional[Item] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# Body - Multiple Parameters
@app.put("/items2/{item_id}")
async def update_item(
        item_id: int,
        item: Item,
        user: User
):
    results = {"item_id": item_id, "item": item, "user": user}
    return results

# Body - Field
from pydantic import Field
from fastapi import Body

class Item2(BaseModel):
    name: str
    description: Optional[str] = Field (
        None, Title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None

@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item2 = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

# Body - Nested Models
from typing import List
from pydantic import HttpUrl

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item3(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    image: Optional[List[Image]] = None

class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]

@app.put("/items3/{item_id}")
async def update_item3(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images