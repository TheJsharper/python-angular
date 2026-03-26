import unittest
class ListMethodRemoveListItemsTestCase(unittest.TestCase):
    def test_remove_list_items_with_remove(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 3]

        # Act
        my_list.remove(2)

        # Assert
        self.assertEqual(my_list, expected)

    def test_remove_list_items_with_remove_non_existent_item_raises_value_error(self):
        # Arrange
        my_list = [1, 2, 3]

        # Act & Assert
        with self.assertRaises(ValueError):
            my_list.remove(4)  # ValueError: list.remove(x): x not found
    def test_remove_list_items_with_pop(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 3]

        # Act
        my_list.pop(1)

        # Assert
        self.assertEqual(my_list, expected)
    def test_remove_list_items_with_pop_non_existent_index_raises_index_error(self):
        # Arrange
        my_list = [1, 2, 3]

        # Act & Assert
        with self.assertRaises(IndexError):
            my_list.pop(3)  # IndexError: pop index out of range

    def test_remove_list_items_with_del(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 3]

        # Act
        del my_list[1]

        # Assert
        self.assertEqual(my_list, expected)
    def test_remove_list_items_with_del_non_existent_index_raises_index_error(self):
        # Arrange
        my_list = [1, 2, 3]

        # Act & Assert
        with self.assertRaises(IndexError):
            del my_list[3]  # IndexError: list assignment index out of range

    def test_remove_list_items_with_slice_assignment(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 5]

        # Act
        my_list[1:4] = []

        # Assert
        self.assertEqual(my_list, expected)

    def test_remove_list_items_with_slice_assignment_and_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 3, 5]

        # Act
        del my_list[1:4:2]
        
        self.assertEqual(my_list, expected)                             
    def test_remove_list_items_with_slice_assignment_and_negative_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        
        expected = [1, 3, 5]

        # Act
        del my_list[3:0:-2]

         # Assert
        self.assertEqual(my_list, expected)

    def test_remove_list_items_with_slice_assignment_and_negative_step_and_different_length(
        self,
    ):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 3, 5]

        # Act
        del my_list[3:0:-2]

         # Assert
        self.assertEqual(my_list, expected)    
        

if __name__ == "__main__":
    unittest.main()
