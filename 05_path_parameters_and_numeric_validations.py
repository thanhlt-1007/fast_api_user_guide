from fastapi import FastAPI, Query, Path
from typing import Optional

app = FastAPI()

#
# Import Path
#

# @app.get("/items/{item_id}")
# def read_item(
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get",
#   ),
#   q: Optional[str] = Query(
#     None,
#     alias="item-query"
#   )
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   return results

#
# Declare metadata
#

# @app.get("/items/{item_id}")
# def read_item(
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get"
#   ),
#   q: Optional[str] = Query(
#     None,
#     alias="item-query"
#   )
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   return results

#
# Order the parameters as you need
#

# @app.get("/items/{item_id}")
# def read_item(
#   q: str,
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get"
#   )
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   return results

#
# Order the parameters as you need, tricks
#

# @app.get("/items/{item_id}")
# def read_item(
#   *,
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get"
#   ),
#   q: str
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   return results

#
# Number validations: greater than or equal
#

# @app.get("/items/{item_id}")
# def read_item(
#   *,
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get",
#     ge=1
#   ),
#   q: str
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   return results

#
# Number validations: greater than and less than or equal
#

# @app.get("/items/{item_id}")
# def read_item(
#   *,
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get",
#     gt=0,
#     le=1000
#   ),
#   q: str
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   return results

#
# Number validations: floats, greater than and less than
#

# @app.get("/items/{item_id}")
# def read_item(
#   *,
#   item_id: int = Path(
#     ...,
#     title="The ID of the item to get",
#     ge=0,
#     le=1000
#   ),
#   q: str,
#   size: float = Query(
#     ...,
#     gt=0,
#     le=10.5
#   )
# ):
#   results = {"item_id": item_id}

#   if q:
#     results.update({"q": q})

#   return results
