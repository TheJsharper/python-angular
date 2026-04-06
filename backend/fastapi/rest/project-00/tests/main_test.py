from fastapi.testclient import TestClient
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from main import app, reset_technologies

client = TestClient(app)


class MainTestCase(unittest.TestCase):

    def setUp(self):
        reset_technologies()
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

    def test_get_technologies_with_query(self):
        query_value = "Python"
        response = client.get(f"/technologies?query={query_value}")
        self.assertEqual(response.status_code, 200)
        technologies = response.json().get("technologies", [])
        self.assertIsInstance(technologies, list)
        self.assertGreater(len(technologies), 0)
        for tech in technologies:
            is_title_match = query_value.lower() in tech["title"].lower()

            is_description_match = query_value.lower() in tech["description"].lower()

            self.assertTrue(is_title_match or is_description_match)

    def test_get_technology_by_id(self):
        technology_id = 1
        response = client.get(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("technology", response.json())
        technology = response.json()["technology"]
        self.assertEqual(technology["id"], technology_id)
        self.assertIn("title", technology)
        self.assertIn("description", technology)
        self.assertIn("content", technology)

    def test_get_technology_by_id_not_found(self):
        technology_id = 999
        response = client.get(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["error"], "Technology not found")

    def test_get_technology_by_id_invalid(self):
        technology_id = "invalid"
        response = client.get(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())
        self.assertEqual(
            response.json()["detail"][0]["msg"],
            "Input should be a valid integer, unable to parse string as an integer",
        )

    def test_get_technology_by_id_negative(self):
        technology_id = -1
        response = client.get(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["error"], "Invalid technology ID")

    def test_get_technology_by_id_include_content(self):
        technology_id = 1
        response = client.get(f"/technologies/{technology_id}?include_content=true")
        self.assertEqual(response.status_code, 200)
        self.assertIn("technology", response.json())
        technology = response.json()["technology"]
        self.assertEqual(technology["id"], technology_id)
        self.assertIn("title", technology)
        self.assertIn("description", technology)
        self.assertIn("content", technology)

    def test_get_technology_by_id_exclude_content(self):
        technology_id = 1
        response = client.get(f"/technologies/{technology_id}?include_content=false")
        self.assertEqual(response.status_code, 200)
        self.assertIn("technology", response.json())
        technology = response.json()["technology"]
        self.assertEqual(technology["id"], technology_id)
        self.assertIn("title", technology)
        self.assertIn("description", technology)
        self.assertNotIn("content", technology)

    def test_create_technology(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 200)
        self.assertIn("technology", response.json())
        technology = response.json()["technology"]
        self.assertIn("id", technology)
        self.assertEqual(technology["title"], new_technology["title"])
        self.assertEqual(technology["description"], new_technology["description"])
        self.assertEqual(technology["content"], new_technology["content"])

    def test_create_technology_missing_fields(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform for developing, shipping, and running applications in containers.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content are required",
        )

    def test_create_technology_invalid_fields(self):
        new_technology = {
            "title": 123,
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content must be strings",
        )

    def test_create_technology_title_too_short(self):
        new_technology = {
            "title": "Doc",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_create_technology_description_too_short(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_create_technology_content_too_short(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Too short.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_create_technology_title_too_long(self):
        new_technology = {
            "title": "D" * 101,
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be 100 characters or less",
        )

    def test_create_technology_description_too_long(self):
        new_technology = {
            "title": "Docker",
            "description": "D" * 301,
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be 300 characters or less",
        )

    def test_create_technology_content_too_long(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "D" * 1001,
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be 1000 characters or less",
        )

    def test_create_technology_description_not_enough_alnum(self):
        new_technology = {
            "title": "Docker",
            "description": "!!!@@@###$$$%%%^^^&&&***((()))",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_create_technology_content_not_enough_alnum(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "!!!@@@###$$$%%%^^^&&&***((()))",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_create_technology_empty_title(self):
        new_technology = {
            "title": "",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_create_technology_empty_description(self):
        new_technology = {
            "title": "Docker",
            "description": "",
            "content": "A platform for developing, shipping, and running applications in containers.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_create_technology_empty_content(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_create_technology_all_fields_empty(self):
        new_technology = {
            "title": "",
            "description": "",
            "content": "",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_create_technology_all_fields_missing(self):
        new_technology = {}
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content are required",
        )

    def test_create_technology_all_fields_invalid(self):
        new_technology = {
            "title": 123,
            "description": 456,
            "content": 789,
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content must be strings",
        )

    def test_create_technology_title_only_whitespace(self):
        new_technology = {
            "title": "     ",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_create_technology_description_only_whitespace(self):
        new_technology = {
            "title": "Docker",
            "description": "     ",
            "content": "A platform for developing, shipping, and running applications in containers.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_create_technology_content_only_whitespace(self):
        new_technology = {
            "title": "Docker",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "     ",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_create_technology_title_whitespace_and_valid(self):
        new_technology = {
            "title": "   Docker   ",
            "description": "A platform for developing, shipping, and running applications in containers.",
            "content": "Docker simplifies application deployment and scaling.",
        }
        response = client.post("/technologies", json=new_technology)
        self.assertEqual(response.status_code, 200)
        self.assertIn("technology", response.json())
        technology = response.json()["technology"]
        self.assertIn("id", technology)
        self.assertEqual(technology["title"], new_technology["title"])
        self.assertEqual(technology["description"], new_technology["description"])
        self.assertEqual(technology["content"], new_technology["content"])

    def test_update_technology(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "An updated description for Python.",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 200)
        self.assertIn("technology", response.json())
        technology = response.json()["technology"]
        self.assertEqual(technology["id"], technology_id)
        self.assertEqual(technology["title"], updated_technology["title"])
        self.assertEqual(technology["description"], updated_technology["description"])
        self.assertEqual(technology["content"], updated_technology["content"])

    def test_update_technology_not_found(self):
        technology_id = 999
        updated_technology = {
            "title": "Updated Technology",
            "description": "An updated description.",
            "content": "Updated content.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["error"], "Technology not found")

    def test_update_technology_invalid_fields(self):
        technology_id = 1
        updated_technology = {
            "title": 123,
            "description": "An updated description for Python.",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content must be strings",
        )

    def test_update_technology_title_too_short(self):
        technology_id = 1
        updated_technology = {
            "title": "Up",
            "description": "An updated description for Python.",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_update_technology_description_too_short(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "Short",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_update_technology_content_too_short(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "An updated description for Python.",
            "content": "Short content.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_update_technology_title_too_long(self):
        technology_id = 1
        updated_technology = {
            "title": "U" * 101,
            "description": "An updated description for Python.",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be 100 characters or less",
        )

    def test_update_technology_description_too_long(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "D" * 301,
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be 300 characters or less",
        )

    def test_update_technology_content_too_long(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "An updated description for Python.",
            "content": "D" * 1001,
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be 1000 characters or less",
        )

    def test_update_technology_description_not_enough_alnum(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "!!!@@@###$$$%%%^^^&&&***((()))",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_update_technology_content_not_enough_alnum(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "An updated description for Python.",
            "content": "!!!@@@###$$$%%%^^^&&&***((()))",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_update_technology_empty_title(self):
        technology_id = 1
        updated_technology = {
            "title": "",
            "description": "An updated description for Python.",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_update_technology_empty_description(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_update_technology_empty_content(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "An updated description for Python.",
            "content": "",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_update_technology_all_fields_empty(self):
        technology_id = 1
        updated_technology = {
            "title": "",
            "description": "",
            "content": "",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_update_technology_all_fields_invalid(self):
        technology_id = 1
        updated_technology = {
            "title": 123,
            "description": 456,
            "content": 789,
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content must be strings",
        )

    def test_update_technology_title_only_whitespace(self):
        technology_id = 1
        updated_technology = {
            "title": "     ",
            "description": "An updated description for Python.",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title must be at least 5 characters long",
        )

    def test_update_technology_description_only_whitespace(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "     ",
            "content": "Updated content about Python.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Description must be at least 10 characters long",
        )

    def test_update_technology_content_only_whitespace(self):
        technology_id = 1
        updated_technology = {
            "title": "Updated Python",
            "description": "An updated description for Python.",
            "content": "     ",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Content must be at least 20 characters long",
        )

    def test_update_technology_not_found_invalid_id(self):
        technology_id = "invalid"
        updated_technology = {
            "title": "Updated Technology",
            "description": "An updated description.",
            "content": "Updated content.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())
        self.assertEqual(
            response.json()["detail"][0]["msg"],
            "Input should be a valid integer, unable to parse string as an integer",
        )

    def test_update_technology_not_found_negative_id(self):
        technology_id = -1
        updated_technology = {
            "title": "Updated Technology",
            "description": "An updated description.",
            "content": "Updated content.",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["error"], "Invalid technology ID")

    def test_update_technology_partial_update(self):
        technology_id = 1
        updated_technology = {
            "title": "Partially Updated Python",
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 200)
        self.assertIn("technology", response.json())
        technology = response.json()["technology"]
        self.assertEqual(technology["id"], technology_id)
        self.assertEqual(technology["title"], updated_technology["title"])
        self.assertIn("description", technology)
        self.assertIn("content", technology)

    def test_update_technology_no_fields(self):
        technology_id = 1
        updated_technology = {}
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content must be strings",
        )

    def test_update_technology_no_fields_invalid(self):
        technology_id = 1
        updated_technology = {
            "title": 123,
            "description": 456,
            "content": 789,
        }
        response = client.put(f"/technologies/{technology_id}", json=updated_technology)
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(
            response.json()["error"],
            "Title, description, and content must be strings",
        )

    def test_delete_technology(self):
        technology_id = 1
        response = client.delete(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Technology deleted successfully")

    def test_delete_technology_not_found(self):
        technology_id = 999
        response = client.delete(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["error"], "Technology not found")

    def test_delete_technology_invalid_id(self):
        technology_id = "invalid"
        response = client.delete(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 422)
        self.assertIn("detail", response.json())
        self.assertEqual(
            response.json()["detail"][0]["msg"],
            "Input should be a valid integer, unable to parse string as an integer",
        )

    def test_delete_technology_negative_id(self):
        technology_id = -1
        response = client.delete(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["error"], "Invalid technology ID")

    def test_delete_technology_already_deleted(self):
        technology_id = 1
        response = client.delete(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
        self.assertEqual(response.json()["message"], "Technology deleted successfully")

        response = client.delete(f"/technologies/{technology_id}")
        self.assertEqual(response.status_code, 404)
        self.assertIn("error", response.json())
        self.assertEqual(response.json()["error"], "Technology not found")

    def tearDown(self):
        reset_technologies()
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
