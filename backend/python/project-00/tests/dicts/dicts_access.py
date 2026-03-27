import unittest
class DictsAccessTestCase(unittest.TestCase):
    def test_dict_access(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act
        name = my_dict["name"]
        age = my_dict["age"]

        # Assert
        self.assertEqual(name, "Alice")
        self.assertEqual(age, 30)

    def test_dict_access_non_existent_key(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act & Assert
        with self.assertRaises(KeyError):
            _ = my_dict["non_existent_key"]

    def test_dict_access_with_get_method(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act
        name = my_dict.get("name")
        non_existent_value = my_dict.get("non_existent_key")

        # Assert
        self.assertEqual(name, "Alice")
        self.assertIsNone(non_existent_value)

    def test_dict_key_presence_with_in_keyword(self):
        # Arrange
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Act
        has_model_key = "model" in thisdict
        has_color_key = "color" in thisdict

        # Assert
        self.assertTrue(has_model_key)
        self.assertFalse(has_color_key)

    def test_dict_keys(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30, "country": "USA"}

        # Act
        keys = my_dict.keys()

        # Assert
        self.assertIn("name", keys)
        self.assertIn("age", keys)
        self.assertIn("country", keys)
        self.assertEqual(len(keys), 3)
        # keys() returns a dict_keys object, which can be converted to a list
        self.assertEqual(sorted(list(keys)), ["age", "country", "name"])

    def test_dict_keys_is_a_view(self):
        # Arrange
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Act
        x = car.keys()
        
        # Assert - Before the change
        self.assertEqual(len(x), 3)
        self.assertIn("brand", x)
        self.assertIn("model", x)
        self.assertIn("year", x)
        
        # Act - Add a new key to the dictionary
        car["color"] = "white"
        
        # Assert - After the change, the keys view reflects the new key
        self.assertEqual(len(x), 4)
        self.assertIn("color", x)
        self.assertIn("brand", x)
        self.assertIn("model", x)
        self.assertIn("year", x)

    def test_dict_values(self):
        # Arrange
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Act
        x = car.values()

        # Assert - Before the change
        self.assertEqual(len(x), 3)
        self.assertIn("Ford", x)
        self.assertIn("Mustang", x)
        self.assertIn(1964, x)

        # Act - Change a value in the dictionary
        car["year"] = 2020

        # Assert - After the change, the values view reflects the new value
        self.assertEqual(len(x), 3)
        self.assertIn("Ford", x)
        self.assertIn("Mustang", x)
        self.assertIn(2020, x)
        self.assertNotIn(1964, x)

    def test_dict_values_is_a_view_when_adding_new_item(self):
        # Arrange
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Act
        x = car.values()

        # Assert - Before the change
        self.assertEqual(len(x), 3)
        self.assertIn("Ford", x)
        self.assertIn("Mustang", x)
        self.assertIn(1964, x)

        # Act - Add a new item to the dictionary
        car["color"] = "red"

        # Assert - After the change, the values view reflects the new item
        self.assertEqual(len(x), 4)
        self.assertIn("Ford", x)
        self.assertIn("Mustang", x)
        self.assertIn(1964, x)
        self.assertIn("red", x)

    def test_dict_items(self):
        # Arrange
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Act
        x = thisdict.items()

        # Assert
        self.assertEqual(len(x), 3)
        self.assertIn(("brand", "Ford"), x)
        self.assertIn(("model", "Mustang"), x)
        self.assertIn(("year", 1964), x)

    def test_dict_items_is_a_view_when_updating_value(self):
        # Arrange
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Act
        x = car.items()

        # Assert - Before the change
        self.assertEqual(len(x), 3)
        self.assertIn(("brand", "Ford"), x)
        self.assertIn(("model", "Mustang"), x)
        self.assertIn(("year", 1964), x)

        # Act - Update an existing value in the dictionary
        car["year"] = 2020

        # Assert - After the change, the items view reflects the new value
        self.assertEqual(len(x), 3)
        self.assertIn(("brand", "Ford"), x)
        self.assertIn(("model", "Mustang"), x)
        self.assertIn(("year", 2020), x)
        self.assertNotIn(("year", 1964), x)

    def test_dict_items_is_a_view_when_adding_new_item(self):
        # Arrange
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        # Act
        x = car.items()

        # Assert - Before the change
        self.assertEqual(len(x), 3)
        self.assertIn(("brand", "Ford"), x)
        self.assertIn(("model", "Mustang"), x)
        self.assertIn(("year", 1964), x)

        # Act - Add a new item to the dictionary
        car["color"] = "red"

        # Assert - After the change, the items view reflects the new item
        self.assertEqual(len(x), 4)
        self.assertIn(("brand", "Ford"), x)
        self.assertIn(("model", "Mustang"), x)
        self.assertIn(("year", 1964), x)
        self.assertIn(("color", "red"), x)

if __name__ == "__main__":
    unittest.main()