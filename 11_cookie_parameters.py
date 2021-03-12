from fastapi import FastAPI, Cookie
from typing import Optional

app = FastAPI()

#
# Import Cookie
#

#
# Declare Cookie as parameters
#

@app.get("/items")
def read_items(ads_id: Optional[str] = Cookie(None)):
  return {"ads_id": ads_id}
