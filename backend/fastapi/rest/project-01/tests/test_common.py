from fastapi.testclient import TestClient
import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from main import app, reset_posts


client = TestClient(app)


class BaseApiTestCase(unittest.TestCase):
    def setUp(self):
        reset_posts()
