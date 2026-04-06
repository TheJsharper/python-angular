import unittest
from test_common import BaseApiTestCase, client


class TestDeleteEndpoints(BaseApiTestCase):
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

    def test_delete_post_valid_id_message(self):
        response = client.delete("/posts/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Post deleted successfully")


if __name__ == "__main__":
    unittest.main()
