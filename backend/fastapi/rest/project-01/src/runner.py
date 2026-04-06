import os
import unittest
from pathlib import Path

import uvicorn


BASE_DIR = Path(__file__).resolve().parent
TESTS_DIR = BASE_DIR.parent / "tests"


def dev() -> None:
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host=host, port=port, reload=True, app_dir=str(BASE_DIR))


def prod() -> None:
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    workers = int(os.getenv("WEB_CONCURRENCY", "1"))
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=False,
        workers=workers,
        app_dir=str(BASE_DIR),
    )


def test() -> None:
    suite = unittest.defaultTestLoader.discover(str(TESTS_DIR), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
