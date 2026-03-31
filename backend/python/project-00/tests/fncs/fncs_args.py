import unittest


import sys
import os
from unittest import mock

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from fncs import fncs_args


class FncsArgsTestCase(unittest.TestCase):
    @mock.patch("builtins.print")
    def test_fn_arg_integer_with_no_arguments(self, mock_print):
        # Arrange

        # Act
        fncs_args.fn_arg_integer()

        # Assert
       
        mock_print.assert_called_once_with("Arguments should not be None.")

    @mock.patch("builtins.print")
    def test_fn_arg_integer_with_none_arguments(self, mock_print):
        # Arrange

        # Act
        fncs_args.fn_arg_integer(None, None)

        # Assert
        mock_print.assert_called_once_with("Arguments should not be None.")

    @mock.patch("builtins.print")
    def test_fn_arg_integer_with_zero_arguments(self, mock_print):
        # Arrange

        # Act
        fncs_args.fn_arg_integer(0, 0)

        # Assert
        mock_print.assert_called_once_with("Arguments should not be zero.")

    @mock.patch("builtins.print")
    def test_fn_arg_integer_with_non_integer_arguments(self, mock_print):
        # Arrange

        # Act
        fncs_args.fn_arg_integer(1, "two", 3.0)

        # Assert
        mock_print.assert_called_once_with("It must be an integer.")

    @mock.patch("builtins.print")
    def test_fn_arg_integer_with_valid_arguments(self, mock_print):
        # Arrange

        # Act
        fncs_args.fn_arg_integer(1, 2, 3)

        # Assert
        mock_print.assert_called_once_with("Positional arguments:", (1, 2, 3))


if __name__ == "__main__":
    unittest.main()
