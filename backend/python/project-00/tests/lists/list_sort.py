import unittest


class list_sort(unittest.TestCase):
    def test_list_sort_with_mixed_types_raises_type_error(self):
        # Arrange
        my_list = [3, "1", 2]

        # Act & Assert
        with self.assertRaises(TypeError):
            my_list.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

    def test_list_sort_with_mixed_types_and_key_raises_type_error(self):
        # Arrange
        my_list = [3, "1", 2]

        # Act & Assert
        with self.assertRaises(TypeError):
            my_list.sort(
                key=lambda x: x + 1
            )  # TypeError: can only concatenate str (not "int") to str

    def test_list_sort_with_mixed_types_and_key_and_reverse_raises_type_error(self):
        # Arrange
        my_list = [3, "1", 2]

        # Act & Assert
        with self.assertRaises(TypeError):
            my_list.sort(
                key=lambda x: x + 1, reverse=True
            )  # TypeError: can only concatenate str (not "int") to str

    def test_list_sort_with_mixed_types_and_key_and_reverse_and_different_length_raises_type_error(
        self,
    ):
        # Arrange
        my_list = [3, "1", 2]

        # Act & Assert
        with self.assertRaises(TypeError):
            my_list.sort(
                key=lambda x: x + 1, reverse=True
            )  # TypeError: can only concatenate str (not "int") to str

    def test_list_sort_with_mixed_types_and_key_and_reverse_and_different_length_2_raises_type_error(
        self,
    ):
        # Arrange
        my_list = [3, "1", 2]

        # Act & Assert
        with self.assertRaises(TypeError):
            my_list.sort(
                key=lambda x: x + 1, reverse=True
            )  # TypeError: can only concatenate str (not "int") to str 

    def test_list_sort_strings(self):
        # Arrange
        thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
        expected = ["banana", "kiwi", "mango", "orange", "pineapple"]

        # Act
        thislist.sort()

        # Assert
        self.assertEqual(thislist, expected)

    def test_list_sort_numbers(self):
        # Arrange
        thislist = [100, 50, 65, 82, 23]
        expected = [23, 50, 65, 82, 100]

        # Act
        thislist.sort()

        # Assert
        self.assertEqual(thislist, expected)

    def test_list_sort_strings_descending(self):
        # Arrange
        thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
        expected = ["pineapple", "orange", "mango", "kiwi", "banana"]

        # Act
        thislist.sort(reverse=True)

        # Assert
        self.assertEqual(thislist, expected)

    def test_list_sort_numbers_descending(self):
        # Arrange
        thislist = [100, 50, 65, 82, 23]
        expected = [100, 82, 65, 50, 23]

        # Act
        thislist.sort(reverse=True)

        # Assert
        self.assertEqual(thislist, expected)


if __name__ == "__main__":
    unittest.main()
