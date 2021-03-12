from fastapi import FastAPI
from typing import Optional, List, Set, Dict
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
  url: HttpUrl
  name: str

class Item(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  tax: Optional[float] = None
  tags: Set[str] = []
  images: Optional[List[Image]] = None

class Offer(BaseModel):
  name: str
  description: Optional[str] = None
  price: float
  items: List[Item]

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  result = {"item_id": item_id, "item": item}
  return result

@app.post("/offers")
def create_offer(offer: Offer):
  return offer

@app.post("/images/multiple")
def create_multiple_images(images: List[Image]):
  return images

@app.post("/index-weights")
# key is int
# value is float
# example: {"1": 1.1, "2": 2.2, "3": 3.3}
def create_index_weights(weights: Dict[int, float]):
  return weights
