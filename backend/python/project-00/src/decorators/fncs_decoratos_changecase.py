from collections.abc import Callable


def changeToUpperCase(func: Callable[[], str]) -> Callable[[], str]:
    def myInner():
        return func().upper()

    return myInner


def changeToLowerCase(func: Callable[[], str]) -> Callable[[], str]:
    def myInner():
        return func().lower()

    return myInner


def changeToArgumnentCase(case: str):
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        def myInner(*args: str) -> str:
            result = func(*args)
            if case == "upper":
                return result.upper()
            elif case == "lower":
                return result.lower()
            elif case == "title":
                return result.title()
            else:
                raise ValueError(
                    "Invalid case argument. Use 'upper', 'lower', or 'title'."
                )

        return myInner

    return decorator


def combineTwoStrings(func: Callable[[str, str], str]) -> Callable[[str, str], str]:
    def myInner(str1: str, str2: str) -> str:
        return func(str1, str2)

    return myInner


def combinteNStrings(func: Callable[..., str]) -> Callable[..., str]:
    def myInner(*args: str) -> str:
        return func(*args)

    return myInner


def changeToTitleCase(func: Callable[[], str]) -> Callable[[], str]:
    def myInner():
        return func().title()

    return myInner


def sum(fnc: Callable[[int, int], int]) -> Callable[[int, int], int]:
    def myInner(a: int, b: int) -> int:
        return fnc(a, b)

    return myInner


def multiply(fnc: Callable[[int, int], int]) -> Callable[[int, int], int]:
    def myInner(a: int, b: int) -> int:
        return fnc(a, b)

    return myInner


def divide(fnc: Callable[[int, int], int]) -> Callable[[int, int], int]:
    def myInner(a: int, b: int) -> int:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return fnc(a, b)

    return myInner
