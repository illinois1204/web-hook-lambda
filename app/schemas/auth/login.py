from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

class ILogin(BaseModel):
    login: Annotated[EmailStr, Field(max_length=100)]
    password: str
    # password: Annotated[str, Field(min_length=5)]
    # password: str = Field(min_length=5)
