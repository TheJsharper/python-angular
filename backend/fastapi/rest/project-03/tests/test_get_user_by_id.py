import unittest
from base_test import BaseTestCase


class TestGetUserById(BaseTestCase):
    def test_get_user_by_id(self):
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["id"], 1)

    def test_get_user_not_found(self):
        response = self.client.get("/users/999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")

    def test_get_user_by_id_after_creation(self):
        new_user_data = {
            "name": "Unique User",
            "email": "unique@example.com",
            "role": "user",
            "firstName": "Unique",
            "lastName": "User",
        }
        response = self.client.post("/users", json=new_user_data)
        self.assertEqual(response.status_code, 200)
        created_user = response.json()
        new_user_id = created_user["id"]

        response = self.client.get(f"/users/{new_user_id}")
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["id"], new_user_id)
        self.assertEqual(user["email"], "unique@example.com")


if __name__ == "__main__":
    unittest.main()
