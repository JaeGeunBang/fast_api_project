from typing import List, Optional

from fastapi import FastAPI, Query

app = FastAPI()


# Query 통해 Validation을 수행를
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 꼭 필요한 Query는 ... 을 넣어주어야함
@app.get("/items2/")
async def read_items2(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items3/")
async def read_items3(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items


# Query 관련된 Validation들
# deprecated는 이제 삭제될것을 알려줌
@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
