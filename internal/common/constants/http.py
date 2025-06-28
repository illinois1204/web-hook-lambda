from fastapi import responses, status

Http500_Response = responses.JSONResponse(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    content={"message": "Oops, something went wrong!"},
)
