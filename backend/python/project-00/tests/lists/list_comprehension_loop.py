import unittest


class ListComprehensionLoopTestCase(unittest.TestCase):
    def test_list_comprehension_loop(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [2, 3, 4]

        # Act
        result = [x + 1 for x in my_list]

        # Assert
        self.assertEqual(result, expected)

    def test_list_comprehension_loop_with_condition(self):
        # Arrange
        my_list = [1, 2, 3, 4, 5]
        expected = [3, 5]

        # Act
        result = [x + 1 for x in my_list if x % 2 == 0]

        # Assert
        self.assertEqual(result, expected)

    def test_list_comprehension_loop_with_nested_loops(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [2, 3, 3, 4, 4, 5]

        # Act
        result = [x + y for x in my_list for y in range(1, 3)]

        # Assert
        self.assertEqual(result, expected)

    def test_list_comprehension_loop_with_nested_loops_and_condition(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [3, 4]

        # Act
        result = [x + y for x in my_list for y in range(1, 3) if x % 2 == 0]

        # Assert
        self.assertEqual(result, expected)

    def test_list_comprehension_loop_with_nested_loops_and_condition_and_different_length(
        self,
    ):
        # Arrange
        my_list = [1, 2, 3]
        expected = [3, 4]

        # Act
        result = [x + y for x in my_list for y in range(1, 3) if x % 2 == 0]

        # Assert
        self.assertEqual(result, expected)

    def test_list_comprehension_loop_with_range_and_condition(self):
        # Arrange
        expected = [0, 1, 2, 3, 4]

        # Act
        newlist = [x for x in range(10) if x < 5]

        # Assert
        self.assertEqual(newlist, expected)

    def test_list_comprehension_loop_with_range(self):
        # Arrange
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Act
        newlist = [x for x in range(10)]

        # Assert
        self.assertEqual(newlist, expected)

    def test_list_comprehension_loop_with_inline_condition(self):
        # Arrange
        fruits = ["apple", "banana", "cherry"]
        expected = ["apple", "orange", "cherry"]

        # Act
        newlist = [x if x != "banana" else "orange" for x in fruits]

        # Assert
        self.assertEqual(newlist, expected)


if __name__ == "__main__":
    unittest.main()
