from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()

"""
공통 파라미터를 만들어, 각 함수에 적용할수 있다. (Dependency가 생길것)
"""

async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons