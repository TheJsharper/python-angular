import unittest
from base_test import BaseTestCase


class TestGetUsers(BaseTestCase):
    def test_get_users(self):
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)

    def test_get_users_after_creation(self):
        new_user_data = {
            "name": "Another User",
            "email": "another@example.com",
            "role": "user",
            "firstName": "Another",
            "lastName": "User",
        }
        response = self.client.post("/users", json=new_user_data)
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertTrue(any(user["email"] == "another@example.com" for user in users))


if __name__ == "__main__":
    unittest.main()
