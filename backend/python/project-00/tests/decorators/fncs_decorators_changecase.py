import unittest
import unittest.mock as mock
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from decorators.fncs_decoratos_changecase import (
    changeToTitleCase,
    changeToUpperCase,
    changeToLowerCase,
    changeToArgumnentCase,
    combineTwoStrings,
    combinteNStrings,
    multiply,
    sum,
    multiply,
    divide,
)


class FncsDecoratorsChangecaseTestCase(unittest.TestCase):
    def test_changecase(self):
        # Arrange
        input_str = "hello world"
        expected_output_upper = "HELLO WORLD"

        # Act
        @changeToUpperCase
        def myFunc():
            return input_str

        # Assert
        self.assertEqual(myFunc(), expected_output_upper)

    def test_changecase_lower(self):
        # Arrange
        input_str = "HELLO WORLD"
        expected_output_lower = "hello world"

        # Act
        @changeToLowerCase
        def myFunc():
            return input_str

        # Assert
        self.assertEqual(myFunc(), expected_output_lower)

    def test_changecase_title(self):
        # Arrange
        input_str = "hello world"
        expected_output_title = "Hello World"

        # Act
        @changeToTitleCase
        def myFunc():
            return input_str

        # Assert
        self.assertEqual(myFunc(), expected_output_title)

    def test_changecase_argument(self):
        # Arrange
        input_str = "hello world"
        expected_output_upper = "HELLO WORLD"
        expected_output_lower = "hello world"
        expected_output_title = "Hello World"

        # Act
        @changeToArgumnentCase("upper")
        def myFuncUpper(s):
            return s

        @changeToArgumnentCase("lower")
        def myFuncLower(s):
            return s

        @changeToArgumnentCase("title")
        def myFuncTitle(s):
            return s

        # Assert
        self.assertEqual(myFuncUpper(input_str), expected_output_upper)
        self.assertEqual(myFuncLower(input_str), expected_output_lower)
        self.assertEqual(myFuncTitle(input_str), expected_output_title)

    def test_changecase_argument_invalid(self):
        # Arrange
        input_str = "hello world"

        # Act
        @changeToArgumnentCase("invalid")
        def myFuncInvalid(s):
            return s

        # Assert
        with self.assertRaises(ValueError) as context:
            myFuncInvalid(input_str)

        self.assertEqual(
            str(context.exception),
            "Invalid case argument. Use 'upper', 'lower', or 'title'.",
        )

    def test_combineTwoStrings(self):
        # Arrange
        str1 = "Hello"
        str2 = "World"
        expected_output = "Hello World"

        # Act
        @combineTwoStrings
        def myFunc(s1, s2):
            return f"{s1} {s2}"

        # Assert
        self.assertEqual(myFunc(str1, str2), expected_output)

    def test_combineNStrings(self):
        # Arrange
        strings = ["Hello", "World", "from", "Python"]
        expected_output = "Hello World from Python"

        # Act
        @combinteNStrings
        def myFunc(*args):
            return " ".join(args)

        # Assert
        self.assertEqual(myFunc(*strings), expected_output)

    def test_sum(self):
        # Arrange
        a = 5
        b = 3
        expected_result = 8

        # Act
        @sum
        def add(x, y):
            return x + y

        # Assert
        self.assertEqual(add(a, b), expected_result)

    def test_multiply(self):
        # Arrange
        a = 5
        b = 3
        expected_result = 15

        # Act
        @multiply
        def mul(x, y):
            return x * y

        # Assert
        self.assertEqual(mul(a, b), expected_result)

    def test_divide(self):
        # Arrange
        a = 10
        b = 2
        expected_result = 5

        # Act
        @divide
        def div(x, y):
            return x / y

        # Assert
        self.assertEqual(div(a, b), expected_result)

    def test_divide_by_zero(self):
        # Arrange
        a = 10
        b = 0

        # Act
        @divide
        def div(x, y):
            return x / y

        # Assert
        with self.assertRaises(ValueError) as context:
            div(a, b)

        self.assertEqual(str(context.exception), "Cannot divide by zero.")


if __name__ == "__main__":
    unittest.main()
