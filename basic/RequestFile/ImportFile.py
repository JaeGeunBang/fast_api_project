from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

# 위 File 보다 좀더 업그레이드 된것이 UploadFile인것 같음.
# 여러 메타 데이터를 제공함 (걍 file은 filename attribute가 없음)
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}