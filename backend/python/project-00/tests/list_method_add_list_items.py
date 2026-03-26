import unittest


class TestAddListItems(unittest.TestCase):
    def test_add_list_items(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3, 4]

        # Act
        my_list.append(4)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_extend(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3, 4, 5]

        # Act
        my_list.extend([4, 5])

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert(self):
        # Arrange
        my_list = [1, 3]
        expected = [1, 2, 3]

        # Act
        my_list.insert(1, 2)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_at_end(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3, 4]

        # Act
        my_list.insert(len(my_list), 4)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_at_start(self):
        # Arrange
        my_list = [2, 3]
        expected = [1, 2, 3]

        # Act
        my_list.insert(0, 1)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_at_middle(self):
        # Arrange
        my_list = [1, 3]
        expected = [1, 2, 3]

        # Act
        my_list.insert(1, 2)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_and_shift(self):
        # Arrange
        my_list = [1, 2, 4]
        expected = [1, 2, 3, 4]

        # Act
        my_list.insert(2, 3)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_and_shift_and_different_length(self):
        # Arrange
        my_list = [1, 2, 4]
        expected = [1, 2, 3, 4]

        # Act
        my_list.insert(2, 3)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_and_shift_and_different_length_2(self):
        # Arrange
        my_list = [1, 2, 4]
        expected = [1, 2, 3, 4]

        # Act
        my_list.insert(2, 3)

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_error(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3, "4"]

        # Act
        my_list.append("4")  # no TypeError: lists accept mixed types

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_extend_error_using_type_list(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3, "4"]

        # Act
        my_list.extend(["4"])  # no TypeError: lists accept mixed types

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_error(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, "4", 2, 3]

        # Act
        my_list.insert(1, "4")  # no TypeError: lists accept mixed types

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_insert_and_shift_error(self):
        # Arrange
        my_list: list[int] = [1, 2, 4]
        expected = [1, 2, "3", 4]

        # Act
        my_list.insert(2, "3")  # no TypeError: lists accept mixed types

        # Assert
        self.assertEqual(my_list, expected)

    def test_add_list_items_with_type_as_index_raises_type_error(self):
        # Arrange
        my_list = [1, 2, 4]

        # Act & Assert
        with self.assertRaises(TypeError):
            my_list[int] = [1, 2, 4]  # TypeError: list indices must be integers or slices, not type

    def test_add_list_items_with_extend_non_iterable_raises_type_error(self):
        # Arrange
        my_list: list[int] = [1, 2, 3]

        # Act & Assert
        with self.assertRaises(TypeError):
            my_list.extend(2)  # TypeError: 'int' object is not iterable


if __name__ == "__main__":
    unittest.main()
