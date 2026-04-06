import os
import sys
import time
import importlib
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


def _clear_transient_imports():
    prefixes = (
        "fastapi",
        "starlette",
        "anyio",
        "httpx",
        "rich",
        "email_validator",
        "main",
    )
    for module_name in list(sys.modules):
        if module_name.startswith(prefixes):
            sys.modules.pop(module_name, None)
