from fastapi import APIRouter
from app.schemas.user import (
    User,
    MultipleUsersResponse,
    CreateUserResponse
)
from app.services.user import UserService

user_router = APIRouter()
user_service = UserService()

@user_router.get("/user/me", response_model=User)
def user_me():
    user = user_service.get_user_info()
    #print(user)
    return user

@user_router.get("/user/him", response_model=User)
def user_him():
    user = user_service.get_user_info()
    return user

@user_router.get("/user/all", response_model=MultipleUsersResponse)
#@user_router.get("/user/all", response_model=User)
def get_all_users_with_limit():
    #print("limit: ", limit)
    users = user_service.get_all_users(10)
    #total_users = len(users)
    print("Total users: ", users.total)
    #obj_users = MultipleUsersResponse(users=users, total=total_users)
    return users

@user_router.get("/user/{user_id}", response_model=User)
def get_user_by_id(user_id: int):
    print("userid: ", user_id)
    user = user_service.get_user_info(user_id)
    #print(user)
    return user

@user_router.post("/users", response_model=CreateUserResponse)
def add_user(new_user: User):
    print("new user: ", new_user.userid)
    #return create_new_user(new_user)
    return CreateUserResponse(userid=new_user.userid)