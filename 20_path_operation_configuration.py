#
# Path Operation Configuration
#

#
# Response Status Code
#

# from fastapi import FastAPI, status
# from pydantic import BaseModel
# from typing import Optional, Set

# app = FastAPI()

# class Item(BaseModel):
#   name: str
#   description: Optional[str] = None
#   price: float
#   tax: Optional[float] = None
#   tags: Set[str] = []

# @app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
# def create_item(item: Item):
#   return item

#
# Tags
#

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional, Set

# app = FastAPI()

# class Item(BaseModel):
#   name: str
#   description: Optional[str] = None
#   price: float
#   tax: Optional[float] = None
#   tags: Set[str] = []

# @app.post("/items", response_model=Item, tags=["items"])
# def create_item(item: Item):
#   return item

# @app.get("/items", tags=["items"])
# def read_items():
#   return [{"name": "Foo", "price": 42}]

# @app.get("/users", tags=["users"])
# def read_users():
#   return [{"user_name": "John Doe"}]

#
# Summary and description
#

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional, Set

# app = FastAPI()

# class Item(BaseModel):
#   name: str
#   description: Optional[str] = None
#   price: float
#   tax: Optional[float] = None
#   tags: Set[str] = []

# @app.post("/items",
#   response_model=Item,
#   summary="Create an item",
#   description="Create an item with all the information, name, description, price, tax and a set of unique tags"
# )
# def create_item(item: Item):
#   return item

#
# Description from docstring
#

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional, Set

# app = FastAPI()

# class Item(BaseModel):
#   name: str
#   description: Optional[str] = None
#   price: float
#   tax: Optional[float] = None
#   tags: Set[str] = []

# @app.post("/items",
#   response_model=Item,
#   summary="Create an item"
# )
# def create_item(item: Item):
#   """
#   Create an item with all the information

#   - **name**: each item must have a name
#   - **description**: a long description
#   - **price**: required
#   - **tax**: if the item doesn't have tax, you can omit it
#   - **tags**: a set of unique tag strings for this item
#   """
#   return item

#
# Response description
#

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional, Set

# app = FastAPI()

# class Item(BaseModel):
#   name: str
#   description: Optional[str] = None
#   price: float
#   tax: Optional[float] = None
#   tags: Set[str] = []

# @app.post(
#   "/items",
#   response_model=Item,
#   summary="Create an item",
#   response_description="The created item"
# )
# def create_item(item: Item):
#   """
#   Create an item with all the information:

#   - **name**: each item must have a name
#   - **description**: a long description
#   - **price**: required
#   - **tax**: if the item doesn't have a tax, you can omit this
#   - **tags**: a set of unique tag strings for this item
#   """

#   return item

#
# Deprecated a path operation
#

from fastapi import FastAPI

app = FastAPI()

@app.get("/items", tags=["items"])
def read_items():
  return [{"name": "Foo", "price": 42}]

@app.get("/users", tags=["users"])
def read_users():
  return [{"user_name": "John Doe"}]

@app.get("/elements", tags=["items"], deprecated=True)
def read_elements():
  return [{"item_id": "Foo"}]
