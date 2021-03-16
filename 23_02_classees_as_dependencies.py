#
# Classes as Dependencies
#

#
# A dict from the previous example
#

# from fastapi import FastAPI, Depends
# from typing import Optional

# app = FastAPI()

# def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#   return {"q": q, "skip": skip, "limit": limit}

# @app.get("/items")
# def read_items(common: dict = Depends(common_parameters)):
#   return common

# @app.get("/users")
# def read_users(common: dict = Depends(common_parameters)):
#   return common

#
# What makes a dependency
#

#
# Classes as dependencies
#

# class Cat:
#   def __init__(self, name: str):
#     self.name = name

# fluffy = Cat(name = "Mr Fluffy")

from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()

fake_items_db = [
  {"item_name": "Foo"},
  {"item_name": "Bar"},
  {"item_name": "Baz"}
]

class CommonQueryParams:
  def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
    self.q = q
    self.skip = skip
    self.limit = limit

# @app.get("/items")
# def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
#   response = {}
#   if commons.q:
#     response.update({"q": commons.q})
#   items = fake_items_db[commons.skip : commons.skip + commons.limit]
#   response.update({"items": items})

#   return response

#
# Use it
#

#
# Type annotation vs Depends
#

# @app.get("/items")
# def read_items(commons: Depends(CommonQueryParams)):
#   response = {}
#   if commons.q:
#     response.update({"q": commons.q})
#   items = fake_items_db[commons.skip : commons.skip + commons.limit]
#   response.update({"items": items})

#   return response

#
# Shortcut
#

@app.get("/items")
def read_items(commons: CommonQueryParams = Depends()):
  response = {}
  if commons.q:
    response.update({"q": commons.q})
  items = fake_items_db[commons.skip : commons.skip + commons.limit]
  response.update({"items": items})

  return response
