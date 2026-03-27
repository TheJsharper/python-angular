import unittest


class DictsUpdateTestCase(unittest.TestCase):
    def test_dict_update_with_assignment(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 31}

        # Act
        my_dict["age"] += 1

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_update_with_update_method(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 31}

        # Act
        my_dict.update({"age": 31})

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_update_with_new_key(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 30, "country": "USA"}

        # Act
        my_dict["country"] = "USA"

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_update_with_multiple_keys(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 31, "country": "USA"}

        # Act
        my_dict.update({"age": 31, "country": "USA"})

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_update_car_year_with_update_method(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        thisdict.update({"year": 2020})

        # Assert
        self.assertEqual(thisdict["year"], 2020)
        self.assertEqual(thisdict["brand"], "Ford")
        self.assertEqual(thisdict["model"], "Mustang")
        self.assertEqual(thisdict, {"brand": "Ford", "model": "Mustang", "year": 2020})

    def test_dict_update_with_invalid_set_input(self):
        # Arrange
        my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act & Assert
        with self.assertRaises(ValueError):
            my_dict.update({"non-existent", "wisch value"})

    def test_dict_assignment_with_non_existent_key(self):
        # Arrange
        my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        my_dict["non-existent"] = "wisch value"

        # Assert
        self.assertIn("non-existent", my_dict)
        self.assertEqual(my_dict["non-existent"], "wisch value")
        self.assertEqual(
            my_dict,
            {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964,
                "non-existent": "wisch value",
            },
        )


if __name__ == "__main__":
    unittest.main()
