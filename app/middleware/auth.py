from fastapi import status, Header, HTTPException, Request
from internal.tools.jwt import JWT
from typing import Optional

async def UseAuth(req: Request, authorization: Optional[str] = Header(None)):
    try:
        if authorization is None or not authorization.startswith("Bearer "): raise
        token = authorization.split(" ")[1]
        payload = JWT.authenticate(token)
        req.state.user = payload
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized action")