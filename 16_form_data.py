from fastapi import FastAPI, Form

app = FastAPI()

#
# Import Form
#

# @app.post("/login")
# def login(user_name: str = Form(...), password: str = Form(...)):
#   return {"user_name": user_name}
