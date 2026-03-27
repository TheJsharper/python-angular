import unittest
class DictsRemoveTestCase(unittest.TestCase):
    def test_dict_remove_with_del(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30, "country": "USA"}
        expected = {"name": "Alice", "age": 30}

        # Act
        del my_dict["country"]

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_remove_with_pop(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30, "country": "USA"}
        expected = {"name": "Alice", "age": 30}

        # Act
        removed_value = my_dict.pop("country")

        # Assert
        self.assertEqual(removed_value, "USA")
        self.assertEqual(my_dict, expected)

    def test_dict_remove_non_existent_key_with_del_raises_key_error(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act & Assert
        with self.assertRaises(KeyError):
            del my_dict["non_existent_key"]

    def test_dict_remove_non_existent_key_with_pop_raises_key_error(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act & Assert
        with self.assertRaises(KeyError):
            my_dict.pop("non_existent_key")

    def test_dict_remove_with_popitem(self):
        # Arrange
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
        }
        expected = {"brand": "Ford", "model": "Mustang"}

        # Act
        removed_item = thisdict.popitem()

        # Assert
        self.assertEqual(removed_item, ("year", 1964))
        self.assertEqual(thisdict, expected)

    def test_dict_delete_entire_dictionary_with_del(self):
        # Arrange
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
        }

        # Act
        del thisdict

        # Assert
        with self.assertRaises(UnboundLocalError):
            _ = thisdict

    def test_dict_clear_empties_dictionary(self):
        # Arrange
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
        }

        # Act
        thisdict.clear()

        # Assert
        self.assertEqual(thisdict, {})
        self.assertEqual(len(thisdict), 0)

    def test_dict_popitem_on_empty_dictionary_raises_key_error(self):
        # Arrange
        thisdict = {}

        # Act & Assert
        with self.assertRaises(KeyError):
            thisdict.popitem()

    def test_dict_pop_after_clear_raises_key_error(self):
        # Arrange
        thisdict = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964,
        }

        # Act
        thisdict.clear()

        # Assert
        with self.assertRaises(KeyError):
            thisdict.pop("year")


if __name__ == "__main__":
    unittest.main()