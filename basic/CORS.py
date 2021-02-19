from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

"""
Origin은 Protocol, Domain, Port의 결합을 뜻
아래 예제는 서로 다른 origin들이다 (different origins)
http://localhost
https://localhost
http://localhost:8080

CORS는 크로스 오리진 (different origins)끼리의 자원을 공유하기 위함. 
ex) 프론드엔드, 백엔드 
백엔드는 allowed origin 리스트를 가지며, 해당 origin을 가지는 프론트만 백엔드에 통신할수 있다

보안적인 하나의 장치인것같음. 인증된 Client만 백엔드서버에서 요청을 받을수 있다. 이런 의미
"""

# allowed origins
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Hello World"}
