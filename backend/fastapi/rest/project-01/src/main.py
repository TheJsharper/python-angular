from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

app = FastAPI(
    title="Project 01",
    description="A simple FastAPI application for demonstration purposes.",
    version="1.0.0",
)

MIN_TITLE_LENGTH = 5
MAX_TITLE_LENGTH = 150
MIN_CONTENT_LENGTH = 250
MAX_CONTENT_LENGTH = 1000


def _validate_extra_properties(extra_properties: dict):
    for key, value in extra_properties.items():
        if not isinstance(value, str):
            raise ValueError(f"Extra property '{key}' must be a string")
        if len(value.strip()) == 0:
            raise ValueError(f"Extra property '{key}' cannot be empty")
        if len(value.strip()) > 200:
            raise ValueError(f"Extra property '{key}' must be 200 characters or less")


class Post(BaseModel):
    id: int
    title: str = Field(
        ..., min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH, required=True
    )
    content: str = Field(
        ..., min_length=MIN_CONTENT_LENGTH, max_length=MAX_CONTENT_LENGTH, required=True
    )


class PostCreate(BaseModel):
    model_config = ConfigDict(extra="allow")

    title: str = Field(
        ..., min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH, required=True
    )
    content: str = Field(
        ..., min_length=MIN_CONTENT_LENGTH, max_length=MAX_CONTENT_LENGTH, required=True
    )

    @model_validator(mode="after")
    def validate_extra_properties(self):
        _validate_extra_properties(self.__pydantic_extra__ or {})
        return self


class PostPatch(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str | None = Field(
        default=None, min_length=MIN_TITLE_LENGTH, max_length=MAX_TITLE_LENGTH
    )
    content: str | None = Field(
        default=None, min_length=MIN_CONTENT_LENGTH, max_length=MAX_CONTENT_LENGTH
    )

    @model_validator(mode="after")
    def validate_patch_payload(self):
        if self.title is None and self.content is None:
            raise ValueError("At least one of title or content is required")
        return self


def build_default_posts():
    default_posts = [
        {
            "id": 1,
            "title": "First Post",
            "content": "This is the first post and it now includes a much more complete narrative for testing constraints. It explains the scenario, gives context, and adds enough detail to make the body substantial. The goal is to ensure the content length falls within the required limits.",
        },
        {
            "id": 2,
            "title": "Second Post",
            "content": "This is the second post and it is intentionally verbose so validation rules can be verified in unit tests. It describes a practical example, highlights expected behavior, and adds extra explanation so the text comfortably passes the minimum content threshold requirement.",
        },
        {
            "id": 3,
            "title": "Third Post",
            "content": "This is the third post with extended content designed to satisfy boundary checks for API data quality. It includes descriptive language, test-friendly structure, and enough characters to remain valid while still being concise enough to stay below the maximum limit.",
        },
    ]

    for post in default_posts:
        Post.model_validate(post)

    return default_posts


posts = build_default_posts()


def reset_posts():
    posts.clear()
    posts.extend(build_default_posts())


@app.get("/posts")
def get_posts() -> JSONResponse:
    return JSONResponse(content=posts)


@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post is None:
        return JSONResponse(content={"error": "Post not found"}, status_code=404)

    try:
        return Post(**post)
    except ValidationError:
        return JSONResponse(content={"error": "Invalid post data"}, status_code=500)


@app.post("/posts", response_model=Post)
def create_post(post: PostCreate):
    new_id = max(existing_post["id"] for existing_post in posts) + 1 if posts else 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content,
    }
    posts.append(new_post)
    return new_post


@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post: dict):
    existing_post = next((post for post in posts if post["id"] == post_id), None)
    if existing_post is None:
        return JSONResponse(content={"error": "Post not found"}, status_code=404)

    try:
        validated_post = PostCreate.model_validate(post)
        updated_post = Post(
            id=post_id,
            title=validated_post.title,
            content=validated_post.content,
        )
        existing_post.update(updated_post.model_dump())
        return updated_post
    except ValidationError:
        return JSONResponse(content={"error": "Invalid post data"}, status_code=422)


@app.patch("/posts/{post_id}", response_model=Post)
def patch_post(post_id: int, post: object = Body(default=None)):
    existing_post = next((post for post in posts if post["id"] == post_id), None)
    if existing_post is None:
        return JSONResponse(content={"error": "Post not found"}, status_code=404)

    if post is None:
        return JSONResponse(content={"error": "Invalid post data"}, status_code=422)

    if not isinstance(post, dict):
        return JSONResponse(content={"error": "Invalid post data"}, status_code=422)

    try:
        validated_post = PostPatch.model_validate(post)
        patch_data = {}
        if validated_post.title is not None:
            patch_data["title"] = validated_post.title
        if validated_post.content is not None:
            patch_data["content"] = validated_post.content

        merged_post = {**existing_post, **patch_data}
        updated_post = Post.model_validate(merged_post)
        existing_post.update(updated_post.model_dump())
        return updated_post
    except ValidationError:
        return JSONResponse(content={"error": "Invalid post data"}, status_code=422)


@app.delete("/posts/{post_id}")
def delete_post(post_id: str):
    try:
        parsed_post_id = int(post_id)
    except ValueError:
        return JSONResponse(content={"error": "Invalid post ID"}, status_code=422)

    existing_post = next((post for post in posts if post["id"] == parsed_post_id), None)
    if existing_post is None:
        return JSONResponse(content={"error": "Post not found"}, status_code=404)

    posts.remove(existing_post)
    return {"message": "Post deleted successfully"}
