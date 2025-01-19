import os
from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from pydantic import BaseModel


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
            "exp": datetime.now(tz=timezone.utc)
            + timedelta(seconds=int(os.getenv("TOKEN_TTL", 0))),
        }
        return jwt.encode(  # type: ignore
            {**payload, **meta}, os.getenv("TOKEN_SECRET"), algorithm=JWT.__algorithm
        )

    @staticmethod
    def authenticate(token: str) -> IToken:
        return jwt.decode(  # type: ignore[attr-defined]
            token, os.getenv("TOKEN_SECRET"), algorithms=[JWT.__algorithm]
        )
