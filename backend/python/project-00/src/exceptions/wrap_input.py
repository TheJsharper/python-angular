from collections.abc import Callable


class WrapInput:
    def __init__(self, input_func: Callable[[object], str]) -> None:
       
        self.input_func = input_func

    def __call__(self, prompt: str) -> str:
        try:
            return self.input_func(prompt)
        except Exception as e:
            message = str(e.args[0]) if isinstance(e, KeyError) and e.args else str(e)
            raise ValueError(f"An error occurred while getting input: {message}") from e
