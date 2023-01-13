from fastapi import FastAPI

#from app.routes.user import user_router
# can be replaced with the following after setting app/__init__.py
from app import user_router
# or replaced with the following after setting app/routes/__init__.py 
#from app.routes import user_router

from app import test_router
from app.exeption_handlers import add_exception_handlers

app = FastAPI()
app.include_router(user_router)
app.include_router(test_router)
add_exception_handlers(app)
