def fn_arg_integer(*args: tuple[int, ...]) -> None:
    # if not args or len(args) == 0 or all(arg is None for arg in args) or all(arg == 0 for arg in args) :
    if all(arg is None for arg in args):
        print("Arguments should not be None.")
    elif not all(isinstance(arg, int) for arg in args):
        print("It must be an integer.")
    elif  all(arg == 0 for arg in args):
        print("Arguments should not be zero.")
    else:
        print("Positional arguments:", args)
