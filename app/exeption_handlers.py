from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.exceptions import UserAlreadyExists, UserNotFound

def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(UserNotFound)
    async def handle_user_not_found_exception(
        request: Request, exc: UserNotFound
    ) -> JSONResponse:
        #logger.error(f"Non-existent user_id: {exc.user_id} was requested")
        return JSONResponse(status_code=404, content="User doesn't exist")
    
    return None