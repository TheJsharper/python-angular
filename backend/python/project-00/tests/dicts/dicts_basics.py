import unittest


class DictsBasicsTestCase(unittest.TestCase):
    def test_dict_creation(self):
        # Arrange
        expected = {"name": "Alice", "age": 30}

        # Act
        result = dict(name="Alice", age=30)

        # Assert
        self.assertEqual(result, expected)

    def test_dict_access(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act
        name = my_dict["name"]
        age = my_dict["age"]

        # Assert
        self.assertEqual(name, "Alice")
        self.assertEqual(age, 30)

    def test_dict_update(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 31}

        # Act
        my_dict["age"] += 1

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_duplicates_not_allowed(self):
        # Arrange & Act
        # When a dictionary has duplicate keys, the last value overwrites the first one
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}

        # Assert
        # The second "year" value (2020) should overwrite the first one (1964)
        self.assertEqual(thisdict["year"], 2020)
        self.assertEqual(len(thisdict), 3)  # Only 3 items, not 4
        self.assertEqual(thisdict, {"brand": "Ford", "model": "Mustang", "year": 2020})

    def test_dict_items_mixed_data_types(self):
        # Arrange & Act
        # Dictionary values can be of any data type
        thisdict = {
            "brand": "Ford",
            "electric": False,
            "year": 1964,
            "colors": ["red", "white", "blue"]
        }

        # Assert
        self.assertEqual(thisdict["brand"], "Ford")
        self.assertIsInstance(thisdict["brand"], str)
        self.assertEqual(thisdict["electric"], False)
        self.assertIsInstance(thisdict["electric"], bool)
        self.assertEqual(thisdict["year"], 1964)
        self.assertIsInstance(thisdict["year"], int)
        self.assertEqual(thisdict["colors"], ["red", "white", "blue"])
        self.assertIsInstance(thisdict["colors"], list)

    def test_dict_type(self):
        # Arrange & Act
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Assert
        self.assertEqual(type(thisdict), dict)
        self.assertIsInstance(thisdict, dict)

    def test_dict_constructor(self):
        # Arrange & Act
        # Using the dict() constructor with keyword arguments
        thisdict = dict(name="John", age=36, country="Norway")

        # Assert
        self.assertEqual(thisdict["name"], "John")
        self.assertEqual(thisdict["age"], 36)
        self.assertEqual(thisdict["country"], "Norway")
        self.assertEqual(thisdict, {"name": "John", "age": 36, "country": "Norway"})
        self.assertEqual(type(thisdict), dict)


if __name__ == "__main__":
    unittest.main()
