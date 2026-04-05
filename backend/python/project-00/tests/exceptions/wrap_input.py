import unittest

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "../src"))
)


from unittest.mock import patch

from exceptions.wrap_input import WrapInput


class WrapInputTestCase(unittest.TestCase):
    def test_wrap_input(self):
        with patch("builtins.input", return_value="test"):
            wrap_input = WrapInput(input)
            result = wrap_input("Enter something: ")
            self.assertEqual(result, "test")

    def test_wrap_input_exception(self):
        with patch("builtins.input", side_effect=Exception("Input error")):
            wrap_input = WrapInput(input)
            with self.assertRaises(ValueError) as context:
                wrap_input("Enter something: ")
            self.assertIn(
                "An error occurred while getting input: Input error",
                str(context.exception),
            )

    def test_wrap_input_no_exception(self):
        with patch("builtins.input", return_value="test"):
            wrap_input = WrapInput(input)
            try:
                result = wrap_input("Enter something: ")
                self.assertEqual(result, "test")
            except ValueError:
                self.fail("WrapInput raised ValueError unexpectedly!")

    def test_wrap_input_different_exception(self):
        with patch("builtins.input", side_effect=KeyError("Key error")):
            wrap_input = WrapInput(input)
            with self.assertRaises(ValueError) as context:
                wrap_input("Enter something: ")
            self.assertIn(
                "An error occurred while getting input: Key error",
                str(context.exception),
            )

    def test_wrap_input_key_error_with_args(self):
        with patch("builtins.input", side_effect=KeyError("Key error", "extra info")):
            wrap_input = WrapInput(input)
            with self.assertRaises(ValueError) as context:
                wrap_input("Enter something: ")
            self.assertIn(
                "An error occurred while getting input: Key error",
                str(context.exception),
            )

    def test_wrap_input_key_error_without_args(self):
        with patch("builtins.input", side_effect=KeyError()):
            wrap_input = WrapInput(input)
            with self.assertRaises(ValueError) as context:
                wrap_input("Enter something: ")
            self.assertIn(
                "An error occurred while getting input: ",
                str(context.exception),
            )

    def test_wrap_input_key_error_with_non_string_arg(self):
        with patch("builtins.input", side_effect=KeyError(123)):
            wrap_input = WrapInput(input)
            with self.assertRaises(ValueError) as context:
                wrap_input("Enter something: ")
            self.assertIn(
                "An error occurred while getting input: 123",
                str(context.exception),
            )

    def test_wrap_input_key_error_with_non_string_arg_and_no_args(self):
        with patch("builtins.input", side_effect=KeyError()):
            wrap_input = WrapInput(input)
            with self.assertRaises(ValueError) as context:
                wrap_input("Enter something: ")
            self.assertIn(
                "An error occurred while getting input: ",
                str(context.exception),
            )

    def test_wrap_input_key_error_with_non_string_arg_and_args(self):
        with patch("builtins.input", side_effect=KeyError(123, "extra info")):
            wrap_input = WrapInput(input)
            with self.assertRaises(ValueError) as context:
                wrap_input("Enter something: ")
            self.assertIn(
                "An error occurred while getting input: 123",
                str(context.exception),
            )

    def test_wrap_input_correctly_calls_input(self):
        with patch("builtins.input", return_value="test") as mock_input:
            wrap_input = WrapInput(input)
            result = wrap_input("Enter something: ")
            mock_input.assert_called_once_with("Enter something: ")
            self.assertEqual(result, "test")

    def test_wrap_input_with_different_prompt(self):
        with patch("builtins.input", return_value="test") as mock_input:
            wrap_input = WrapInput(input)
            result = wrap_input("Please enter something: ")
            mock_input.assert_called_once_with("Please enter something: ")
            self.assertEqual(result, "test")

    def test_wrap_input_with_empty_prompt(self):
        with patch("builtins.input", return_value="test") as mock_input:
            wrap_input = WrapInput(input)
            result = wrap_input("")
            mock_input.assert_called_once_with("")
            self.assertEqual(result, "test")

    def test_wrap_add_two_floats(self):
        with patch("builtins.input", return_value="3.14") as mock_input:
            wrap_input = WrapInput(input)
            result = wrap_input("Enter a float: ")
            mock_input.assert_called_once_with("Enter a float: ")
            self.assertEqual(result, "3.14")

    def test_wrap_add_two_integers(self):
        with patch("builtins.input", return_value="42") as mock_input:
            wrap_input = WrapInput(input)
            result = wrap_input("Enter an integer: ")
            mock_input.assert_called_once_with("Enter an integer: ")
            self.assertEqual(result, "42")

    def test_wrap_input_add_two_from_input(self):
        with patch("builtins.input", side_effect=["3.14", "2.71"]) as mock_input:
            wrap_input = WrapInput(input)
            result1 = wrap_input("Enter first float: ")
            result2 = wrap_input("Enter second float: ")
            mock_input.assert_has_calls(
                [
                    unittest.mock.call("Enter first float: "),
                    unittest.mock.call("Enter second float: "),
                ]
            )
            self.assertEqual(result1, "3.14")
            self.assertEqual(result2, "2.71")


if __name__ == "__main__":
    unittest.main()
