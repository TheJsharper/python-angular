import unittest
from unittest import mock


class FncsRecursionTestCase(unittest.TestCase):
    def test_fncs_recursion_with_factorial(self):
        # Arrange
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        expected = 120

        # Act
        result = factorial(5)

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_recursion_with_fibonacci(self):
        # Arrange
        def fibonacci(n):
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        expected = 8

        # Act
        result = fibonacci(6)

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_recursion_with_countdown(self):
        # Arrange
        def countdown(n):
            if n <= 0:
                print("Done!")
            else:
                print(n)
                countdown(n - 1)

        # Act & Assert
        with mock.patch("builtins.print") as mock_print:
            countdown(3)

            expected_calls = [
                mock.call(3),
                mock.call(2),
                mock.call(1),
                mock.call("Done!"),
            ]
            mock_print.assert_has_calls(expected_calls)
            self.assertEqual(mock_print.call_count, 4)

    def test_fncs_recursion_with_sum_list(self):
        # Arrange
        def sum_list(numbers):
            if len(numbers) == 0:
                return 0
            else:
                return numbers[0] + sum_list(numbers[1:])

        my_list = [1, 2, 3, 4, 5]

        # Act
        result = sum_list(my_list)

        # Assert
        self.assertEqual(result, 15)
        self.assertEqual(sum_list([]), 0)

    def test_fncs_recursion_with_find_max(self):
        # Arrange
        def find_max(numbers):
            if len(numbers) == 1:
                return numbers[0]
            else:
                max_of_rest = find_max(numbers[1:])
                return numbers[0] if numbers[0] > max_of_rest else max_of_rest

        my_list = [3, 7, 2, 9, 1]

        # Act
        result = find_max(my_list)

        # Assert
        self.assertEqual(result, 9)
        self.assertEqual(find_max([5]), 5)


if __name__ == "__main__":
    unittest.main()
