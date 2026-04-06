from test_common import BaseApiTestCase, client


class TestPostEndpoints(BaseApiTestCase):
    def test_create_post(self):
        new_post = {
            "title": "New Test Post",
            "content": "This is a new test post created during unit testing to verify the create_post endpoint functionality in detail. It includes a longer narrative that validates minimum content size behavior, keeps the test realistic, and ensures API validation accepts payloads that satisfy the configured 250 to 1000 character content rule.",
        }
        response = client.post("/posts", json=new_post)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("id", data)
        self.assertEqual(data["title"], new_post["title"])
        self.assertEqual(data["content"], new_post["content"])

    def test_create_post_invalid_data(self):
        response = client.post("/posts", json={"title": "Invalid Post", "content": "Short"})
        self.assertEqual(response.status_code, 422)

    def test_create_post_missing_fields(self):
        response = client.post("/posts", json={"title": "Incomplete Post"})
        self.assertEqual(response.status_code, 422)

    def test_create_post_content_boundaries(self):
        self.assertEqual(client.post("/posts", json={"title": "Boundary Content Post", "content": "C" * 250}).status_code, 200)
        self.assertEqual(client.post("/posts", json={"title": "Boundary Content Post Max", "content": "C" * 1000}).status_code, 200)

    def test_create_post_title_boundaries(self):
        self.assertEqual(client.post("/posts", json={"title": "T" * 5, "content": "C" * 250}).status_code, 200)
        self.assertEqual(client.post("/posts", json={"title": "T" * 150, "content": "C" * 250}).status_code, 200)

    def test_create_post_extra_fields_allowed_not_persisted(self):
        payload = {
            "title": "Extra Fields Post",
            "content": "This post includes extra fields that should be ignored by the API while valid fields are still accepted and persisted correctly. The content is intentionally extended so it satisfies the configured minimum length requirement and allows this test to focus on extra-field handling behavior rather than content validation boundaries.",
            "extra_field1": "This is an extra field that should not affect the post creation process.",
            "extra_field2": "12345",
        }
        response = client.post("/posts", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertNotIn("extra_field1", data)
        self.assertNotIn("extra_field2", data)

    def test_create_post_extra_fields_invalid(self):
        self.assertEqual(client.post("/posts", json={"title": "Extra Fields Invalid", "content": "C" * 250, "extra_field1": "valid", "extra_field2": 12345}).status_code, 422)
        self.assertEqual(client.post("/posts", json={"title": "Extra Field Empty", "content": "C" * 250, "extra_field1": ""}).status_code, 422)
        self.assertEqual(client.post("/posts", json={"title": "Extra Field Whitespace", "content": "C" * 250, "extra_field1": "   "}).status_code, 422)
        self.assertEqual(client.post("/posts", json={"title": "Extra Field Too Long", "content": "C" * 250, "extra_field1": "X" * 201}).status_code, 422)

    def test_post_requires_fields_via_http(self):
        self.assertEqual(client.post("/posts", json={"content": "C" * 250}).status_code, 422)
        self.assertEqual(client.post("/posts", json={"title": "Valid Title"}).status_code, 422)
