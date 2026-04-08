from pydantic import BaseModel, ConfigDict, Field, model_validator

class UserFields(BaseModel):
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


class UserCreate(UserFields):
    pass


class UserModify(UserFields):
    id: int = Field(..., gt=0)


class UserOptionalFields(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str | None = Field(None, min_length=1, max_length=100)
    email: str | None = Field(
        None,
        min_length=5,
        max_length=100,
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
    )
    role: str | None = Field(None, min_length=1, max_length=50)
    firstName: str | None = Field(None, min_length=1, max_length=50)
    lastName: str | None = Field(None, min_length=1, max_length=50)


class UserPartialModify(UserOptionalFields):
    id: int = Field(..., gt=0)

    @model_validator(mode="after")
    def validate_at_least_one_field(self):
        if all(
            value is None
            for value in (
                self.name,
                self.email,
                self.role,
                self.firstName,
                self.lastName,
            )
        ):
            raise ValueError("At least one field besides id must be provided")
        return self


class User(UserFields):
    id: int