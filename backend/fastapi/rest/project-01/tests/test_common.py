import os
import sys
import time
import importlib
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


def _load_client_with_retry(max_attempts=2):
    """Retry once to handle transient first-run import interruptions on Windows."""
    last_error = None
    for attempt in range(1, max_attempts + 1):
        try:
            testclient_module = importlib.import_module("fastapi.testclient")
            main_module = importlib.import_module("main")
            return testclient_module.TestClient(main_module.app), main_module.reset_posts
        except KeyboardInterrupt as exc:
            last_error = exc
            if attempt == max_attempts:
                raise
            time.sleep(0.2)
    raise last_error


client, reset_posts = _load_client_with_retry()


class BaseApiTestCase(unittest.TestCase):
    def setUp(self):
        reset_posts()

    def tearDown(self):
        reset_posts()
