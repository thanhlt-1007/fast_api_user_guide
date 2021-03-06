from fastapi import FastAPI
from typing import Optional

app = FastAPI()

fake_items_db = [
  {"item_name": "Foo"},
  {"item_name": "Bar"},
  {"item_name": "Baz"}
]

# @app.get("/items")
# def read_items(skip: int = 0, limit: int = 10):
#   return fake_items_db[skip : skip + limit]

#
# Optional parameters
#

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#   item = {"item_id": item_id}

#   if q:
#     item.update({"q": q})

#   return item

#
# Query parameter type conversion
#

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
#   item = {"item_id": item_id}

#   if q:
#     item.update({"q": q})

#   if not short:
#     item.update({"description": "This is an amazing item that has a long description"})

#   return item

#
# Multiple path and query parameters
#

# @app.get("/users/{user_id}/items/{item_id}")
# def read_user_item(user_id: int, item_id: int, q: Optional[str] = None, short: bool = False):
#   item = {"item_id": item_id, "user_id": user_id}

#   if q:
#     item.update({"q": q})

#   if not short:
#     item.update({"description": "This is an amazing item that has a long description"})

#   return item

#
# Required query parameters
#

# @app.get("/items/{item_id}")
# def read_item(item_id: int, needy: str):
#   return {"item_id": item_id, "needy": needy}
