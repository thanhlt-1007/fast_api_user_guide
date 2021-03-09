from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#
# Create your data model
#

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

#
# Declare it as a parameter
#

# @app.post("/items")
# def create_item(item: Item):
#   return item.dict()

#
# Use the model
#

# @app.post("/items")
# def create_item(item: Item):
#   item_dict = item.dict()

#   if item.tax:
#     price_with_tax = item.price + item.tax
#     item_dict.update({"price_with_tax": price_with_tax})

#   return item_dict

#
# Request body + path parameters
#

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#   return {"item_id": item_id, **item.dict()}

#
# Request body + path + query parameters
#

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item, q: Optional[str] = None):
#   result = {"item_id": item_id, **item.dict()}

#   if q:
#     result.update({"q": q})

#   return result
