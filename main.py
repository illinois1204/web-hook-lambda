from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from datetime import datetime
import os

app = FastAPI()
print("App is running!")

@app.get("/liveness")
def ping():
    return {
        "status": "ok",
        "message": "app is alive!",
        "ts": round(datetime.now().timestamp())
    }


@app.get("/ping-pong", status_code=204)
def ping(): pass


@app.get("/call-bell")
def call(res: Response):
    res.status_code = 204


@app.get("/account/me")
def ping():
    print(f"env key is: {os.getenv("TOKEN")}")
    return JSONResponse(content={"message": "no token"}, status_code=401)
