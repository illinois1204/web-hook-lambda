from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.controller.gitlab import add_linter_note
from app.schemas.gitlab.thread_linter import IThreadLinter
from internal.common.constants.http import Http500_Response

Router = APIRouter()


@Router.post("/thread/linter")
def _(body: IThreadLinter):
    try:
        if not add_linter_note(body):
            return JSONResponse(
                content={"message": "action failed"},
                status_code=status.HTTP_421_MISDIRECTED_REQUEST,
            )
    except Exception as e:
        print(e)
        return Http500_Response
