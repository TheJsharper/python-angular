import unittest
from base_test import BaseTestCase


class TestPutUsers(BaseTestCase):
    def test_update_user(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin", "firstName": "Alice", "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["id"], 1)
        self.assertEqual(user["email"], "alice.updated@example.com")
        self.assertEqual(user["lastName"], "Updated")

    def test_update_user_not_found(self):
        response = self.client.put("/users/999", json={
            "id": 999, "name": "Nonexistent",
            "email": "nonexistent@example.com",
            "role": "admin", "firstName": "None", "lastName": "User",
        })
        self.assertEqual(response.status_code, 404)
        self.assertIn("User not found", response.text)

    def test_update_user_id_mismatch(self):
        response = self.client.put("/users/1", json={
            "id": 2, "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin", "firstName": "Alice", "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("id", response.text)

    def test_update_user_invalid_id(self):
        response = self.client.put("/users/1", json={
            "id": -1, "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin", "firstName": "Alice", "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("id", response.text)

    def test_update_user_invalid_data(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "", "email": "invalidemail",
            "role": "", "firstName": "", "lastName": "",
        })
        self.assertEqual(response.status_code, 422)

    def test_update_user_extra_fields(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin", "firstName": "Alice", "lastName": "Updated",
            "extraField": "This should not be allowed",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("extraField", response.text)

    def test_update_user_email_pattern(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "Alice Updated",
            "email": "invalidemailpattern",
            "role": "admin", "firstName": "Alice", "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 422)

    def test_update_user_email_too_long(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "Alice Updated",
            "email": "a" * 101 + "@example.com",
            "role": "admin", "firstName": "Alice", "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("email", response.text)

    def test_update_user_name_too_long(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "a" * 101,
            "email": "alice.updated@example.com",
            "role": "admin", "firstName": "Alice", "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("name", response.text)

    def test_update_user_role_too_long(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "a" * 51, "firstName": "Alice", "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("role", response.text)

    def test_update_user_first_name_too_long(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin", "firstName": "a" * 51, "lastName": "Updated",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("firstName", response.text)

    def test_update_user_last_name_too_long(self):
        response = self.client.put("/users/1", json={
            "id": 1, "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin", "firstName": "Alice", "lastName": "a" * 51,
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("lastName", response.text)


if __name__ == "__main__":
    unittest.main()
