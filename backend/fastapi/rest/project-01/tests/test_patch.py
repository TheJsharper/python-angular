from test_common import BaseApiTestCase, client


class TestPatchEndpoints(BaseApiTestCase):
    def test_patch_post_partial_title(self):
        patch_data = {"title": "Patched Title"}
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], patch_data["title"])
        self.assertIn("content", data)

    def test_patch_post_partial_content(self):
        patch_data = {"content": "C" * 250}
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["content"], patch_data["content"])
        self.assertIn("title", data)

    def test_patch_post_not_found(self):
        response = client.patch("/posts/999", json={"title": "Patched Missing"})
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
        self.assertEqual(fetch_response.json(), original_data)

    def test_patch_post_extra_field_invalid_type(self):
        patch_data = {"title": "Patched Title", "extra_field1": 123}
        response = client.patch("/posts/1", json=patch_data)
        self.assertEqual(response.status_code, 422)

    def test_patch_post_transport_errors(self):
        self.assertEqual(client.patch("/posts/1", data="This is not JSON").status_code, 422)
        self.assertEqual(client.patch("/posts/1", json={}).status_code, 422)
        no_json_response = client.patch("/posts/1")
        self.assertEqual(no_json_response.status_code, 422)
        self.assertIn("error", no_json_response.json())

    def test_patch_post_valid_update_with_extras_denied(self):
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
        self.assertEqual(fetch_response.json(), original_data)
