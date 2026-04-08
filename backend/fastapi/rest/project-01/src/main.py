from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from database import posts
from validation import Post, PostCreate, PostPatch
from pydantic import ValidationError

app = FastAPI(
    title="Project 01",
    description="A simple FastAPI application for demonstration purposes.",
    version="1.0.0",
)


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
