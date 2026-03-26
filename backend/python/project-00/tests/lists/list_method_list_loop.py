
import unittest



class ListMethodListLoopTestCase(unittest.TestCase):
    def test_list_loop_with_for_loop(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3]

        # Act
        result = []
        for item in my_list:
            result.append(item)

        # Assert
        self.assertEqual(result, expected)

    def test_list_loop_with_while_loop(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3]

        # Act
        result = []
        i = 0
        while i < len(my_list):
            result.append(my_list[i])
            i += 1

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_list_comprehension(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3]

        # Act
        result = [item for item in my_list]

        # Assert
        self.assertEqual(result, expected)

    def test_list_loop_with_enumerate(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [(0, 1), (1, 2), (2, 3)]

        # Act
        result = []
        for index, item in enumerate(my_list):
            result.append((index, item))

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_zip(self):
        # Arrange
        my_list1 = [1, 2, 3]
        my_list2 = ['a', 'b', 'c']
        expected = [(1, 'a'), (2, 'b'), (3, 'c')]

        # Act
        result = []
        for item1, item2 in zip(my_list1, my_list2):
            result.append((item1, item2))

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_enumerate_and_zip(self):
        # Arrange
        my_list1 = [1, 2, 3]
        my_list2 = ['a', 'b', 'c']
        expected = [(0, 1, 'a'), (1, 2, 'b'), (2, 3, 'c')]

        # Act
        result = []
        for index, (item1, item2) in enumerate(zip(my_list1, my_list2)):
            result.append((index, item1, item2))

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_list_comprehension_and_enumerate(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [(0, 1), (1, 2), (2, 3)]

        # Act
        result = [(index, item) for index, item in enumerate(my_list)]

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_list_comprehension_and_zip(self):
        # Arrange
        my_list1 = [1, 2, 3]
        my_list2 = ['a', 'b', 'c']
        expected = [(1, 'a'), (2, 'b'), (3, 'c')]

        # Act
        result = [(item1, item2) for item1, item2 in zip(my_list1, my_list2)]

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_list_comprehension_and_enumerate_and_zip(self):
        # Arrange
        my_list1 = [1, 2, 3]
        my_list2 = ['a', 'b', 'c']
        expected = [(0, 1, 'a'), (1, 2, 'b'), (2, 3, 'c')]

        # Act
        result = [(index, item1, item2) for index, (item1, item2) in enumerate(zip(my_list1, my_list2))]

        # Assert
        self.assertEqual(result, expected)

    def test_list_loop_with_list_comprehension_and_enumerate_and_zip_and_filter(self):
        # Arrange
        my_list1 = [1, 2, 3]
        my_list2 = ['a', 'b', 'c']
        expected = [(0, 1, 'a'), (1, 2, 'b')]

        # Act
        result = [(index, item1, item2) for index, (item1, item2) in enumerate(zip(my_list1, my_list2)) if item1 < 3]

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_list_comprehension_and_enumerate_and_zip_and_filter_and_map(self):
        # Arrange
        my_list1 = [1, 2, 3]
        my_list2 = ['a', 'b', 'c']
        expected = [(0, 2, 'a'), (1, 4, 'b')]

        # Act
        result = [(index, item1 * 2, item2) for index, (item1, item2) in enumerate(zip(my_list1, my_list2)) if item1 < 3]

        # Assert
        self.assertEqual(result, expected)
    def test_list_loop_with_for_range(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3]

        # Act
        result = []
        for i in range(len(my_list)):
            result.append(my_list[i])

        # Assert
        self.assertEqual(result, expected)


        
if __name__ == "__main__":
    unittest.main()
