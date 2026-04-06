from fastapi.testclient import TestClient
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from main import app, reset_posts

client = TestClient(app)


class TestMain(unittest.TestCase):
    def setUp(self):
        reset_posts()

    def test_get_posts(self):
        response = client.get("/posts")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 3)

    def test_get_post_by_id(self):
        response = client.get("/posts/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["id"], 1)

    def test_get_post_not_found(self):
        response = client.get("/posts/999")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertIn("error", data)

    def test_get_post_invalid_id(self):
        response = client.get("/posts/abc")
        self.assertEqual(response.status_code, 422)

    def test_create_post(self):
        new_post = {
            "title": "New Test Post",
            "content": "This is a new test post created during unit testing to verify the create_post endpoint functionality in detail. It includes a longer narrative that validates minimum content size behavior, keeps the test realistic, and ensures API validation accepts payloads that satisfy the configured 250 to 1000 character content rule.",
        }
        response = client.post("/posts", json=new_post)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertIn("id", data)
        self.assertEqual(data["title"], new_post["title"])
        self.assertEqual(data["content"], new_post["content"])

    def test_create_post_invalid_data(self):
        invalid_post = {
            "title": "Invalid Post",
            "content": "Short",
        }
        response = client.post("/posts", json=invalid_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_missing_fields(self):
        incomplete_post = {
            "title": "Incomplete Post",
        }
        response = client.post("/posts", json=incomplete_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_content_too_short(self):
        short_content_post = {
            "title": "Short Content Post",
            "content": "Too short",
        }
        response = client.post("/posts", json=short_content_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_content_too_long(self):
        long_content_post = {
            "title": "Long Content Post",
            "content": "L" * 1001,
        }
        response = client.post("/posts", json=long_content_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_title_too_long(self):
        long_title_post = {
            "title": "T" * 151,
            "content": "This is a valid content that meets the length requirements for testing the title length constraint in the create_post endpoint.",
        }
        response = client.post("/posts", json=long_title_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_title_too_short(self):
        short_title_post = {
            "title": "Shrt",
            "content": "This is a valid content that meets the length requirements for testing the title length constraint in the create_post endpoint.",
        }
        response = client.post("/posts", json=short_title_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_content_boundary(self):
        boundary_content_post = {
            "title": "Boundary Content Post",
            "content": "C" * 250,
        }
        response = client.post("/posts", json=boundary_content_post)
        self.assertEqual(response.status_code, 200)

    def test_create_post_content_boundary_max(self):
        boundary_content_post = {
            "title": "Boundary Content Post Max",
            "content": "C" * 1000,
        }
        response = client.post("/posts", json=boundary_content_post)
        self.assertEqual(response.status_code, 200)

    def test_create_post_title_boundary(self):
        boundary_title_post = {
            "title": "T" * 5,
            "content": "C" * 250,
        }
        response = client.post("/posts", json=boundary_title_post)
        self.assertEqual(response.status_code, 200)

    def test_create_post_title_boundary_max(self):
        boundary_title_post = {
            "title": "T" * 150,
            "content": "C" * 250,
        }
        response = client.post("/posts", json=boundary_title_post)
        self.assertEqual(response.status_code, 200)

    def test_create_post_extra_fields(self):
        extra_fields_post = {
            "title": "Extra Fields Post",
            "content": "This post includes extra fields that should be ignored by the API while valid fields are still accepted and persisted correctly. The content is intentionally extended so it satisfies the configured minimum length requirement and allows this test to focus on extra-field handling behavior rather than content validation boundaries.",
            "extra_field1": "This is an extra field that should not affect the post creation process.",
            "extra_field2": "12345",
        }
        response = client.post("/posts", json=extra_fields_post)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertIn("id", data)
        self.assertEqual(data["title"], extra_fields_post["title"])
        self.assertEqual(data["content"], extra_fields_post["content"])
        self.assertNotIn("extra_field1", data)
        self.assertNotIn("extra_field2", data)

        fetch_response = client.get(f"/posts/{data['id']}")
        self.assertEqual(fetch_response.status_code, 200)
        stored_data = fetch_response.json()
        self.assertNotIn("extra_field1", stored_data)
        self.assertNotIn("extra_field2", stored_data)

    def test_create_post_all_valid_properties(self):
        payload = {
            "title": "T" * 150,
            "content": "C" * 1000,
            "extra_field1": "valid-extra",
            "extra_field2": "E" * 200,
            "extra_field3": "ok",
        }
        response = client.post("/posts", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], payload["title"])
        self.assertEqual(data["content"], payload["content"])
        self.assertNotIn("extra_field1", data)
        self.assertNotIn("extra_field2", data)
        self.assertNotIn("extra_field3", data)

        fetch_response = client.get(f"/posts/{data['id']}")
        self.assertEqual(fetch_response.status_code, 200)
        stored_data = fetch_response.json()
        self.assertNotIn("extra_field1", stored_data)
        self.assertNotIn("extra_field2", stored_data)
        self.assertNotIn("extra_field3", stored_data)

    def test_create_post_extra_fields_invalid_type(self):
        extra_fields_post = {
            "title": "Extra Fields Invalid",
            "content": "C" * 250,
            "extra_field1": "valid extra",
            "extra_field2": 12345,
        }
        response = client.post("/posts", json=extra_fields_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_extra_field_empty(self):
        extra_fields_post = {
            "title": "Extra Field Empty",
            "content": "C" * 250,
            "extra_field1": "",
        }
        response = client.post("/posts", json=extra_fields_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_extra_field_whitespace(self):
        extra_fields_post = {
            "title": "Extra Field Whitespace",
            "content": "C" * 250,
            "extra_field1": "   ",
        }
        response = client.post("/posts", json=extra_fields_post)
        self.assertEqual(response.status_code, 422)

    def test_create_post_extra_field_too_long(self):
        extra_fields_post = {
            "title": "Extra Field Too Long",
            "content": "C" * 250,
            "extra_field1": "X" * 201,
        }
        response = client.post("/posts", json=extra_fields_post)
        self.assertEqual(response.status_code, 422)

    def test_post_create_requires_title_via_http(self):
        payload = {
            "content": "C" * 250,
        }
        response = client.post("/posts", json=payload)
        self.assertEqual(response.status_code, 422)

    def test_post_create_requires_content_via_http(self):
        payload = {
            "title": "Valid Title",
        }
        response = client.post("/posts", json=payload)
        self.assertEqual(response.status_code, 422)

    def test_put_post_not_found(self):
        update_data = {
            "title": "Updated Title",
            "content": "This is updated content that meets the length requirements for testing the update_post endpoint when the specified post ID does not exist.",
        }
        response = client.put("/posts/999", json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_put_post_invalid_data(self):
        update_data = {
            "title": "Up",
            "content": "Short",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_valid_update(self):
        update_data = {
            "title": "Updated Title",
            "content": "C" * 250,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], update_data["title"])
        self.assertEqual(data["content"], update_data["content"])

    def test_put_post_extra_fields(self):
        update_data = {
            "title": "Updated Title with Extra Fields",
            "content": "This is updated content that meets the length requirements for testing the update_post endpoint with valid data and extra fields. It ensures that the API correctly processes updates, ignores extra fields, and returns the expected response when all validation rules are satisfied.",
            "extra_field1": "This is an extra field that should be ignored during the update process.",
            "extra_field2": "67890",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], update_data["title"])
        self.assertEqual(data["content"], update_data["content"])
        self.assertNotIn("extra_field1", data)
        self.assertNotIn("extra_field2", data)

    def test_put_post_all_valid_properties(self):
        update_data = {
            "title": "T" * 150,
            "content": "C" * 1000,
            "extra_field1": "valid-extra",
            "extra_field2": "E" * 200,
            "extra_field3": "ok",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], update_data["title"])
        self.assertEqual(data["content"], update_data["content"])
        self.assertNotIn("extra_field1", data)
        self.assertNotIn("extra_field2", data)
        self.assertNotIn("extra_field3", data)

        fetch_response = client.get("/posts/1")
        self.assertEqual(fetch_response.status_code, 200)
        stored_data = fetch_response.json()
        self.assertNotIn("extra_field1", stored_data)
        self.assertNotIn("extra_field2", stored_data)
        self.assertNotIn("extra_field3", stored_data)

    def test_put_post_no_fields(self):
        update_data = {}
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_title_too_long(self):
        update_data = {
            "title": "T" * 151,
            "content": "This is a valid content that meets the length requirements for testing the title length constraint in the update_post endpoint.",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_content_too_short(self):
        update_data = {
            "title": "Valid Title",
            "content": "Short",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_content_too_long(self):
        update_data = {
            "title": "Valid Title",
            "content": "C" * 1001,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_title_too_short(self):
        update_data = {
            "title": "Shrt",
            "content": "This is a valid content that meets the length requirements for testing the title length constraint in the update_post endpoint.",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_boundary_content(self):
        update_data = {
            "title": "Valid Title",
            "content": "C" * 250,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)

    def test_put_post_boundary_content_max(self):
        update_data = {
            "title": "Valid Title",
            "content": "C" * 1000,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)

    def test_put_post_boundary_title(self):
        update_data = {
            "title": "T" * 5,
            "content": "C" * 250,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)

    def test_put_post_boundary_title_max(self):
        update_data = {
            "title": "T" * 150,
            "content": "C" * 250,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)

    def test_put_post_extra_fields_invalid_type(self):
        update_data = {
            "title": "Updated Title with Extra Fields",
            "content": "This is updated content that meets the length requirements for testing the update_post endpoint with valid data and extra fields. It ensures that the API correctly processes updates, ignores extra fields, and returns the expected response when all validation rules are satisfied.",
            "extra_field1": "This is an extra field that should be ignored during the update process.",
            "extra_field2": 67890,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_extra_field_empty(self):
        update_data = {
            "title": "Updated Title",
            "content": "C" * 250,
            "extra_field1": "",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_extra_field_whitespace(self):
        update_data = {
            "title": "Updated Title",
            "content": "C" * 250,
            "extra_field1": "   ",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_extra_field_too_long(self):
        update_data = {
            "title": "Updated Title",
            "content": "C" * 250,
            "extra_field1": "X" * 201,
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_no_fields(self):
        update_data = {}
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_nonexistent_id(self):
        update_data = {
            "title": "Updated Title",
            "content": "This is updated content that meets the length requirements for testing the update_post endpoint when the specified post ID does not exist.",
        }
        response = client.put("/posts/999", json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_put_post_invalid_id(self):
        update_data = {
            "title": "Updated Title",
            "content": "This is updated content that meets the length requirements for testing the update_post endpoint when the specified post ID is invalid.",
        }
        response = client.put("/posts/abc", json=update_data)
        self.assertEqual(response.status_code, 422)

    def test_patch_post_partial_title(self):
        patch_data = {
            "title": "Patched Title",
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], patch_data["title"])
        self.assertIn("content", data)

    def test_patch_post_partial_content(self):
        patch_data = {
            "content": "C" * 250,
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["content"], patch_data["content"])
        self.assertIn("title", data)

    def test_patch_post_not_found(self):
        patch_data = {
            "title": "Patched Missing",
        }
        response = client.patch("/posts/999", json=patch_data)
        self.assertEqual(response.status_code, 404)

    def test_patch_post_no_fields(self):
        response = client.patch("/posts/1", json={})
        self.assertEqual(response.status_code, 422)

    def test_patch_post_extra_fields_denied_and_not_persisted(self):
        original_response = client.get("/posts/1")
        self.assertEqual(original_response.status_code, 200)
        original_data = original_response.json()

        patch_data = {
            "title": "Patched Title with Extras",
            "extra_field1": "valid-extra",
            "extra_field2": "another-valid-extra",
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 422)

        fetch_response = client.get("/posts/1")
        self.assertEqual(fetch_response.status_code, 200)
        stored_data = fetch_response.json()
        self.assertEqual(stored_data, original_data)

    def test_patch_post_extra_field_invalid_type(self):
        patch_data = {
            "title": "Patched Title",
            "extra_field1": 123,
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 422)

    def test_put_post_no_json(self):
        response = client.put("/posts/1")
        self.assertEqual(response.status_code, 422)

    def test_put_post_empty_json_message(self):
        response = client.put("/posts/1", json={})
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())

    def test_put_post_empty_json(self):
        response = client.put("/posts/1", json={})
        self.assertEqual(response.status_code, 422)

    def test_put_post_invalid_json(self):
        response = client.put("/posts/1", data="This is not JSON")
        self.assertEqual(response.status_code, 422)

    def test_patch_post_invalid_json(self):
        response = client.patch("/posts/1", data="This is not JSON")
        self.assertEqual(response.status_code, 422)

    def test_patch_post_empty_json(self):
        response = client.patch("/posts/1", json={})
        self.assertEqual(response.status_code, 422)

    def test_patch_post_no_json(self):
        response = client.patch("/posts/1")
        self.assertEqual(response.status_code, 422)

    def test_patch_post_invalid_json(self):
        response = client.patch("/posts/1", data="This is not JSON")
        self.assertEqual(response.status_code, 422)

    def test_put_post_no_json(self):
        response = client.put("/posts/1")
        self.assertEqual(response.status_code, 422)

    def test_put_post_empty_json_message(self):
        response = client.put("/posts/1", json={})
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())

    def test_patch_post_empty_json(self):
        response = client.patch("/posts/1", json={})
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())

    def test_patch_post_no_json(self):
        response = client.patch("/posts/1")
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())

    def test_patch_post_invalid_json(self):
        response = client.patch("/posts/1", data="This is not JSON")
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())

    def test_patch_post_valid_update(self):
        original_response = client.get("/posts/1")
        self.assertEqual(original_response.status_code, 200)
        original_data = original_response.json()

        patch_data = {
            "title": "Partially Patched Title",
            "content": "This is partially updated content that meets the length requirements for testing the patch_post endpoint with valid data. It ensures that the API correctly processes partial updates, ignores extra fields, and returns the expected response when all validation rules are satisfied.",
            "extra_field1": "This is an extra field that should be ignored during the patch process.",
            "extra_field2": "67890",
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())

        fetch_response = client.get("/posts/1")
        self.assertEqual(fetch_response.status_code, 200)
        stored_data = fetch_response.json()
        self.assertEqual(stored_data, original_data)

    def test_patch_post_valid_partial_update(self):
        original_response = client.get("/posts/1")
        self.assertEqual(original_response.status_code, 200)
        original_data = original_response.json()

        patch_data = {
            "title": "Partially Patched Title",
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], patch_data["title"])
        self.assertEqual(data["content"], original_data["content"])

    def test_patch_post_valid_partial_update_content(self):
        original_response = client.get("/posts/1")
        self.assertEqual(original_response.status_code, 200)
        original_data = original_response.json()

        patch_data = {
            "content": "This is partially updated content that meets the length requirements for testing the patch_post endpoint with valid data. It ensures that the API correctly processes partial updates, ignores extra fields, and returns the expected response when all validation rules are satisfied.",
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], original_data["title"])
        self.assertEqual(data["content"], patch_data["content"])

    def test_patch_post_extra_fields_denied_and_not_persisted(self):
        original_response = client.get("/posts/1")
        self.assertEqual(original_response.status_code, 200)
        original_data = original_response.json()

        patch_data = {
            "title": "Patched Title with Extras",
            "extra_field1": "valid-extra",
            "extra_field2": "another-valid-extra",
        }
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 422)

        fetch_response = client.get("/posts/1")
        self.assertEqual(fetch_response.status_code, 200)
        stored_data = fetch_response.json()
        self.assertEqual(stored_data, original_data)

    def test_delete_post(self):
        response = client.delete("/posts/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)

        fetch_response = client.get("/posts/1")
        self.assertEqual(fetch_response.status_code, 404)

    def test_delete_post_not_found(self):
        response = client.delete("/posts/999")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("error", data)

    def test_delete_post_invalid_id(self):
        response = client.delete("/posts/abc")
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())

    def test_delete_post_valid_id(self):
        response = client.delete("/posts/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("message", data)
        self.assertEqual(data["message"], "Post deleted successfully")

    def test_delete_post_nonexistent_id(self):
        response = client.delete("/posts/999")
        self.assertEqual(response.status_code, 404)
        data = response.json()
        self.assertIn("error", data)
        self.assertEqual(data["error"], "Post not found")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
