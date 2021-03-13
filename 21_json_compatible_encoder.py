#
# JSON Compatible Encoder
#

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from datetime import datetime
from fastapi.encoders import jsonable_encoder

fake_db = {}

class Item(BaseModel):
  title: str
  timestamp: datetime
  description: Optional[str] = None

app = FastAPI()
@app.put("/items/{id}")
def update_item(id: int, item: Item):
  data = jsonable_encoder(item)
  fake_db[id] = data

  return data
