from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

# class Item(BaseModel):
#   name: str
#   description: Optional[str] = None
#   price: float
#   tax: Optional[float] = None

#   class Config:
#     schema_extra = {
#       "example": {
#         "name": "Foo",
#         "description": "A very nice Item",
#         "price": 35.4,
#         "tax": 3.2
#       }
#     }

# class Item(BaseModel):
#   name: str = Field(..., example="Foo")
#   description: Optional[str] = Field(None, example="A very nice Item")
#   price: float = Field(..., example=35.4)
#   tax: Optional[float] = Field(None, example=3.2)

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#   result = {"item_id": item_id, "item": item}
#   return result

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None

@app.put("/items/{item_id}")
def update_item(
  item_id: int,
  item: Item = Body(
    ...,
    example={
      "name": "Foo",
      "description": "A vary nice Item",
      "price": 35.4,
      "tax": 3.2
    }
  )
):
  return {"item_id": item_id, "item": item}
