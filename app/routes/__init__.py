from dataclasses import dataclass
from typing import List

from fastapi import APIRouter, FastAPI

from . import gitlab, jira


@dataclass
class IProvider:
    instance: APIRouter
    prefix: str


HttpProvider: List[IProvider] = [
    IProvider(instance=gitlab.Router, prefix="/gitlab"),
    IProvider(instance=jira.Router, prefix="/jira/dc"),
]


def RegisterHTTP(app: FastAPI):
    for route in HttpProvider:
        app.include_router(route.instance, prefix=route.prefix)
