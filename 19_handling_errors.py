from fastapi import FastAPI, Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from pydantic import BaseModel

app = FastAPI()

items = {"foo": "The Woo Wrestlers"}

#
# Use HTTPException
#

# @app.get("/items/{item_id}")
# def read_item(item_id: str):
#   if item_id not in items:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
#   return {"item": items[item_id]}

#
# Add custom headers
#

# @app.get("/items-header/{item_id}")
# def read_item_header(item_id: str):
#   if item_id not in items:
#     raise HTTPException(
#       status_code=status.HTTP_404_NOT_FOUND,
#       detail="Item not found",
#       headers={"X-Error": "There goes my error"}
#     )

#   return items[item_id]

#
# Install custom exception handlers
#

# class UnicornException(Exception):
#   def __init__(self, name: str):
#     self.name = name

# @app.exception_handler(UnicornException)
# def unicorn_exception_handler(request: Request, exception: UnicornException):
#   return JSONResponse(
#     status_code=418,
#     content={
#       "message": f"Oops! {exception.name} did something. There goes a rainbow ..."
#     }
#   )

# @app.get("/unicorns/{name}")
# def read_unicorn(name: str):
#   if name == "yolo":
#     raise UnicornException(name=name)

#   return {"unicorn_name": name}

#
# Override request validation exceptions
#

# @app.exception_handler(StarletteHTTPException)
# def http_exception_handler(request: Request, exception: StarletteHTTPException):
#   return PlainTextResponse(
#     str(exception.detail),
#     status_code=exception.status_code
#   )

# @app.exception_handler(RequestValidationError)
# def request_validation_exception_handler(request: Request, exception: RequestValidationError):
#   return PlainTextResponse(
#     str(exception),
#     status_code=status.HTTP_400_BAD_REQUEST
#   )

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#   if item_id == 3:
#     raise HTTPException(
#       status_code=418,
#       detail="Nope! i don't like 3"
#     )

#   return {"item_id": item_id}

#
# Use the RequestValidatorError body
#

@app.exception_handler(RequestValidationError)
def request_validation_exception_handler(request: Request, exception: RequestValidationError):
  return JSONResponse(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    content=jsonable_encoder({
      "detail": exception.errors(),
      "body": exception.body
    })
  )

class Item(BaseModel):
  title: str
  size: int

@app.post("/items")
def create_item(item: Item):
  return item
