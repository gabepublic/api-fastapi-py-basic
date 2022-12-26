from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def home():
    return "Hello World"

@app.get("/company", response_class=JSONResponse)
def company():
    return {"name": "robot lab, inc.", \
        "noOfEmployee": 88}