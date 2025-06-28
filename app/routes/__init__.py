from dataclasses import dataclass
from typing import List

from fastapi import APIRouter, FastAPI

from . import gitlab


@dataclass
class IProvider:
    instance: APIRouter
    prefix: str


HttpProvider: List[IProvider] = [IProvider(instance=gitlab.Router, prefix="/gitlab")]


def RegisterHTTP(app: FastAPI):
    for route in HttpProvider:
        app.include_router(route.instance, prefix=route.prefix)
