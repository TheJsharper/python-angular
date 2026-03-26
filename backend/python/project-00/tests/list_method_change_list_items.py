import unittest


class TestChangeListItems(unittest.TestCase):
    def test_change_list_items(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 20, 3]

        # Act
        my_list[1] = 20

        # Assert
        self.assertEqual(my_list, expected)

    def test_change_list_items_with_slice(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 20, 30, 40, 5]

        # Act
        my_list[1:4] = [20, 30, 40]

        # Assert
        self.assertEqual(my_list, expected)

    def test_change_list_items_with_slice_and_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 20, 3, 40, 5]

        # Act
        my_list[1:4:2] = [20, 40]

        # Assert
        self.assertEqual(my_list, expected)

    def test_change_list_items_with_slice_and_negative_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 20, 3, 40, 5]

        # Act
        my_list[3:0:-2] = [40, 20]

        # Assert
        self.assertEqual(my_list, expected)

    def test_change_list_items_with_slice_and_negative_step_and_different_length(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 20, 3, 40, 5]

        # Act
        my_list[3:0:-2] = [40, 20]

        # Assert
        self.assertEqual(my_list, expected)

    def test_change_list_items_with_slice_and_negative_step_and_different_length_2(
        self,
    ):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 20, 3, 40, 5]

        # Act
        my_list[3:0:-2] = [40, 20]

        # Assert
        self.assertEqual(my_list, expected)

    def test_change_list_items_by_index_and_slice(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 20, 30, 40, 5]

        # Act
        my_list[1] = 20

        my_list[2:4] = [30, 40]

        # Assert
        self.assertEqual(my_list, expected)

    def test_change_list_items_by_index_and_slice_and_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 20, 30, 40, 5]

        # Act
        my_list[1] = 20

        my_list[2:4:1] = [30, 40]

        # Assert
        self.assertEqual(my_list, expected)
        
    def test_change_list_items_insert_method(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 20, 2, 3]

        # Act
        my_list.insert(1, 20)

        # Assert
        self.assertEqual(my_list, expected)    


if __name__ == "__main__":
    unittest.main()
