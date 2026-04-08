from pydantic import BaseModel, ConfigDict, Field

class UserCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(
        ...,
        min_length=5,
        max_length=100,
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
    )
    role: str = Field(..., min_length=1, max_length=50)
    firstName: str = Field(..., min_length=1, max_length=50)
    lastName: str = Field(..., min_length=1, max_length=50)


class UserModify(UserCreate):
    id: int = Field(..., gt=0)


class User(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: int
    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    role: str = Field(..., min_length=1, max_length=50)
    firstName: str = Field(..., min_length=1, max_length=50)
    lastName: str = Field(..., min_length=1, max_length=50)