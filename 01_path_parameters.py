from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Model(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"

@app.get("/")
def root():
  return {"message": "Hello Worrld"}

# @app.get("/items/{item_id}")
# def read_item(item_id):
#   return {"item_id": item_id}

@app.get("/items/{item_id}")
def read_item(item_id: int):
  return {"item_id": item_id}

@app.get("/users/me")
def read_current_user():
  return {"user_id": "the current user"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
  return {"user_id": user_id}

@app.get("/models/{model_name}")
def read_model(model_name):
  if model_name == Model.alexnet:
    message = "Deep Learning FTX!"
  elif model_name == Model.lenet:
    message = "LeCNN all the images"
  else:
    message = "LeCNN all the images"

  return {"model_name": model_name, "message": message}
