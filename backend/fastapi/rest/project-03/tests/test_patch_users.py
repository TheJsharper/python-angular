import unittest
from base_test import BaseTestCase


class TestPatchUsers(BaseTestCase):
    def test_patch_user_name(self):
        response = self.client.patch("/users/1", json={"id": 1, "name": "Alice Renamed"})
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["name"], "Alice Renamed")
        self.assertEqual(user["email"], "alice@example.com")

    def test_patch_user_email(self):
        response = self.client.patch("/users/1", json={"id": 1, "email": "alice.singlepatch@example.com"})
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["email"], "alice.singlepatch@example.com")
        self.assertEqual(user["name"], "alice")

    def test_patch_user_role(self):
        response = self.client.patch("/users/1", json={"id": 1, "role": "super-admin"})
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["role"], "super-admin")
        self.assertEqual(user["firstName"], "Alice")

    def test_patch_user_first_name(self):
        response = self.client.patch("/users/1", json={"id": 1, "firstName": "Alicia"})
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["firstName"], "Alicia")
        self.assertEqual(user["lastName"], "Johnson")

    def test_patch_user_last_name(self):
        response = self.client.patch("/users/1", json={"id": 1, "lastName": "Walker"})
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["lastName"], "Walker")
        self.assertEqual(user["firstName"], "Alice")

    def test_patch_user_multiple_fields(self):
        response = self.client.patch("/users/1", json={
            "id": 1, "email": "alice.patch@example.com", "lastName": "Patched",
        })
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["email"], "alice.patch@example.com")
        self.assertEqual(user["lastName"], "Patched")
        self.assertEqual(user["firstName"], "Alice")

    def test_patch_user_requires_field_besides_id(self):
        response = self.client.patch("/users/1", json={"id": 1})
        self.assertEqual(response.status_code, 422)
        self.assertIn("At least one field besides id must be provided", response.text)

    def test_patch_user_id_mismatch(self):
        response = self.client.patch("/users/1", json={"id": 2, "email": "alice.patch@example.com"})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["error"], "Path user_id must match body id")

    def test_patch_user_not_found(self):
        response = self.client.patch("/users/999", json={"id": 999, "email": "nonexistent@example.com"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")

    def test_patch_user_invalid_email(self):
        response = self.client.patch("/users/1", json={"id": 1, "email": "invalidemail"})
        self.assertEqual(response.status_code, 422)
        self.assertIn("email", response.text)

    def test_patch_user_empty_name(self):
        response = self.client.patch("/users/1", json={"id": 1, "name": ""})
        self.assertEqual(response.status_code, 422)
        self.assertIn("name", response.text)

    def test_patch_user_empty_role(self):
        response = self.client.patch("/users/1", json={"id": 1, "role": ""})
        self.assertEqual(response.status_code, 422)
        self.assertIn("role", response.text)

    def test_patch_user_empty_first_name(self):
        response = self.client.patch("/users/1", json={"id": 1, "firstName": ""})
        self.assertEqual(response.status_code, 422)
        self.assertIn("firstName", response.text)

    def test_patch_user_empty_last_name(self):
        response = self.client.patch("/users/1", json={"id": 1, "lastName": ""})
        self.assertEqual(response.status_code, 422)
        self.assertIn("lastName", response.text)

    def test_patch_user_extra_fields(self):
        response = self.client.patch("/users/1", json={
            "id": 1, "email": "alice.extra@example.com", "extra_field": "extra_value",
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn("extra_field", response.text)

    def test_patch_user_email_pattern(self):
        response = self.client.patch("/users/1", json={"id": 1, "email": "invalidemailpattern"})
        self.assertEqual(response.status_code, 422)
        self.assertIn("email", response.text)

    def test_patch_user_email_too_long(self):
        response = self.client.patch("/users/1", json={"id": 1, "email": "a" * 101 + "@example.com"})
        self.assertEqual(response.status_code, 422)
        self.assertIn("email", response.text)

    def test_patch_user_name_too_long(self):
        response = self.client.patch("/users/1", json={"id": 1, "name": "a" * 101})
        self.assertEqual(response.status_code, 422)
        self.assertIn("name", response.text)

    def test_patch_user_role_too_long(self):
        response = self.client.patch("/users/1", json={"id": 1, "role": "a" * 51})
        self.assertEqual(response.status_code, 422)
        self.assertIn("role", response.text)


if __name__ == "__main__":
    unittest.main()
