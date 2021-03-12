from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()

@app.post("/files")
def create_file(file_bytes: bytes = File(...), file_upload: UploadFile = File(...), token: str = Form(...)):
  return {
    "len_file_bytes": len(file_bytes),
    "content_type_file_upload": file_upload.content_type,
    "token": token
  }
