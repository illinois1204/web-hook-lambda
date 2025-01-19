from typing import Annotated

from pydantic import BaseModel, EmailStr, Field


class ILogin(BaseModel):
    login: Annotated[EmailStr, Field(max_length=100)]
    password: str
    # password: Annotated[str, Field(min_length=5)]
    # password: str = Field(min_length=5)
