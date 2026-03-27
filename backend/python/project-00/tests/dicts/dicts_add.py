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

    def test_dict_update_with_set_of_strings_raises_value_error(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act & Assert
        # A set of plain strings has no key-value pairs, so update() raises ValueError
        with self.assertRaises(ValueError):
            my_dict.update({"invalid", "set"})

    def test_dict_update_with_set_of_integers_raises_value_error(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act & Assert
        # A set of integers is also invalid — each element must be a key-value pair
        with self.assertRaises(ValueError):
            my_dict.update({1, 2, 3})

if __name__ == "__main__":
    unittest.main()        