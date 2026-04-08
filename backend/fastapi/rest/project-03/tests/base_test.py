import os
import sys
import importlib
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from database.users_store import reset_users_store


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        main_module = importlib.import_module("main")
        from fastapi.testclient import TestClient

        cls.client = TestClient(main_module.app)

    def setUp(self):
        reset_users_store()
