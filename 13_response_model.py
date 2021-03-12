from fastapi import FastAPI
from typing import  Optional, List
from pydantic import BaseModel, EmailStr

app = FastAPI()

#
# Response Model
#

# You can declare the model used for the response with the parameter response_model in any of path operations
# @app.get()
# @app.post()
# @app.put()
# @app.delete()

# class Item(BaseModel):
#   name: str
#   description: Optional[str] = None
#   price: float
#   tax: Optional[float] = None
#   tags: List[str] = []

# @app.post("/items", response_model=Item)
# def create_item(item: Item):
#   return item

#
# Return the same input data
#

# class UserIn(BaseModel):
#   user_name: str
#   password: str
#   email: EmailStr
#   full_name: Optional[str] = None

# Don't do it in production
# @app.post("/user", response_model=UserIn)
# def create_user(user: UserIn):
#   return user

# Now whenever a browser is creating a user with a password, the API will return the same password in the response.
# In this case, it might not a problem, because the user himself is sending password
# But if we use the same model for another path operation, we could ne sending our user's password to ecery client

#
# Add in output model
#

# We can instead create an input model with the plaintext password and output model without it

# class UserOut(BaseModel):
#   user_name: str
#   email: EmailStr
#   full_name: Optional[str] = None

# @app.post("/user", response_model=UserOut)
# def create_user(user: UserIn):
#   return user

#
# Response Model encoding parameters
#

# Your response model could have default values, like
# but you might want to omit them from the result if they were not actually stored.
# For example , if you have models with optional attributes in a NoSQL database, but you don't want to send very long JSON responses full of default values.

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: float = 10.5
  tags: List[str] = []

items = {
  "foo": {
    "name": "Foo",
    "price": 50.2
  },
  "bar": {
    "name": "Bar",
    "description": "The bartenders",
    "price": 62,
    "tax": 20.2
  },
  "baz": {
    "name": "Baz",
    "description": None,
    "price": 50.2,
    "tax": 10.5,
    "tags": []
  }
}

@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
def read_item(item_id: str):
  return items[item_id]

#
# Use the response_model_exclude_unset parameter
#

# You can set the path operation decorator parameter response_model_exclude_unset=True
# and those default values won't be included in the response, only the values actually set
# So if you send a request to that path operation for the item with ID foo, the response (not including default values) will be
# {
#   "name": "Foo",
#   "price": 50.2
# }

# Info
# FastAPI uses Pydantic model's dict() with its exclude_unset_parameters to schieve this

# Info
# You can also use
# response_model_exclude_default=True
# response_model_exclude_none=Trie

# Data with values for fields with defaults
# But if your data has values for the model's fields with default values, like the item witd ID bar
# {
#   "name": "Bar",
#   "description"" "The bartenders,
#   "price": 62,
#   "tax": 20.2
# }
# they will be included in the response

# Data with the same values as the defaults
# if the data has the same values as default ones, likes the item with ID baz
# {
#   "name": "Baz",
#   "description": None,
#   "price": 50.2,
#   "tax": 10.5,
#   "tags": [],
# }

# FastAPI is smart enough (actually, Pydantic is smart enough) to realize that, even though description, tax and tags have the same values as the defaults
# they were set explicitly (instead of taken from the defaults)

# So, they will be included in the JSON response

# Tip
# Notice that the default values can be anythong, not only None.
# They can be a list([]), a float of 10.5, etc.

# response_model_include and response_model_exclude

# You can also use the path operation decorator parameters response_model_include and response_model_exclude
# They take a set of str with the name of attributes to include (omitting the rest) or to exclude (includeing the rest)
# This can be used as a quick shortcut if you have only one Pydantic model and want to remove some data from the output.

# Tip
# But it is still recommended to use the ideas above, using multiple classes, instead of these parameters.

# This is because the JSON Schema generated in your app's OpenAPI (and the docs) will still be one for the complete model.
# even if you use response_model_include or response_model_exclude to omit some attributes.

# This also applies to response_model_by_alias that works similarly

# @app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
# def read_item_name(item_id: str):
#   return items[item_id]

# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# def read_item_public(item_id: str):
#   return items[item_id]

# Using list instead of set

# If you forget to use a set and use a list of tuple instead
# FastAOU will still convert it to a set and it work correcctly

@app.get("/items/{item_id}/name", response_model=Item, response_model_include=["name", "description"])
def read_item(item_id: str):
  return items[item_id]

@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
def read_item_public(item_id: str):
  return items[item_id]
