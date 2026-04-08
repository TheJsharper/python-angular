import unittest
from base_test import BaseTestCase


class TestPostUsers(BaseTestCase):
    def test_create_user(self):
        new_user_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "role": "user",
            "firstName": "Test",
            "lastName": "User",
        }
        response = self.client.post("/users", json=new_user_data)
        self.assertEqual(response.status_code, 200)
        created_user = response.json()
        self.assertEqual(created_user["name"], new_user_data["name"])
        self.assertEqual(created_user["email"], new_user_data["email"])
        self.assertEqual(created_user["role"], new_user_data["role"])
        self.assertEqual(created_user["firstName"], new_user_data["firstName"])
        self.assertEqual(created_user["lastName"], new_user_data["lastName"])

    def test_create_user_invalid_data(self):
        response = self.client.post("/users", json={
            "name": "", "email": "invalidemail",
            "role": "", "firstName": "", "lastName": "",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_missing_fields(self):
        response = self.client.post("/users", json={
            "name": "Incomplete User",
            "email": "incomplete@example.com",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_extra_fields(self):
        response = self.client.post("/users", json={
            "name": "Extra User", "email": "extra@example.com",
            "role": "user", "firstName": "Extra", "lastName": "User",
            "extraField": "This should not be here",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_invalid_email(self):
        response = self.client.post("/users", json={
            "name": "User", "email": "invalidemail",
            "role": "user", "firstName": "A", "lastName": "B",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_invalid_email_pattern(self):
        response = self.client.post("/users", json={
            "name": "User", "email": "invalidemailpattern",
            "role": "user", "firstName": "A", "lastName": "B",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_email_too_long(self):
        response = self.client.post("/users", json={
            "name": "User", "email": "a" * 101 + "@example.com",
            "role": "user", "firstName": "A", "lastName": "B",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("email", response.text)

    def test_create_user_empty_name(self):
        response = self.client.post("/users", json={
            "name": "", "email": "valid@example.com",
            "role": "user", "firstName": "A", "lastName": "B",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_empty_role(self):
        response = self.client.post("/users", json={
            "name": "User", "email": "valid@example.com",
            "role": "", "firstName": "A", "lastName": "B",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_empty_first_name(self):
        response = self.client.post("/users", json={
            "name": "User", "email": "valid@example.com",
            "role": "user", "firstName": "", "lastName": "B",
        })
        self.assertEqual(response.status_code, 422)

    def test_create_user_empty_last_name(self):
        response = self.client.post("/users", json={
            "name": "User", "email": "valid@example.com",
            "role": "user", "firstName": "A", "lastName": "",
        })
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
