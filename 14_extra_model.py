from fastapi import FastAPI
from typing import Optional, Union, List, Dict
from pydantic import BaseModel, EmailStr

app = FastAPI()

# Extra Model

# The input model needs to be able to have a password
# The output model should not have a password
# The database model would probably neef to have a hasjed password

# Danger
# Never store user's plaintext passwords. Always store a secure hash that you can then verify
# If you don't know, you will learn what a password hash is in the security chapters

# Multiple models

# Here's a general idea of how the models could look like with their password fields and the laces where they are used

# class UserIn(BaseModel):
#   user_name: str
#   password: str
#   email: EmailStr
#   full_name: Optional[str] = None

# class UserOut(BaseModel):
#   user_name: str
#   email: EmailStr
#   full_name: Optional[str] = None

# class UserInDB(BaseModel):
#   user_name: str
#   hashed_password: str
#   email: EmailStr
#   full_name: Optional[str] = None

# def fake_password_hasher(raw_password: str):
#   return "super_secret" + raw_password

# def fake_save_user(user_in: UserIn):
#   hashed_password = fake_password_hasher(user_in.password)
#   user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#   print("User saved! .. not really")

#   return user_in_db

# @app.post("/users", response_model=UserOut)
# def create_user(user_in: UserIn):
#   user_saved = fake_save_user(user_in)
#   return user_saved

#
# About **user_int.dict()
#

# Pydantic.dict()
# user_int is a Pydantic model of class UserIn
# Pydantic models have a dict() method that returns a dict with a model's data
# So, if we created a Pydantic object user_in like
# user_in = UserIn(user_name="john", password="secret", email="john.doe@example.com")
# and then we call
# user_dict = user_in.dict()

# we know have a dict with the data in the variable user_dict (it's a dict instead of a Pydantic model object)
# And if we call
# print(user_dict)
# we would get a Python dict with
# {
#   "user_name": "john",
#   "password": "secret",
#   "email": "john.doe@example.com",
#   "full_name": None
# }

# Unwrapping a dict

# If we take a dict liek user_dict and pass it to a function (or class) with **user_dict
# Python will unwrap it
# It will pass the keys abd values of the user_dict directly as key-value arguments

# So, continuing with the user_dict from above, writing
# UserInt(**user_dict)

# Would result in something equivalebt to
# UserIn(
#   user_name="john",
#   password="secret",
#   email="john.doe@example.com",
#   full_name=None
# )

# Or more exactly, using user_dict directly, with whatever contents it might have in the future
# UserIn(
#   user_name = user_dict["user_name"],
#   password = user_dict["password"],
#   email = user_dict["email"],
#   full_name = user_dict["full_name"]
# )

# A Pydantic model from the contents of another
# As in the example above we got user_dict from user_in.dict(), this code
# user_dict = user_in.dict()
# UserInDB(**user_dict)

# would be equivalent to
# UserInDB(**user_in.dict())

# because user_in.dict() is a dict, and then we make Python unwrap it by passing it to UserInDB prepended with **
# So, we get a Pydantic model from the data in another Pydantic model.

# Unwrapping a dict and extra keywords
# And then adding the extra keyword argument hashed_password=hashed_password, like in
# UserInDB(**user_in.dict(), hashed_password=hashed_password)
# ends up being like
# UserInDB(
#   user_name = user_dict["user_name"],
#   password = user_dict["password"],
#   email = user_dict["email"],
#   full_name = user_dict["full_name"]
#   hashed_password = hashed_password
# )

# Warning
# The supporting addtional functions are just to demo a possible flow of the data
# but they of course are not providing any real security

# Reduce duplication

# Reducing code duplication is one ò the core ideas om FastAPI
# As code duplication increments teh chances of bugs, security issues, code desynchronization issues (when you update in one place but noe in the other), etc
# And thế models are all sharing a lot ò the data and suplicating attribute names and types
# We could do better
# We can declare a UserBase model that serves as a base for our other mnodels
# And then we can make subclasses of taht model that inherit ít attributes (type declarations, validation, etc)
# All the data conversion, validation, documentation, etc, wil still work as normally
# That way, we can declare just the differences between the models (wuth pkaintext passeordm with hashed_password and without password)

# class UserBase(BaseModel):
#   user_name: str
#   email: EmailStr
#   full_name: Optional[str] = None

# class UserIn(UserBase):
#   password: str

# class UserOut(UserBase):
#   pass

# class UserInDB(UserBase):
#   hashed_password: str

# def fake_password_hasher(raw_password: str):
#   return "supersecret" + raw_password

# def fake_save_user(user_in: UserIn):
#   hashed_password = fake_password_hasher(user_in.password)
#   user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#   print("User saved! ... not really ...")
#   return user_in_db

# @app.post("/users", response_model=UserOut)
# def create_user(user_in: UserIn):
#   user_saved = fake_save_user(user_in)
#   return user_saved

#
# Union of anyOf
#

# class BaseItem(BaseModel):
#   description: str
#   type: str

# class CarItem(BaseItem):
#   type = "car"

# class PlaneItem(BaseItem):
#   type = "plane"
#   size: int

# items = {
#   "item1": {
#     "description": "All my friends drive a low rider",
#     "type": "car"
#   },
#   "item2": {
#     "description": "Music is my aeroplane, it's my aeroplane",
#     "type": "plane",
#     "size": 5,
#   }
# }

# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# def read_item(item_id: str):
#   return items[item_id]

#
# List of models
#

# class Item(BaseModel):
#   name: str
#   description: str

# items = [
#   {"name": "Foo", "description": "There comes my hero"},
#   {"name": "Red", "description": "It's my aeroplane"}
# ]

# @app.get("/items", response_model=List[Item])
# def read_items():
#   return items

#
# Response with arbitray dict
#

@app.get("/keyword-weights", response_model=Dict[str, float])
def read_keyword_weights():
  return {"foo": 2.3, "bar": 3.4}
