
import unittest


class FncsBasicsTestCase(unittest.TestCase):
    def test_fncs_basics(self):
        # Arrange
        def greet(name: str) -> str:
            return f"Hello, {name}!"

        expected = "Hello, Alice!"

        # Act
        result = greet("Alice")

        # Assert
        self.assertEqual(result, expected)
    def test_fncs_with_multiple_arguments(self):
        # Arrange
        def add(a: int, b: int) -> int:
            return a + b

        expected = 5

        # Act
        result = add(2, 3)

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_return_dictionary(self):
        # Arrange
        def get_car() -> dict:
            return {"brand": "Ford", "model": "Mustang", "year": 1964}

        # Act
        result = get_car()

        # Assert
        self.assertIsInstance(result, dict)
        self.assertEqual(result["brand"], "Ford")
        self.assertEqual(result["model"], "Mustang")
        self.assertEqual(result["year"], 1964)

    def test_fncs_return_list(self):
        # Arrange
        def get_fruits() -> list:
            return ["apple", "banana", "cherry"]

        # Act
        result = get_fruits()

        # Assert
        self.assertIsInstance(result, list)
        self.assertEqual(result, ["apple", "banana", "cherry"])

    def test_fncs_return_set(self):
        # Arrange
        def get_colors() -> set:
            return {"red", "green", "blue"}

        # Act
        result = get_colors()

        # Assert
        self.assertIsInstance(result, set)
        self.assertEqual(result, {"red", "green", "blue"})

    def test_fncs_return_tuple(self):
        # Arrange
        def get_coordinates() -> tuple:
            return (10, 20)

        # Act
        result = get_coordinates()

        # Assert
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (10, 20))
        self.assertEqual(result[0], 10)
        self.assertEqual(result[1], 20)

    def test_fncs_arguments_type_check_and_raises_type_error(self):
        # Arrange
        def add_numbers(a: int, b: int) -> int:
            if not isinstance(a, int) or not isinstance(b, int):
                raise TypeError("Both arguments must be integers")
            return a + b

        # Act & Assert
        self.assertEqual(add_numbers(2, 3), 5)
        with self.assertRaises(TypeError):
            add_numbers("2", 3)
        with self.assertRaises(TypeError):
            add_numbers(2, None)

    def test_fncs_dictionary_argument_type_check_and_raises_type_error(self):
        # Arrange
        def get_name(person: dict) -> str:
            if not isinstance(person, dict):
                raise TypeError("Argument must be a dictionary")
            if "name" not in person:
                raise KeyError("Missing 'name' key")
            return person["name"]

        # Act & Assert
        self.assertEqual(get_name({"name": "Alice"}), "Alice")
        with self.assertRaises(TypeError):
            get_name(["Alice"])
        with self.assertRaises(KeyError):
            get_name({"age": 30})

    def test_fncs_accepts_different_data_types_as_arguments(self):
        # Arrange
        def describe_input(value):
            return type(value).__name__, value

        # Act
        string_result = describe_input("hello")
        number_result = describe_input(42)
        list_result = describe_input([1, 2, 3])
        dict_result = describe_input({"name": "Alice"})

        # Assert
        self.assertEqual(string_result, ("str", "hello"))
        self.assertEqual(number_result, ("int", 42))
        self.assertEqual(list_result, ("list", [1, 2, 3]))
        self.assertEqual(dict_result, ("dict", {"name": "Alice"}))

    def test_fncs_sending_dictionary_as_argument(self):
        # Arrange
        def get_model(car: dict) -> str:
            return car["model"]

        car = {"brand": "Ford", "model": "Mustang", "year": 2024}

        # Act
        result = get_model(car)

        # Assert
        self.assertEqual(result, "Mustang")

    def test_fncs_positional_only_arguments(self):
        # Arrange
        def greet(name, /):
            return f"Hello, {name}!"

        # Act & Assert
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        with self.assertRaises(TypeError):
            greet(name="Alice")

    def test_fncs_positional_only_and_keyword_only_arguments(self):
        # Arrange
        def person_info(name, /, *, age):
            return f"{name} is {age} years old"

        # Act & Assert
        self.assertEqual(person_info("Alice", age=30), "Alice is 30 years old")

        # name is positional-only
        with self.assertRaises(TypeError):
            person_info(name="Alice", age=30)

        # age is keyword-only
        with self.assertRaises(TypeError):
            person_info("Alice", 30)

if __name__ == "__main__":
    unittest.main()        