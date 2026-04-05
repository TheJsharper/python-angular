import os
import builtins
from collections.abc import Callable


_ORIGINAL_OPEN = builtins.open


class WrapperFileSystem:
    def __init__(self, file_system: Callable) -> None:
        self.file_system = file_system

    def read_file(self, file_path: str) -> str:
        opener = builtins.open if self.file_system is _ORIGINAL_OPEN else self.file_system
        with opener(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def write_file(self, file_path: str, content: str) -> None:
        opener = builtins.open if self.file_system is _ORIGINAL_OPEN else self.file_system
        with opener(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def delete_file(self, file_path: str) -> None:
        os.remove(file_path)
