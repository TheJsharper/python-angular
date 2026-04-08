import unittest
from base_test import BaseTestCase


class TestDeleteUsers(BaseTestCase):
    def test_delete_user_success(self):
        response = self.client.delete("/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "User deleted successfully")

    def test_delete_user_no_longer_exists(self):
        self.client.delete("/users/1")
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")

    def test_delete_user_removed_from_list(self):
        self.client.delete("/users/2")
        users = self.client.get("/users").json()
        self.assertFalse(any(u["id"] == 2 for u in users))

    def test_delete_user_not_found(self):
        response = self.client.delete("/users/999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")

    def test_delete_user_invalid_id(self):
        response = self.client.delete("/users/0")
        self.assertEqual(response.status_code, 422)

    def test_delete_user_negative_id(self):
        response = self.client.delete("/users/-1")
        self.assertEqual(response.status_code, 422)

    def test_delete_user_non_integer_id(self):
        response = self.client.delete("/users/abc")
        self.assertEqual(response.status_code, 422)
        self.assertIn("int_parsing", response.text)

    def test_delete_same_user_twice(self):
        self.client.delete("/users/1")
        response = self.client.delete("/users/1")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")


if __name__ == "__main__":
    unittest.main()
