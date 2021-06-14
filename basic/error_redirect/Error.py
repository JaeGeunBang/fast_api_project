from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import RedirectResponse

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/error")


@app.get("/error")
async def get_error():
    pass



@app.get("/")
async def get_helloworld():
    return {"Hello World"}
