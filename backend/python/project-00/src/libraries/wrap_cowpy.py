from typing import Any


class WrapCowpy:
    def __init__(self, cowpy: Any) -> None:
        self.cowpy = cowpy

    def say(self, message: str) -> str:
        if hasattr(self.cowpy, "milk_random_cow"):
            return self.cowpy.milk_random_cow(message)
        if hasattr(self.cowpy, "milk"):
            return self.cowpy.milk(message)
        raise AttributeError("cowpy object must provide milk_random_cow or milk")