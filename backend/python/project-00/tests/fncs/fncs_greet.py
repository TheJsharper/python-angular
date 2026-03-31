import unittest


import sys
import os
from unittest import mock

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from fncs import fncs_greet


class FncsGreetTestCase(unittest.TestCase):
    @mock.patch("builtins.print")
    def test_greet_function(self, mock_print):
        # Arrange

        # Act
        fncs_greet.greet(name="Alice")

        # Assert
        mock_print.assert_called_once_with("Hello, Alice")

    @mock.patch("builtins.print")
    def test_greet_function_with_different_name(self, mock_print):
        # Arrange
        expected_name = "Bob"
        expected_print = f"Hello, {expected_name}"
        # Act
        fncs_greet.greet(name=expected_name)

        # Assert
        mock_print.assert_called_once_with(expected_print)

    def test_greet_function_with_custom_greeting(self):
        # Arrange
        name = "Charlie"
        greeting = "Hi"
        expected_print = f"{greeting}, {name}"
        with mock.patch("builtins.print") as mock_print:
            # Act
            fncs_greet.greet(name=name, greeting=greeting)

            # Assert
            mock_print.assert_called_once_with(expected_print)

    def test_greet_function_with_non_string_name(self):
        # Arrange
        non_string_name = 123

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            fncs_greet.greet(name=non_string_name)
        self.assertEqual(str(context.exception), "Name must be a string")

    def test_greet_function_with_non_string_greeting(self):
        # Arrange
        name = "Alice"
        non_string_greeting = 123

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            fncs_greet.greet(name=name, greeting=non_string_greeting)
        self.assertEqual(str(context.exception), "Greeting must be a string")


if __name__ == "__main__":
    unittest.main()
