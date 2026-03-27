import unittest
from unittest import mock


class FncsArgsKwargsTestCase(unittest.TestCase):
    def test_fncs_args_kwargs_with_args(self):
        # Arrange
        def sum_numbers(*args):
            return sum(args)

        expected = 10

        # Act
        result = sum_numbers(1, 2, 3, 4)

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_args_kwargs_with_kwargs(self):
        # Arrange
        def greet(name, greeting="Hello"):
            return f"{greeting}, {name}!"

        expected = "Hi, Alice!"

        # Act
        result = greet(name="Alice", greeting="Hi")

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_args_kwargs_with_mixed_args_kwargs(self):
        # Arrange
        def describe_person(name, age, **kwargs):
            description = f"{name} is {age} years old."
            for key, value in kwargs.items():
                description += f" {key.capitalize()}: {value}."
            return description

        expected = "Alice is 30 years old. Country: USA. Occupation: Engineer."

        # Act
        result = describe_person("Alice", 30, country="USA", occupation="Engineer")

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_args_kwargs_sum_with_numbers_varargs(self):
        # Arrange
        def my_function(*numbers):
            total = 0
            for num in numbers:
                total += num
            return total

        # Act
        result = my_function(1, 2, 3, 4)

        # Assert
        self.assertEqual(result, 10)

    def test_fncs_args_kwargs_with_kid_dictionary(self):
        # Arrange
        def my_function(**kid):
            print("His last name is " + kid["lname"])

        # Act & Assert
        with mock.patch("builtins.print") as mock_print:
            my_function(fname="Tobias", lname="Refsnes")
            mock_print.assert_called_once_with("His last name is Refsnes")

    def test_fncs_args_kwargs_with_myvar_dictionary_details(self):
        # Arrange
        def my_function(**myvar):
            print("Type:", type(myvar))
            print("Name:", myvar["name"])
            print("Age:", myvar["age"])
            print("All data:", myvar)

        # Act & Assert
        with mock.patch("builtins.print") as mock_print:
            my_function(name="Alice", age=30)

            self.assertEqual(mock_print.call_count, 4)
            mock_print.assert_any_call("Type:", dict)
            mock_print.assert_any_call("Name:", "Alice")
            mock_print.assert_any_call("Age:", 30)
            mock_print.assert_any_call("All data:", {"name": "Alice", "age": 30})

    def test_fncs_args_kwargs_username_with_additional_details(self):
        # Arrange
        def my_function(username, **details):
            print("Username:", username)
            print("Additional details:")
            for key, value in details.items():
                print(" ", key + ":", value)

        # Act & Assert
        with mock.patch("builtins.print") as mock_print:
            my_function("emil123", age=25, city="Oslo", hobby="coding")

            expected_calls = [
                mock.call("Username:", "emil123"),
                mock.call("Additional details:"),
                mock.call(" ", "age:", 25),
                mock.call(" ", "city:", "Oslo"),
                mock.call(" ", "hobby:", "coding"),
            ]
            mock_print.assert_has_calls(expected_calls)
            self.assertEqual(mock_print.call_count, 5)

    def test_fncs_args_kwargs_with_title_args_and_kwargs(self):
        # Arrange
        def my_function(title, *args, **kwargs):
            print("Title:", title)
            print("Positional arguments:", args)
            print("Keyword arguments:", kwargs)

        # Act & Assert
        with mock.patch("builtins.print") as mock_print:
            my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")

            expected_calls = [
                mock.call("Title:", "User Info"),
                mock.call("Positional arguments:", ("Emil", "Tobias")),
                mock.call("Keyword arguments:", {"age": 25, "city": "Oslo"}),
            ]
            mock_print.assert_has_calls(expected_calls)
            self.assertEqual(mock_print.call_count, 3)

    def test_fncs_args_unpack_list_into_function_arguments(self):
        # Arrange
        def my_function(a, b, c):
            return a + b + c

        numbers = [1, 2, 3]

        # Act
        result = my_function(*numbers)

        # Assert
        self.assertEqual(result, 6)

    def test_fncs_kwargs_unpack_dictionary_into_function_arguments(self):
        # Arrange
        def my_function(fname, lname):
            print("Hello", fname, lname)

        person = {"fname": "Emil", "lname": "Refsnes"}

        # Act & Assert
        with mock.patch("builtins.print") as mock_print:
            my_function(**person)
            mock_print.assert_called_once_with("Hello", "Emil", "Refsnes")


if __name__ == "__main__":
    unittest.main()
