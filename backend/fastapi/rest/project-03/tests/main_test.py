import os
import sys
import time
import importlib
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Import the main module and create a test client
        cls.main_module = importlib.import_module("main")
        from fastapi.testclient import TestClient

        cls.client = TestClient(cls.main_module.app)

    def test_health_check(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_get_users(self):
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)

    def test_get_user_by_id(self):
        response = self.client.get("/users/1")
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["id"], 1)

    def test_get_user_not_found(self):
        response = self.client.get("/users/999")
        self.assertEqual(response.status_code, 404)
        error = response.json()
        self.assertEqual(error["error"], "User not found")

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
        invalid_user_data = {
            "name": "",
            "email": "invalidemail",
            "role": "",
            "firstName": "",
            "lastName": "",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_create_user_missing_fields(self):
        incomplete_user_data = {
            "name": "Incomplete User",
            "email": "incomplete@example.com",
        }
        response = self.client.post("/users", json=incomplete_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_create_user_extra_fields(self):
        extra_user_data = {
            "name": "Extra User",
            "email": "extra@example.com",
            "role": "user",
            "firstName": "Extra",
            "lastName": "User",
            "extraField": "This should not be here",
        }
        response = self.client.post("/users", json=extra_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_users_after_creation(self):
        # Create a new user first
        new_user_data = {
            "name": "Another User",
            "email": "another@example.com",
            "role": "user",
            "firstName": "Another",
            "lastName": "User",
        }
        response = self.client.post("/users", json=new_user_data)
        self.assertEqual(response.status_code, 200)

        # Now get the list of users and check if the new user is included
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        users = response.json()
        self.assertTrue(any(user["email"] == "another@example.com" for user in users))

    def test_get_user_by_id_after_creation(self):
        # Create a new user first
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

        # Now get the user by ID and check if it matches the created user
        response = self.client.get(f"/users/{new_user_id}")
        self.assertEqual(response.status_code, 200)
        user = response.json()
        self.assertEqual(user["id"], new_user_id)
        self.assertEqual(user["email"], "unique@example.com")

    def test_get_user_by_id_create_email_validation(self):
        # Create a new user with invalid email
        invalid_user_data = {
            "name": "Invalid Email User",
            "email": "invalidemail",
            "role": "user",
            "firstName": "Invalid",
            "lastName": "EmailUser",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_user_by_id_create_name_validation(self):
        # Create a new user with empty name
        invalid_user_data = {
            "name": "",
            "email": "invalid@example.com",
            "role": "user",
            "firstName": "Invalid",
            "lastName": "NameUser",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_user_by_id_create_role_validation(self):
        # Create a new user with empty role
        invalid_user_data = {
            "name": "Invalid Role User",
            "email": "invalidrole@example.com",
            "role": "",
            "firstName": "Invalid",
            "lastName": "RoleUser",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_user_by_id_create_firstName_validation(self):
        # Create a new user with empty firstName
        invalid_user_data = {
            "name": "Invalid FirstName User",
            "email": "invalidfirstname@example.com",
            "role": "user",
            "firstName": "",
            "lastName": "FirstNameUser",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_user_by_id_create_lastName_validation(self):
        # Create a new user with empty lastName
        invalid_user_data = {
            "name": "Invalid LastName User",
            "email": "invalidlastname@example.com",
            "role": "user",
            "firstName": "Invalid",
            "lastName": "",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_user_by_id_create_extra_field_validation(self):
        # Create a new user with an extra field
        invalid_user_data = {
            "name": "Invalid Extra Field User",
            "email": "invalidextrafield@example.com",
            "role": "user",
            "firstName": "Invalid",
            "lastName": "ExtraFieldUser",
            "extraField": "This should not be allowed",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_user_by_id_create_email_pattern_validation(self):
        # Create a new user with an email that doesn't match the pattern
        invalid_user_data = {
            "name": "Invalid Email Pattern User",
            "email": "invalidemailpattern",
            "role": "user",
            "firstName": "Invalid",
            "lastName": "EmailPatternUser",
        }
        response = self.client.post("/users", json=invalid_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_get_user_by_id_create_email_length_validation(self):
        # Create a new user with an email that is too long
        invalid_user_data = {
            "name": "Invalid Email Length User",
            "email": "a" * 101 + "@example.com",
            "role": "user",
            "firstName": "Invalid",
            "lastName": "EmailLengthUser",
        }
        response = self.client.post("/users", json=invalid_user_data)

        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("email", response.text)

    def test_update_user(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 200)
        updated_user = response.json()
        self.assertEqual(updated_user["id"], 1)
        self.assertEqual(updated_user["email"], "alice.updated@example.com")
        self.assertEqual(updated_user["lastName"], "Updated")

    def test_update_user_id_mismatch(self):
        updated_user_data = {
            "id": 2,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()["error"], "Path user_id must match body id")

    def test_update_user_not_found(self):
        updated_user_data = {
            "id": 999,
            "name": "Nonexistent User",
            "email": "nonexistent@example.com",
            "role": "user",
            "firstName": "Nonexistent",
            "lastName": "User",
        }
        response = self.client.put("/users/999", json=updated_user_data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "User not found")

    def test_update_user_invalid_data(self):
        updated_user_data = {
            "id": 1,
            "name": "",
            "email": "invalidemail",
            "role": "",
            "firstName": "",
            "lastName": "",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity^

    def test_update_user_extra_fields(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
            "extraField": "This should not be allowed",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_update_user_email_pattern_validation(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "invalidemailpattern",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_update_user_email_length_validation(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "a" * 101 + "@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("email", response.text)

    def test_update_user_name_length_validation(self):
        updated_user_data = {
            "id": 1,
            "name": "a" * 101,
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("name", response.text)

    def test_update_user_role_length_validation(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "a" * 51,
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("role", response.text)

    def test_update_user_firstName_length_validation(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "a" * 51,
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("firstName", response.text)

    def test_update_user_lastName_length_validation(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "a" * 51,
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("lastName", response.text)

    def test_update_user_extra_fields(self):
        updated_user_data = {
            "id": 1,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
            "extraField": "This should not be allowed",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("extraField", response.text)

    def test_update_user_id_validation(self):
        updated_user_data = {
            "id": -1,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("id", response.text)

    def test_update_user_id_mismatch(self):
        updated_user_data = {
            "id": 2,
            "name": "Alice Updated",
            "email": "alice.updated@example.com",
            "role": "admin",
            "firstName": "Alice",
            "lastName": "Updated",
        }
        response = self.client.put("/users/1", json=updated_user_data)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity
        self.assertIn("id", response.text)

    def test_update_user_not_found(self):
        updated_user_data = {
            "id": 999,
            "name": "Nonexistent User",
            "email": "nonexistent@example.com",
            "role": "admin",
            "firstName": "Nonexistent",
            "lastName": "User",
        }
        response = self.client.put("/users/999", json=updated_user_data)
        self.assertEqual(response.status_code, 404)  # Not Found
        self.assertIn("User not found", response.text)


if __name__ == "__main__":
    unittest.main()
