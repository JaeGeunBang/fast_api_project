import uvicorn
from fastapi import FastAPI

app = FastAPI()

"""
1. Run meun -> Debug 클릭
2. Debug에서 디버깅할 main 파일 선택
3. 디버그 진행
"""

@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)