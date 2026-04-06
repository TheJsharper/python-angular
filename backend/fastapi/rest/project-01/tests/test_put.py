from test_common import BaseApiTestCase, client


class TestPutEndpoints(BaseApiTestCase):
    def test_put_post_not_found(self):
        update_data = {"title": "Updated Title", "content": "C" * 250}
        response = client.put("/posts/999", json=update_data)
        self.assertEqual(response.status_code, 404)

    def test_put_post_valid_update(self):
        update_data = {"title": "Updated Title", "content": "C" * 250}
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["id"], 1)
        self.assertEqual(data["title"], update_data["title"])
        self.assertEqual(data["content"], update_data["content"])

    def test_put_post_extra_fields_allowed_not_persisted(self):
        update_data = {
            "title": "Updated Title with Extra Fields",
            "content": "C" * 250,
            "extra_field1": "valid-extra",
            "extra_field2": "67890",
        }
        response = client.put("/posts/1", json=update_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertNotIn("extra_field1", data)
        self.assertNotIn("extra_field2", data)

    def test_put_post_invalid_payloads(self):
        self.assertEqual(client.put("/posts/1", json={"title": "Up", "content": "Short"}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={"title": "T" * 151, "content": "C" * 250}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={"title": "Valid Title", "content": "Short"}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={"title": "Valid Title", "content": "C" * 1001}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={"title": "Shrt", "content": "C" * 250}).status_code, 422)

    def test_put_post_boundary_values(self):
        self.assertEqual(client.put("/posts/1", json={"title": "Valid Title", "content": "C" * 250}).status_code, 200)
        self.assertEqual(client.put("/posts/1", json={"title": "Valid Title", "content": "C" * 1000}).status_code, 200)
        self.assertEqual(client.put("/posts/1", json={"title": "T" * 5, "content": "C" * 250}).status_code, 200)
        self.assertEqual(client.put("/posts/1", json={"title": "T" * 150, "content": "C" * 250}).status_code, 200)

    def test_put_post_extra_field_validation(self):
        self.assertEqual(client.put("/posts/1", json={"title": "Updated Title", "content": "C" * 250, "extra_field1": "valid", "extra_field2": 67890}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={"title": "Updated Title", "content": "C" * 250, "extra_field1": ""}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={"title": "Updated Title", "content": "C" * 250, "extra_field1": "   "}).status_code, 422)
        self.assertEqual(client.put("/posts/1", json={"title": "Updated Title", "content": "C" * 250, "extra_field1": "X" * 201}).status_code, 422)

    def test_put_post_transport_errors(self):
        self.assertEqual(client.put("/posts/1").status_code, 422)
        response = client.put("/posts/1", json={})
        self.assertEqual(response.status_code, 422)
        self.assertIn("error", response.json())
        self.assertEqual(client.put("/posts/1", data="This is not JSON").status_code, 422)

    def test_put_post_invalid_id(self):
        update_data = {"title": "Updated Title", "content": "C" * 250}
        self.assertEqual(client.put("/posts/abc", json=update_data).status_code, 422)
