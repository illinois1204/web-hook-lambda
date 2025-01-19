from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse

from internal.tools.jwt import JWT, IToken

from ..middleware.auth import UseAuth
from ..schemas.auth.login import ILogin

Router = APIRouter()


@Router.post("/login")
def signIn(body: ILogin):
    try:
        print(body)
        return {"token": JWT.generate({"id": "uuid"})}
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": "Oops, something went wrong!"},
        )


@Router.get("/me", dependencies=[Depends(UseAuth)])
def me(req: Request):
    me: IToken = getattr(req.state, "user")
    return me


#######################################################################################
# @app.get("/liveness")
# def ping():
#     return {
#         "status": "ok",
#         "message": "app is alive!",
#         "ts": round(datetime.now().timestamp())
#     }


# @app.get("/ping-pong", status_code=204)
# def ping(): pass


# @app.get("/call-bell")
# def call(res: Response):
#     res.status_code = 204


# @app.get("/account/me")
# def ping():
#     print(f"env key is: {os.getenv("TOKEN")}")
#     return JSONResponse(content={"message": "no token"}, status_code=401)
