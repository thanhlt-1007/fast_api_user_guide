from fastapi import FastAPI, Header
from typing import Optional, List

#
# Import Header
#

#
# Declare Header parameters
#

app = FastAPI()

# @app.get("/items")
# def read_items(user_agent: Optional[str] = Header(None)):
#   return {"User-Agent": user_agent}

#
# Automatic conversion
#

# Header has a little extra functionlity on top what Path, Query and Cookie provide
# Most of the standard headers are seperated by a "hyphen" characters, also know as the "minus symbol" (-)
# But a variable like "user-agent" is invalid in Python
# So, by default, Header will convert the parameter name to characters from underscore (_) to hyphen (-) to extract and document the headers.
# Also, HTTP headers are case-insensitive, so, you can declare them with standard Python style (also known as "snake_case")
# So, you can use user_agent as you normally would in Python code, instead of needing to capitalize the first letters as User_Agent or something similar
# If for some reason you need to disable automatic conversion of underscore to hyphesn, set the parameter convert_underscores of Header to False

# @app.get("/items")
# def read_items(strange_header: Optional[str] = Header(None)):
#   return {"strange_header": strange_header}

#
# Duplicated headers
#

@app.get("/items")
def read_items(x_token: Optional[List[str]] = Header(None)):
  return {"X-Token": x_token}
