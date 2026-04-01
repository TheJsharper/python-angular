import unittest
import unittest.mock as mock
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from fncs import fncs_args_kwargs_big_function


class FncsArgsKwargsBigFunction(unittest.TestCase):

    @mock.patch("builtins.print")
    def test_big_function_no_arguments(self, mock_print):

        fncs_args_kwargs_big_function.bigFunction()

        mock_print.assert_called_once_with("No arguments provided.")

    @mock.patch("builtins.print")
    def test_big_function_too_many_positional_arguments(self, mock_print):

        fncs_args_kwargs_big_function.bigFunction(1, 2, 3, 4, 5, 6, a=1)

        mock_print.assert_called_once_with(
            "Too many positional arguments. Maximum allowed is 5."
        )

    @mock.patch("builtins.print")
    def test_big_function_too_many_keyword_arguments(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, 2, 3, a=1, b=2, c=3, d=4, e=5, f=6)

        mock_print.assert_called_once_with(
            "Too many keyword arguments. Maximum allowed is 5."
        )

    @mock.patch("builtins.print")
    def test_big_function_non_integer_positional_arguments(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, "two", 3, a=1)

        mock_print.assert_called_once_with("All positional arguments must be integers.")

    @mock.patch("builtins.print")
    def test_big_function_non_integer_keyword_argument_values(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, 2, 3, a=1, b="two")

        mock_print.assert_called_once_with(
            "All keyword argument values must be integers."
        )

    @mock.patch("builtins.print")
    def test_big_function_empty_keyword_argument_keys(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, 2, 3, a=1, b=2, c=3, **{"": 6})

        mock_print.assert_called_once_with("Keyword argument keys cannot be empty.")

    @mock.patch("builtins.print")
    def test_big_function_negative_positional_arguments(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, -2, 3, a=1)

        mock_print.assert_called_once_with("Positional arguments cannot be negative.")

    @mock.patch("builtins.print")
    def test_big_function_negative_keyword_argument_values(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, 2, 3, a=1, b=-2)

        mock_print.assert_called_once_with(
            "Keyword argument values cannot be negative."
        )

    @mock.patch("builtins.print")
    def test_big_function_duplicate_positional_arguments(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, 2, 2, a=1)

        mock_print.assert_called_once_with("Positional arguments must be unique.")

    @mock.patch("builtins.print")
    def test_big_function_valid_arguments(self, mock_print):
        fncs_args_kwargs_big_function.bigFunction(1, 2, 3, a=4, b=5)

        mock_print.assert_any_call("Positional arguments:", (1, 2, 3))
        mock_print.assert_any_call("Keyword arguments:", {"a": 4, "b": 5})
        self.assertEqual(mock_print.call_count, 2)


if __name__ == "__main__":
    unittest.main()
