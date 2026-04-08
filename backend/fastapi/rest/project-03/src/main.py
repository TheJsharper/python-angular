from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from database.users_store import build_default_users
from validation.user_schemas import User, UserCreate, UserModify

app = FastAPI(
    title="Project 03",
    description="FastAPI sample project with simple dev/prod scripts",
    version="1.0.0",
)


@app.get("/health")
async def health_check():
    return JSONResponse(content={"status": "ok"})


@app.get("/users", response_model=list[User])
async def get_users() -> list[dict]:

    users = build_default_users()

    return users


@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int) -> User | JSONResponse:
    users = build_default_users()
    user = next((user for user in users if user["id"] == user_id), None)

    if user is None:
        return JSONResponse(content={"error": "User not found"}, status_code=404)

    return user


@app.post("/users", response_model=User)
async def create_user(user: UserCreate) -> User:
    users = build_default_users()
    new_id = max(existing_user["id"] for existing_user in users) + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email,
        "role": user.role,
        "firstName": user.firstName,
        "lastName": user.lastName,
    }
    users.append(new_user)
    return User(**new_user)


@app.put("/users/{user_id}", response_model=User)
async def update_user(
    user_id: int = Path(..., gt=0), user_update: UserModify = ...
) -> User | JSONResponse:
    users = build_default_users()
    user_index = next(
        (index for index, user in enumerate(users) if user["id"] == user_id), None
    )

    if user_index is None:
        return JSONResponse(content={"error": "User not found"}, status_code=404)

    if user_update.id != user_id:
        return JSONResponse(
            content={"error": "Path user_id must match body id"}, status_code=422
        )

    updated_user = {
        "id": user_update.id,
        "name": user_update.name,
        "email": user_update.email,
        "role": user_update.role,
        "firstName": user_update.firstName,
        "lastName": user_update.lastName,
    }
    users[user_index] = updated_user
    return User(**updated_user)
