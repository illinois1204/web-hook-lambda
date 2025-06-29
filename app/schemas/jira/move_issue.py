from typing import Annotated

from pydantic import BaseModel, Field


class IModeIssue(BaseModel):
    target_branch: str
    mr_event: Annotated[str | None, Field(max_length=50)] = None
