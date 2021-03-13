#
# Body - Updates
#

#
# Update replacing with PUT
#

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional, List
# from fastapi.encoders import jsonable_encoder

# app = FastAPI()

# class Item(BaseModel):
#   name: Optional[str] = None
#   description: Optional[str] = None
#   price: Optional[float] = None
#   tax: float = 10.5
#   tags: List[str] = []

# items = {
#   "foo": {"name": "Foo", "price": 50.2},
#   "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#   "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
# }

# @app.get("/items/{item_id}", response_model=Item)
# def read_item(item_id: str):
#   return items[item_id]

# @app.put("/items/{item_id}", response_model=Item)
# def update_item(item_id: str, item: Item):
#   items[item_id] = jsonable_encoder(item)
#   return items[item_id]

#
# Warning about replacing
#

# That means that if you want to update the item bar using PUT with a body containing
# {
#   "name": "Barz",
#   "price": 3,
#   "description": None
# }
# because it doesn't include the already stored attribute "tax": 20.2, the input model would take the default value of "tax": 10.5
# And the data would be saved that new "tax": 10.5

#
# Partial updates with PATCH
#

#
# Using Pydantic's exclude_unset parameter
#

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class Item(BaseModel):
  name: Optional[str] = None
  description: Optional[str] = None
  price: Optional[float] = None
  tax: float = 10.5
  tags: List[str] = []

items = {
  "foo": {"name": "Foo", "price": 50.2},
  "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
  "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
  return items[item_id]

@app.patch("/items/{item_id}")
def update_item(item_id: str, item: Item):
  stored_item_data = items[item_id]
  stored_item_model = Item(**stored_item_data)
  update_data = item.dict(exclude_unset=True)
  updated_item = stored_item_model.copy(update=update_data)
  items[item_id] = jsonable_encoder(updated_item)

  return updated_item
