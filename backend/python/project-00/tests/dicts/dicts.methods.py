import unittest


class DictsMethodsTestCase(unittest.TestCase):
    def test_dict_methods_keys(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected_keys = ["name", "age"]

        # Act
        keys = list(my_dict.keys())

        # Assert
        self.assertEqual(keys, expected_keys)

    def test_dict_methods_values(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected_values = ["Alice", 30]

        # Act
        values = list(my_dict.values())

        # Assert
        self.assertEqual(values, expected_values)

    def test_dict_methods_items(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected_items = [("name", "Alice"), ("age", 30)]

        # Act
        items = list(my_dict.items())

        # Assert
        self.assertEqual(items, expected_items)

    def test_dict_methods_clear(self):
        # Arrange
        my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        my_dict.clear()

        # Assert
        self.assertEqual(my_dict, {})
        self.assertEqual(len(my_dict), 0)

    def test_dict_methods_copy(self):
        # Arrange
        my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        copied_dict = my_dict.copy()

        # Assert
        self.assertEqual(copied_dict, my_dict)
        self.assertIsNot(copied_dict, my_dict)

    def test_dict_methods_fromkeys(self):
        # Arrange
        keys = ("key1", "key2", "key3")
        value = 0
        expected = {"key1": 0, "key2": 0, "key3": 0}

        # Act
        result = dict.fromkeys(keys, value)

        # Assert
        self.assertEqual(result, expected)

    def test_dict_methods_get(self):
        # Arrange
        my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        model = my_dict.get("model")

        # Assert
        self.assertEqual(model, "Mustang")

    def test_dict_methods_items_returns_tuples_for_each_pair(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        items_list = list(thisdict.items())

        # Assert
        self.assertEqual(items_list, [("brand", "Ford"), ("model", "Mustang"), ("year", 1964)])
        self.assertTrue(all(isinstance(item, tuple) and len(item) == 2 for item in items_list))

    def test_dict_methods_keys_returns_dictionary_keys(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        keys_list = list(thisdict.keys())

        # Assert
        self.assertEqual(keys_list, ["brand", "model", "year"])

    def test_dict_methods_pop(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        removed_value = thisdict.pop("model")

        # Assert
        self.assertEqual(removed_value, "Mustang")
        self.assertEqual(thisdict, {"brand": "Ford", "year": 1964})
        self.assertNotIn("model", thisdict)

    def test_dict_methods_popitem(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        removed_item = thisdict.popitem()

        # Assert
        # popitem() removes and returns the last inserted key-value pair as a tuple
        self.assertEqual(removed_item, ("year", 1964))
        self.assertEqual(thisdict, {"brand": "Ford", "model": "Mustang"})
        self.assertNotIn("year", thisdict)

    def test_dict_methods_setdefault_existing_key(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        # Key exists — returns its current value without modifying the dictionary
        value = thisdict.setdefault("model", "BMW")

        # Assert
        self.assertEqual(value, "Mustang")
        self.assertEqual(thisdict["model"], "Mustang")

    def test_dict_methods_setdefault_non_existing_key(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        # Key does not exist — inserts it with the specified value and returns it
        value = thisdict.setdefault("color", "white")

        # Assert
        self.assertEqual(value, "white")
        self.assertIn("color", thisdict)
        self.assertEqual(thisdict["color"], "white")

    def test_dict_methods_update(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        # Updates an existing key and adds a new one
        thisdict.update({"year": 2020, "color": "red"})

        # Assert
        self.assertEqual(thisdict["year"], 2020)
        self.assertEqual(thisdict["color"], "red")
        self.assertEqual(thisdict["brand"], "Ford")
        self.assertEqual(thisdict["model"], "Mustang")

    def test_dict_methods_values_returns_all_values(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        values_list = list(thisdict.values())

        # Assert
        self.assertEqual(values_list, ["Ford", "Mustang", 1964])

    def test_dict_methods_car_exercise(self):
        # Arrange
        car = {"brand": "Ford", "model": "Mustang", "year": 2024}

        # Act - Print the value of the "model" key
        model = car["model"]

        # Assert
        self.assertEqual(model, "Mustang")

        # Act - Add a new key "color" with the value "red"
        car["color"] = "red"

        # Assert
        self.assertIn("color", car)
        self.assertEqual(car["color"], "red")

        # Act - Remove the "brand" key using pop()
        removed = car.pop("brand")

        # Assert
        self.assertEqual(removed, "Ford")
        self.assertNotIn("brand", car)
        self.assertEqual(car, {"model": "Mustang", "year": 2024, "color": "red"})


if __name__ == "__main__":
    unittest.main()
