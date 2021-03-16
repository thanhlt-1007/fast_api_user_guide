#
# Dependencies - First Steps
#

#
# What is "Dependency Injection"
#

#
# First Steps
#

#
# Create a dependency, or "dependable"
#

from fastapi import FastAPI, Depends
from typing import Optional

app = FastAPI()

def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
  return {"q": q, "skip": skip, "limit": limit}

@app.get("/items")
def read_items(commons: dict = Depends(common_parameters)):
  return commons

@app.get("/users")
def read_user(commons: dict = Depends(common_parameters)):
  return commons
