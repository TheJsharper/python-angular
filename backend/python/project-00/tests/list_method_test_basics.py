import unittest


class TestListMethods(unittest.TestCase):
    def test_append(self):
        # Arrange
        my_list = []
        # Act
        my_list.append(1)
        # Assert
        self.assertEqual(my_list, [1])

    def test_clear(self):
        # Arrange
        my_list = [1, 2, 3]
        # Act
        my_list.clear()
        # Assert
        self.assertEqual(my_list, [])

    def test_copy(self):
        # Arrange
        my_list = [1, 2, 3]
        # Act
        copied_list = my_list.copy()
        # Assert
        self.assertEqual(copied_list, my_list)

    def test_count(self):
        # Arrange
        my_list = [1, 2, 2, 3]
        # Act
        count = my_list.count(2)
        # Assert
        self.assertEqual(count, 2)

    def test_extend(self):
        # Arrange
        my_list = [1, 2]
        # Act
        my_list.extend([3, 4])
        # Assert
        self.assertEqual(my_list, [1, 2, 3, 4])

    def test_index(self):
        # Arrange
        my_list = [1, 2, 3]
        # Act
        index = my_list.index(2)
        # Assert
        self.assertEqual(index, 1)

    def test_insert(self):
        # Arrange
        my_list = [1, 3]
        # Act
        my_list.insert(1, 2)
        # Assert
        self.assertEqual(my_list, [1, 2, 3])

    def test_pop(self):
        # Arrange
        my_list = [1, 2, 3]
        # Act
        popped_element = my_list.pop()
        # Assert
        self.assertEqual(popped_element, 3)
        self.assertEqual(my_list, [1, 2])

    def test_remove(self):
        # Arrange
        my_list = [1, 2, 3]
        # Act
        my_list.remove(2)
        # Assert
        self.assertEqual(my_list, [1, 3])

    def test_reverse(self):
        # Arrange
        my_list = [1, 2, 3]
        # Act
        my_list.reverse()
        # Assert
        self.assertEqual(my_list, [3, 2, 1])

    def test_sort(self):
        # Arrange
        my_list = [3, 1, 2]
        # Act
        my_list.sort()
        # Assert
        self.assertEqual(my_list, [1, 2, 3])

    def test_len(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = 3

        # Act
        result = len(my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_check_duplicate(self):
        # Arrange
        my_list = [1, 2, 2, 3]
        expected = True

        # Act
        has_duplicates = len(my_list) != len(set(my_list))

        # Assert
        self.assertEqual(has_duplicates, expected)

    def test_data_type(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = list

        # Act
        result = type(my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_check_constructor(self):
        # Arrange
        my_list = list()
        expected = []

        # Act
        result = my_list

        # Assert
        self.assertEqual(result, expected)

    def test_check_index_out_of_range(self):
        # Arrange
        my_list = [1, 2, 3]

        # Act & Assert
        with self.assertRaises(IndexError):
            _ = my_list[5]

    def test_check_remove_nonexistent_element(self):
        # Arrange
        my_list = [1, 2, 3]

        # Act & Assert
        with self.assertRaises(ValueError):
            my_list.remove(4)

    def test_check_negative_index(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = 3

        # Act
        result = my_list[-1]

        # Assert
        self.assertEqual(result, expected)

    def test_access_slice(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [2, 3]

        # Act
        result = my_list[1:3]

        # Assert
        self.assertEqual(result, expected)

    def test_access_to_index(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [2, 3, 4, 5]

        # Act
        result = my_list[1:]

        # Assert
        self.assertEqual(result, expected)

    def test_access_to_index_with_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [1, 3, 5]

        # Act
        result = my_list[::2]

        # Assert
        self.assertEqual(result, expected)

    def test_access_from_index_to_index_with_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [2, 4]

        # Act
        result = my_list[1:5:2]

        # Assert
        self.assertEqual(result, expected)

    def test_access_with_negative_step(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]

        # Act
        result = my_list[::-1]

        # Assert
        self.assertEqual(result, expected)

    def test_access_with_negative_step_from_index_to_index(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [4, 3]

        # Act
        result = my_list[3:0:-1]

        # Assert
        self.assertEqual(result, expected)

    def test_access_from_index_2_to_end(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [3, 4, 5]

        # Act
        result = my_list[2:]

        # Assert
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
