from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(
        alias="name",
        title="Username",
        description="A short description about the username field.",
        min_length=2,
        default=None,
    )
    userid: int = Field(
        alias="id",
        title="UserID",
        description="The unique UserID",
        min=1
    )
    description: str = Field(
        alias="desc",
        title="User description",
        description="A short description about the description field.",
        min_length=2,
        default=None,
    )
    #profile: UserProfile

class MultipleUsersResponse(BaseModel):
    users: list[User]
    total: int

class CreateUserResponse(BaseModel):
    userid: int