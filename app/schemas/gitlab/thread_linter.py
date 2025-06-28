from typing import Annotated

from pydantic import BaseModel, Field


class IThreadLinter(BaseModel):
    project: int
    mr_iid: int
    access_token: str
    server: Annotated[str | None, Field(max_length=50)] = None
    # TODO: передача файла или содержимого линтера
