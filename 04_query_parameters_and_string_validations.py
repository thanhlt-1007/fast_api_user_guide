from fastapi import FastAPI, Query
from typing import Optional, List

app = FastAPI()

# @app.get("/items")
# def read_items(q: Optional[str] = None):
#   results = {
#     "item": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Additional validation
#

# @app.get("/items")
# def read_items(q: Optional[str] = Query(None, max_length=50)):
#   results = {
#     "item": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Use Query as the default value
#

#
# Add more validations
#

# @app.get("/items")
# def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):
#   results = {
#     "item": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Add regular expressions
#

# @app.get("/items")
# def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regexp="^fixedquery$")):
#   results = {
#     "item": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Default values
#

# @app.get("/items")
# def read_items(q: Optional[str] = Query("fixedquery", min_length=3)):
#   results = {
#     "item": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Make it required
#

# @app.get("/items")
# def read_items(q: str = Query(..., min_length=3)):
#   results = {
#     "items": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Query parameter list / multiple values
#

# @app.get("/items")
# def read_items(q: Optional[List[str]] = Query(None)):
#   return {"q": q}

#
# Query parameter list / multiple values with defaults
#

# @app.get("/items")
# def read_items(q: List[str] = Query(["foo", "bar"])):
#   return {"q": q}

#
# Using list
#

# @app.get("/items")
# def read_items(q: list = Query([])):
#   return {"q": q}

#
# Declare more metadata
#

# @app.get("/items")
# def read_items(
#   q: Optional[str] = Query(
#     None,
#     title="Query string",
#     description="Query string for the items to search in the database that have a good match",
#     min_length=3
#   )):
#   results = {
#     "items": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Alias parameters
#

# @app.get("/items")
# def read_items(
#   q: Optional[str] = Query(None, alias="item-query")
#   ):
#   results = {
#     "items": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results

#
# Deprecating parameters
#

#
# Deprecating parameters
#

# @app.get("/items")
# def read_items(
#   q: Optional[str] = Query(
#     None,
#     alias="item-query",
#     title="Query string",
#     description="Query string for the items to search in the database that have a good match",
#     min_length=3,
#     max_length=50,
#     regex="^fixedquery$",
#     deprecated=True
#   )
#   ):
#   results = {
#     "items": [
#       {"item_id": "Foo"},
#       {"item_id": "Bar"}
#     ]
#   }

#   if q:
#     results.update({"q": q})

#   return results
