import unittest


class DictsLoopTestCase(unittest.TestCase):
    def test_dict_loop_with_for_loop(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30, "country": "USA"}
        expected_items = [("name", "Alice"), ("age", 30), ("country", "USA")]

        # Act
        items = []
        for key, value in my_dict.items():
            items.append((key, value))

        # Assert
        self.assertEqual(items, expected_items)

    def test_dict_loop_print_values_one_by_one(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
        expected_values = ["Ford", "Mustang", 1964]

        # Act
        values = []
        for key in thisdict:
            values.append(thisdict[key])

        # Assert
        self.assertEqual(values, expected_values)

    def test_dict_loop_with_values_method(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
        expected_values = ["Ford", "Mustang", 1964]

        # Act
        values = []
        for value in thisdict.values():
            values.append(value)

        # Assert
        self.assertEqual(values, expected_values)

    def test_dict_loop_with_keys_method(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
        expected_keys = ["brand", "model", "year"]

        # Act
        keys = []
        for key in thisdict.keys():
            keys.append(key)

        # Assert
        self.assertEqual(keys, expected_keys)

    def test_dict_loop_with_items_method(self):
        # Arrange
        thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
        expected_items = [("brand", "Ford"), ("model", "Mustang"), ("year", 1964)]

        # Act
        items = []
        for key, value in thisdict.items():
            items.append((key, value))

        # Assert
        self.assertEqual(items, expected_items)

    def test_dict_loop_with_list_comprehension(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30, "country": "USA"}
        expected_keys = ["name", "age", "country"]

        # Act
        keys = [key for key in my_dict]

        # Assert
        self.assertEqual(keys, expected_keys)

        values = [value for value in my_dict.values()]

        expected_values = ["Alice", 30, "USA"]

        self.assertEqual(values, expected_values)

        items = [(key, value) for key, value in my_dict.items()]
        expected_items = [("name", "Alice"), ("age", 30), ("country", "USA")]

        self.assertEqual(items, expected_items)


if __name__ == "__main__":
    unittest.main()
