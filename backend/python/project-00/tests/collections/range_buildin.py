import unittest


class RangeArraysIteratorsTestCase(unittest.TestCase):
    def test_range_with_start_and_stop(self):
        # Arrange
        expected = [1, 2, 3, 4]

        # Act
        result = list(range(1, 5))

        # Assert
        self.assertEqual(result, expected)

    def test_range_with_start_stop_and_step(self):
        # Arrange
        expected = [0, 2, 4]

        # Act
        result = list(range(0, 6, 2))

        # Assert
        self.assertEqual(result, expected)

    def test_range_with_negative_step(self):
        # Arrange
        expected = [5, 4, 3]

        # Act
        result = list(range(5, 2, -1))

        # Assert
        self.assertEqual(result, expected)

    def test_range_with_only_stop(self):
        # Arrange
        expected = [0, 1, 2]

        # Act
        result = list(range(3))

        # Assert
        self.assertEqual(result, expected)

    def test_range_with_large_step(self):
        # Arrange
        expected = [0, 5]

        # Act
        result = list(range(0, 10, 5))

        # Assert
        self.assertEqual(result, expected)

    def test_range_start_stop_step_example(self):
        # Arrange
        start, stop, step = 2, 12, 3
        expected = [2, 5, 8, 11]

        # Act
        result = list(range(start, stop, step))

        # Assert
        self.assertEqual(result, expected)

    def test_range_create_from_zero_to_nine(self):
        # Arrange
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # Act
        x = range(10)
        result = list(x)

        # Assert
        self.assertEqual(result, expected)

    def test_range_examples_from_print_list_calls(self):
        # Act
        result1 = list(range(5))
        result2 = list(range(1, 6))
        result3 = list(range(5, 20, 3))

        # Assert
        self.assertEqual(result1, [0, 1, 2, 3, 4])
        self.assertEqual(result2, [1, 2, 3, 4, 5])
        self.assertEqual(result3, [5, 8, 11, 14, 17])

    def test_range_membership_with_step(self):
        # Arrange
        r = range(0, 10, 2)

        # Act
        has_six = 6 in r
        has_seven = 7 in r

        # Assert
        self.assertTrue(has_six)
        self.assertFalse(has_seven)

    def test_range_length_with_step(self):
        # Arrange
        r = range(0, 10, 2)

        # Act
        result = len(r)

        # Assert
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
