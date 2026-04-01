def require_auth(func: callable):
    def wrapper(user: str):
        if not user == "authenticated_user":
            raise Exception("User must be authenticated to access this function.")
        return func(user)

    return wrapper
