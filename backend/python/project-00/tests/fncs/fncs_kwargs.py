import sys
import os
import unittest

from unittest import mock

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from fncs.fncs_kwargs import fn_arg_keyword


class FncsKwargsTestCase(unittest.TestCase):
    def test_fncs_kwargs(self):
        # Arrange
        dict_input = {"a": 4, "b": 5}

        # Act
        result = fn_arg_keyword(**dict_input)

        # Assert
        self.assertEqual(result, {"a": 4, "b": 5})

    @mock.patch("builtins.print")
    def test_fncs_kwargs_no_kwargs(self, mock_print):
        # Arrange

        # Act
        result = fn_arg_keyword()

        # Assert
        self.assertEqual(result, None)
        mock_print.assert_called_once_with("No keyword arguments provided.")

    @mock.patch("builtins.print")
    def test_fncs_kwargs_one_kwarg(self, mock_print):
        # Arrange
        dict_input = {"a": 4}

        # Act
        result = fn_arg_keyword(**dict_input)

        # Assert
        self.assertEqual(result, None)
        mock_print.assert_called_once_with(
            "One keyword argument provided: " + str(dict_input)
        )

    @mock.patch("builtins.print")
    def test_fncs_kwargs_invalid_input(self, mock_print):
        # Arrange
        invalid_input = "This is not a dictionary"

        # Act & Assert
        with self.assertRaises(TypeError):
            fn_arg_keyword(**invalid_input)

    def test_fncs_kwargs_multiple_kwargs(self):
        # Arrange
        dict_input = {"a": 4, "b": 5, "c": 6}

        # Act
        result = fn_arg_keyword(**dict_input)

        # Assert
        self.assertEqual(result, {"a": 4, "b": 5, "c": 6})

    def test_fncs_kwargs_non_dict_kwargs(self):
        # Arrange
        non_dict_input = [("a", 4), ("b", 5)]

        # Act & Assert
        with self.assertRaises(TypeError):
            fn_arg_keyword(**non_dict_input)

    @mock.patch("builtins.print")
    def test_fncs_kwargs_mixed_kwargs(self, mock_print):
        # Arrange
        mixed_input = {"a": 4, "b": "five", "c": 6}

        # Act
        result = fn_arg_keyword(**mixed_input)

        # Assert
        self.assertEqual(result, None)
        mock_print.assert_called_once_with("All values must be integers.")

   # @mock.patch("builtins.print")
    def test_fncs_kwargs_non_string_keys(self):
        # Arrange
        non_string_keys_input = {1: 4, 2: 5}

        # Act
        #result = fn_arg_keyword(**non_string_keys_input)

        # Assert
        #self.assertEqual(result, None)
        with self.assertRaises(TypeError):
            fn_arg_keyword(**non_string_keys_input)


if __name__ == "__main__":
    unittest.main()
