from test_common import BaseApiTestCase, client


class TestGetEndpoints(BaseApiTestCase):
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
