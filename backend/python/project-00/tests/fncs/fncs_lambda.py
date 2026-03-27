import unittest


class FncsLambdaTestCase(unittest.TestCase):
    def test_fncs_lambda_with_simple_expression(self):
        # Arrange
        add = lambda x, y: x + y
        expected = 5

        # Act
        result = add(2, 3)

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_lambda_with_no_arguments(self):
        # Arrange
        greet = lambda: "Hello, World!"
        expected = "Hello, World!"

        # Act
        result = greet()

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_lambda_with_default_arguments(self):
        # Arrange
        power = lambda x, y=2: x**y
        expected_default = 9
        expected_custom = 27

        # Act
        result_default = power(3)
        result_custom = power(3, 3)

        # Assert
        self.assertEqual(result_default, expected_default)
        self.assertEqual(result_custom, expected_custom)

    def test_fncs_lambda_with_multiple_statements(self):
        # Arrange
        complex_operation = lambda x: (x * 2, x + 3)
        expected = (10, 8)

        # Act
        result = complex_operation(5)

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_lambda_with_multiplication(self):
        # Arrange
        x = lambda a, b: a * b

        # Act
        result = x(5, 6)

        # Assert
        self.assertEqual(result, 30)

    def test_fncs_lambda_closure_with_myfunc(self):
        # Arrange
        def myfunc(n):
            return lambda a: a * n

        mytripler = myfunc(3)

        # Act
        result1 = mytripler(4)
        result2 = mytripler(10)

        # Assert
        self.assertEqual(result1, 12)
        self.assertEqual(result2, 30)

    def test_fncs_lambda_closure_with_doubler_and_tripler(self):
        # Arrange
        def myfunc(n):
            return lambda a: a * n

        mydoubler = myfunc(2)
        mytripler = myfunc(3)

        # Act
        double_result = mydoubler(5)
        triple_result = mytripler(5)

        # Assert
        self.assertEqual(double_result, 10)
        self.assertEqual(triple_result, 15)

    def test_fncs_lambda_with_map(self):
        # Arrange
        numbers = [1, 2, 3, 4]

        # Act
        squared = list(map(lambda x: x * x, numbers))

        # Assert
        self.assertEqual(squared, [1, 4, 9, 16])

    def test_fncs_lambda_with_filter(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5, 6]

        # Act
        evens = list(filter(lambda x: x % 2 == 0, numbers))

        # Assert
        self.assertEqual(evens, [2, 4, 6])

    def test_fncs_lambda_with_sorted(self):
        # Arrange
        words = ["banana", "kiwi", "apple", "fig"]

        # Act
        sorted_by_length = sorted(words, key=lambda x: len(x))

        # Assert
        self.assertEqual(sorted_by_length, ["fig", "kiwi", "apple", "banana"])

    def test_fncs_lambda_filter_odd_numbers(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        # Act
        odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

        # Assert
        self.assertEqual(odd_numbers, [1, 3, 5, 7])

    def test_fncs_lambda_sorted_students_by_age(self):
        # Arrange
        students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]

        # Act
        sorted_students = sorted(students, key=lambda x: x[1])

        # Assert
        self.assertEqual(sorted_students, [("Tobias", 22), ("Emil", 25), ("Linus", 28)])

    def test_fncs_lambda_sorted_words_by_length(self):
        # Arrange
        words = ["apple", "pie", "banana", "cherry"]

        # Act
        sorted_words = sorted(words, key=lambda x: len(x))

        # Assert
        self.assertEqual(sorted_words, ["pie", "apple", "banana", "cherry"])


if __name__ == "__main__":
    unittest.main()
