from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files")
def create_file(file: bytes = File(...)):
  return {"len": len(file)}

@app.post("/upload_files")
def create_upload_file(file: UploadFile = File(...)):
  return {"filename": file.filename}
