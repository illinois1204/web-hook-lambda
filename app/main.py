from app.routes import RegisterHTTP
from fastapi import FastAPI

app = FastAPI()
RegisterHTTP(app)
print(f"{'\033[92m'}INFO{'\033[0m'}:\t  App is running!")
