from fastapi.testclient import TestClient
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from main import app

client = TestClient(app)


class MainTestCase(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_app_initialization(self):
        self.assertIsNotNone(app)
        self.assertEqual(app.title, "Project 00")
        self.assertEqual(
            app.description,
            "A simple FastAPI application for demonstration purposes.",
        )
        self.assertEqual(app.version, "1.0.0")

    def test_read_root(self):
        response = client.get("/")
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to Project 00!"})

    def test_get_technologies(self):
        response = client.get("/technologies")
        self.assertEqual(response.status_code, 200)
        self.assertIn("technologies", response.json())
        self.assertIsInstance(response.json()["technologies"], list)
        self.assertGreater(len(response.json()["technologies"]), 0)

    def test_get_technologies_content(self):
        response = client.get("/technologies")
        self.assertEqual(response.status_code, 200)
        technologies = response.json().get("technologies", [])
        self.assertIsInstance(technologies, list)
        self.assertGreater(len(technologies), 0)
        for tech in technologies:
            self.assertIn("id", tech)
            self.assertIn("title", tech)
            self.assertIn("description", tech)
            self.assertIn("content", tech)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
