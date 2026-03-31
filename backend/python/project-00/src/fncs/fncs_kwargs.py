def fn_arg_keyword(**kwargs: dict[str, int]) -> dict[str, any]:
    """
    This function takes any number of keyword arguments and returns them as a dictionary.
    """
    if not kwargs:
        print("No keyword arguments provided.")
    elif len(kwargs) == 1:
        print("One keyword argument provided: " + str(kwargs))
    elif not isinstance(kwargs, dict):
        print("Invalid input. Please provide keyword arguments as a dictionary.")
    elif not all(isinstance(value, int) for value in kwargs.values()):
        print("All values must be integers.")
    elif not all(isinstance(key, str) for key in kwargs.keys()):
        print("All keys must be strings.")
    else:
        # print("Keyword arguments provided: " + str(kwargs))
        return kwargs
