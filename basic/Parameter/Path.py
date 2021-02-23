from fastapi import FastAPI
from enum import Enum

app = FastAPI()

"""
Path Parameter?
- localhost:8000/path1/path2/path3...
"""
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


"""
Enum 형태로 선택할수 있다.
"""
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


"""
Path Converter
"""
@app.get("/files/{file_path:path}")
async def read_file(path: str):
    return {"file_path": path}