from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.controller import jira
from app.schemas.jira.move_issue import IModeIssue
from internal.constants.http import Http500_Response

Router = APIRouter()


@Router.post("/thread/linter")
def _(body: IModeIssue):
    try:
        issue_list = jira.extract_issue_list(body.target_branch)
        if len(issue_list) == 0:
            print(
                "Can't find the task id, apparently this commit does not relate to any task."
            )
            return

        unhandled = jira.move_issue(issue_list, body.mr_event)
        if len(unhandled):
            return JSONResponse(
                content={
                    "message": "The following tasks were not processed",
                    "list": unhandled,
                },
                status_code=status.HTTP_206_PARTIAL_CONTENT,
            )
    except Exception as e:
        print(e)
        return Http500_Response
