#
# CORS (Cross-Origin Resource Sharing)
#

#
# Origin
#

'''
An origin is the combination of protocol (http, https),
domain (myapp.com, localhost, localhost.tiangolo.com)
and port (80, 443, 8080)

So, all these are different origins
- http://localhot
- https://localhost
- http://localhost:8080

Event if they are all in localhost, they use different protocols or ports, so, they are different "origins"
'''

#
# Steps
#

'''
So let's say you have a frontend running in your browser at https://localhost:8080,
and its JavaScript is trying to communicate with a backend running at http://localhost
(because we don't specify a port, the browser will assume the default port 80)

Then, the browser will send an HTTP OPTIONS request to the backend,
and if the backend sends the appropriate headers authorizing the communication from this different origin (http://localhost:8080)
then the browser will let the JavaScript in the frontend send its request to the backend.

To achieve this, the backend must have a list of "allowes origins"

In this case, it would have to include http://localhost:8080 for the frontend to work correctly
'''


#
# Wildcards
#

'''
It's also possible to declare the list as "*", (a "wildcard") to say that all are allowed.

But that will only allow certain types of communication, excluding everything that involves credentials:
Cookies, Authorization headers like those used with Bearer Token, etc

So, for everythong to work correctly, it's better to specify explicitly theo allowes origins
'''

#
# Use CORSMiddleware
#

'''
You can configure in your FastAPI application using CORSMiddleware
- Import CORSMiddlware
- Create a list of allowed origins (as strings)
- Add it as a "middleware" to your FastAPI application

You can also specify if your backend allows
- Credentials (Authorization headers, Cookies, etc), ...
- Specific HTTP method (POST, PUT) or all of them with the wildcard "*"
- Specific HTTP headers ỏ all of them with the wildcard "*"
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
  "http://localhost.tiangolo.com",
  "https://localhost.tiangolo.com",
  "http://localhost",
  "http://localhost:8080"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get("/")
def main():
  return {"message": "Hello World"}

'''
The following arguments are supported
- allow_origins - A list of origins that should be permitted to make cross-origin requests
- Eg: ["https://example.org", "https://www.example.org"]
- You can ["*"] to allow any origin

- allow_origin_regexp - A regex string to match against origins that should be permitted to make cross-origin requests
- Eg: "https://.*\.example\.org"

- allow_methods - A list of HTTP methods that should be allowed for cross-origin requests.
- Defaults to ["GET"]
- You can use ["*"] to allow all standard methods.

- allow_headers - A list of HTTP requests headers that should be supported for cross-origin requests.
- Defaults to "[]".
- You can use "[*]" to allow all headers.
- The Accept, Accept-Language, Content-Language and Content-Type headers are always allowed by CORS requests.

- allow_credentials - Indicate that cookies should be supported for cross-origin requests.
- Defaults to False.
- Also allow_origins cannot be set to ["*"] for credentials be allowed, origins must be specified

- expose_headers - Indicate any response headers that should be made accessible to the browser.
- Default to [].

- max_age = Sets a maximum time in seconds for browsers to cache CORS response.
- Default to 600.
'''

#
# CORS preflight requests
#

#
# Simple requests
#

#
# More info
#
