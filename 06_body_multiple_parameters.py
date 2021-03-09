from fastapi import FastAPI, Path, Query, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#
# Mix Path, Query and body parameters
#

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

class User(BaseModel):
  user_name: str
  full_name: Optional[str] = None

# @app.put("/items/{item_id}")
# def update_item(
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get",
#     ge=0,
#     le=1000
#   ),
#   q: Optional[str] = Query(
#     None
#   ),
#   item: Optional[Item] = None
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   if item:
#     results.update({"item": item})

#   return results

#
# Multiple body parameters
#

# @app.put("/items/{item_id}")
# def update_item(
#   *,
#   item_id: int = Path(
#     ...
#   ),
#   item: Item,
#   user: User
# ):
#   return {"item_id": item_id, "item": item, "user": user}

#
# Singular values in body
#

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item, user: User, importance: int = Body(...)):
#   results = {
#     "item_id": item_id,
#     "item": item,
#     "user": user,
#     "importance": importance
#   }

#   return results

#
# Multiple body params and query
#

# @app.put("/items/{item_id}")
# def update_item(
#   item_id: int,
#   item: Item,
#   user: User,
#   q: Optional[str] = None,
#   importance: int = Body(
#     ...,
#     gt=0
#   )
# ):
#   results = {
#     "item_id": item_id,
#     "item": item,
#     "user": user,
#     "importance": importance
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Embed a single body parameter
#

# @app.put("/items/{item_id}")
# def update_item(
#   item_id: int,
#   item: Item = Body(
#     ...,
#     embed=True
#   )
# ):
#   results = {
#     "item_id": item_id,
#     "item": item
#   }

#   return results
