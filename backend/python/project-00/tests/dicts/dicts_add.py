import unittest
class DictsAddTestCase(unittest.TestCase):
    def test_dict_add_with_assignment(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 30, "country": "USA"}

        # Act
        my_dict["country"] = "USA"

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_add_with_update_method(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 30, "country": "USA"}

        # Act
        my_dict.update({"country": "USA"})

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_add_with_multiple_keys(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 30, "country": "USA", "city": "New York"}

        # Act
        my_dict.update({"country": "USA", "city": "New York"})

        # Assert
        self.assertEqual(my_dict, expected)
if __name__ == "__main__":
    unittest.main()        