from fastapi import APIRouter, FastAPI
from dataclasses import dataclass
from typing import List
from . import admin


@dataclass
class IProvider:
    instance: APIRouter
    prefix: str

HttpProvider: List[IProvider] = [
    IProvider(instance=admin.Router, prefix="/admin")
]

def RegisterHTTP(app: FastAPI):
    for route in HttpProvider:
        app.include_router(route.instance, prefix=route.prefix)
        