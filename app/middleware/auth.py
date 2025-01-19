from typing import Optional

from fastapi import Header, HTTPException, Request, status

from internal.tools.jwt import JWT


async def UseAuth(req: Request, authorization: Optional[str] = Header(None)):
    try:
        if authorization is None or not authorization.startswith("Bearer "):
            raise
        token = authorization.split(" ")[1]
        payload = JWT.authenticate(token)
        req.state.user = payload
    except:  # noqa: E722
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized action"
        )
