import unittest


class UpdateTuplesTestCase(unittest.TestCase):
    def test_update_tuple_items(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected = (1, 2, 3)  # tuple is unchanged after TypeError

        # Act
        with self.assertRaises(TypeError):
            my_tuple[1] = (
                20  # TypeError: 'tuple' object does not support item assignment
            )

        # Assert
        self.assertEqual(my_tuple, expected)

    def test_update_tuple_items_with_slice(self):
        # Arrange
        my_tuple = (1, 2, 3, 4, 5)
        expected = (1, 2, 3, 4, 5)  # tuple is unchanged after TypeError

        # Act
        with self.assertRaises(TypeError):
            my_tuple[1:4] = (
                20,
                30,
                40,
            )  # TypeError: 'tuple' object does not support item assignment

        # Assert
        self.assertEqual(my_tuple, expected)

    def test_update_tuple_via_list_conversion(self):
        # Arrange
        x = ("apple", "banana", "cherry")
        expected = ("apple", "kiwi", "cherry")

        # Act
        y = list(x)
        y[1] = "kiwi"
        x = tuple(y)

        # Assert
        self.assertEqual(x, expected)

    def test_append_to_tuple_via_list_conversion(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")
        expected = ("apple", "banana", "cherry", "orange")

        # Act
        y = list(thistuple)
        y.append("orange")
        thistuple = tuple(y)

        # Assert
        self.assertEqual(thistuple, expected)


    def test_append_to_tuple_via_concatenation(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")
        y = ("orange",)
        expected = ("apple", "banana", "cherry", "orange")

        # Act
        thistuple += y

        # Assert
        self.assertEqual(thistuple, expected)

    def test_remove_from_tuple_via_list_conversion(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")
        expected = ("banana", "cherry")

        # Act
        y = list(thistuple)
        y.remove("apple")
        thistuple = tuple(y)

        # Assert
        self.assertEqual(thistuple, expected)

    def test_delete_tuple_raises_name_error(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")

        # Act
        del thistuple

        # Assert
        with self.assertRaises(NameError):
            _ = thistuple  # NameError: name 'thistuple' is not defined


if __name__ == "__main__":
    unittest.main()
