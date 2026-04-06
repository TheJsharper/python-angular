from pydantic import BaseModel, ConfigDict, Field, model_validator

from .constants import (
    MAX_CONTENT_LENGTH,
    MAX_TITLE_LENGTH,
    MIN_CONTENT_LENGTH,
    MIN_TITLE_LENGTH,
)
from .validators import validate_extra_properties


class Post(BaseModel):
    id: int
    title: str = Field(..., min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH)
    content: str = Field(..., min_length=MIN_CONTENT_LENGTH, max_length=MAX_CONTENT_LENGTH)


class PostCreate(BaseModel):
    model_config = ConfigDict(extra="allow")

    title: str = Field(..., min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH)
    content: str = Field(..., min_length=MIN_CONTENT_LENGTH, max_length=MAX_CONTENT_LENGTH)

    @model_validator(mode="after")
    def validate_extra_fields(self):
        validate_extra_properties(self.__pydantic_extra__ or {})
        return self


class PostPatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str | None = Field(default=None, min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH)
    content: str | None = Field(default=None, min_length=MIN_CONTENT_LENGTH, max_length=MAX_CONTENT_LENGTH)

    @model_validator(mode="after")
    def validate_patch_payload(self):
        if self.title is None and self.content is None:
            raise ValueError("At least one of title or content is required")
        return self
