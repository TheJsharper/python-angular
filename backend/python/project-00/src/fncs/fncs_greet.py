def greet(name: str, greeting: str = "Hello") -> None:
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    if not isinstance(greeting, str):
        raise ValueError("Greeting must be a string")

    print(greeting + ", " + name)
