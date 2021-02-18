from typing import List

from database import database, clusters
import sqlalchemy
from fastapi import FastAPI
from model import Cluster, PostClusterIn


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/clusters/", response_model=List[Cluster])
async def get_clusters():
    query = clusters.select()
    return await database.fetch_all(query)


@app.post("/clusters/", response_model=Cluster)
async def post_clusters(cluster: PostClusterIn):
    query = clusters.insert().values(name=cluster.name, config=cluster.config, status='')
    last_record_id = await database.execute(query)
    return {**cluster.dict(), "id": last_record_id}
