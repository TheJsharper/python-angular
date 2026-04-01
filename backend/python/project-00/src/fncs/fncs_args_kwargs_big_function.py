def bigFunction(*args: tuple[int, ...], **kwargs: dict[str, int]) -> None:
    if not args or not kwargs:
        print("No arguments provided.")
        return
    if len(args) > 5:
        print("Too many positional arguments. Maximum allowed is 5.")
        return
    if len(kwargs) > 5:
        print("Too many keyword arguments. Maximum allowed is 5.")
        return
    if any(not isinstance(arg, int) for arg in args):
        print("All positional arguments must be integers.")
        return
    if any(not isinstance(value, int) for value in kwargs.values()):
        print("All keyword argument values must be integers.")
        return
    if any(key == "" for key in kwargs.keys()):
        print("Keyword argument keys cannot be empty.")
        return
    if any(arg < 0 for arg in args):
        print("Positional arguments cannot be negative.")
        return
    if any(value < 0 for value in kwargs.values()):
        print("Keyword argument values cannot be negative.")
        return
    if len(set(args)) != len(args):
        print("Positional arguments must be unique.")
        return
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
