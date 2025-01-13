import jwt, os
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from typing import Optional

class IToken(BaseModel):
    id: str
    session: Optional[str]
    iat: Optional[str]
    exp: Optional[str]

class JWT:
    __algorithm = "HS256"

    @staticmethod
    def generate(payload: dict) -> str:
        meta = {
            "iat": datetime.now(tz=timezone.utc),
            "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=int(os.getenv("TOKEN_TTL")))
        }
        return jwt.encode({ **payload, **meta }, os.getenv("TOKEN_SECRET"), algorithm=JWT.__algorithm)

    @staticmethod
    def authenticate(token: str) -> IToken:
        return jwt.decode(token, os.getenv("TOKEN_SECRET"), algorithms=[JWT.__algorithm])
