import time

from fastapi import FastAPI, Request

app = FastAPI()

# 실제 http 요청 처리전에 수행하는 함수
# 디비 커넥션 연결 작업을 할때 주로 사용한다.
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
