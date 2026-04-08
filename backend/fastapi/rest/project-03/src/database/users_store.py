DEFAULT_USERS = [
    {
        "id": 1,
        "name": "alice",
        "email": "alice@example.com",
        "firstName": "Alice",
        "lastName": "Johnson",
        "role": "admin",
    },
    {
        "id": 2,
        "name": "bob",
        "email": "bob@example.com",
        "firstName": "Bob",
        "lastName": "Smith",
        "role": "user",
    },
    {
        "id": 3,
        "name": "charlie",
        "email": "charlie@example.com",
        "firstName": "Charlie",
        "lastName": "Brown",
        "role": "user",
    },
]

_users = [user.copy() for user in DEFAULT_USERS]


def build_default_users():
    return _users
