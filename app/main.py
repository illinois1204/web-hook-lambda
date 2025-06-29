from fastapi import FastAPI

from app.routes import RegisterHTTP
from internal.constants.console_lights import ColorFG

app = FastAPI()
RegisterHTTP(app)
print(ColorFG.GREEN.format("INFO") + ":\t  App is running!")
