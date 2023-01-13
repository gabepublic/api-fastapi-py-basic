from typing import Tuple
from app.schemas.user import (
    User, 
    MultipleUsersResponse
)
from app.exceptions import UserAlreadyExists, UserNotFound

users = {
    1: {
            "name": "jtest1",
            "id": 1,
            "desc": "short description of jtest1",
        },
    2: {
            "name": "jtest2",
            "id": 2,
            "desc": "short description of jtest2",
        },
}

class UserService:

    def __init__(self):
        pass

    @staticmethod
    def get_user_info(user_id: str = None) -> User:
        user = None
        if not user_id:
            user_content = users[1]
            user = User(**user_content)
        else:
            if (user_id in users.keys()):
                user_content = users[user_id]
                user = User(**user_content)
            else:
                raise UserNotFound(user_id=user_id)
        #print(user)
        return user

    @staticmethod
    def create_new_user(new_user: User) -> User:
        user_content = {
            "name": "jtest",
            "id": 1,
            "desc": "short description of jtest",
        }
        user = User(**user_content)
        #print(user)
        return user

    @staticmethod
    def get_all_users(limit: int) -> MultipleUsersResponse:
        print("limit: ", limit)
        list_users = list(users.values())
        limit_users = list_users[0 : limit]
        total_users = len(limit_users)
        print("Total users: ", total_users)
        response_users = MultipleUsersResponse(users=limit_users, 
                total=total_users)
        return response_users
