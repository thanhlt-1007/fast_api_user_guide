from fastapi import FastAPI, Body
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
  name: str
  description: Optional[str] = Field(
    None,
    title="The description of the item",
    max_length=300
  )
  price: float = Field(
    ...,
    gt=0,
    description="The price must be greater than zero"
  )
  tax: Optional[float] = None

#
# Declare model attributes
#

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item = Body(..., embed=True)):
#   results = {}
#   return results
