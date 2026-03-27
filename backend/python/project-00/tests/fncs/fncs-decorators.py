import unittest
import functools


class FncsDecoratorsTestCase(unittest.TestCase):
    def test_fncs_decorators_with_simple_decorator(self):
        # Arrange
        def simple_decorator(func):
            def wrapper():
                return "Decorated: " + func()

            return wrapper

        @simple_decorator
        def greet():
            return "Hello"

        expected = "Decorated: Hello"

        # Act
        result = greet()

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_decorators_with_arguments(self):
        # Arrange
        def repeat_decorator(times):
            def decorator(func):
                def wrapper(*args, **kwargs):
                    result = ""
                    for _ in range(times):
                        result += func(*args, **kwargs) + " "
                    return result.strip()

                return wrapper

            return decorator

        @repeat_decorator(3)
        def greet(name):
            return f"Hello, {name}!"

        expected = "Hello, Alice! Hello, Alice! Hello, Alice!"

        # Act
        result = greet("Alice")

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_decorators_with_class_method(self):
        # Arrange
        def method_decorator(func):
            def wrapper(self):
                return "Decorated: " + func(self)

            return wrapper

        class Greeter:
            @method_decorator
            def greet(self):
                return "Hello"

        greeter = Greeter()
        expected = "Decorated: Hello"

        # Act
        result = greeter.greet()

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_decorators_with_multiple_decorators(self):
        # Arrange
        def uppercase_decorator(func):
            def wrapper():
                return func().upper()

            return wrapper

        def exclaim_decorator(func):
            def wrapper():
                return func() + "!"

            return wrapper

        @exclaim_decorator
        @uppercase_decorator
        def greet():
            return "Hello"

        expected = "HELLO!"

        # Act
        result = greet()

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_decorators_changecase(self):
        # Arrange
        def changecase(func):
            def myinner():
                return func().upper()

            return myinner

        @changecase
        def myfunction():
            return "Hello Sally"

        # Act
        result = myfunction()

        # Assert
        self.assertEqual(result, "HELLO SALLY")

    def test_fncs_decorators_changecase_multiple_functions(self):
        # Arrange
        def changecase(func):
            def myinner():
                return func().upper()

            return myinner

        @changecase
        def myfunction():
            return "Hello Sally"

        @changecase
        def otherfunction():
            return "I am speed!"

        # Act
        first_result = myfunction()
        second_result = otherfunction()

        # Assert
        self.assertEqual(first_result, "HELLO SALLY")
        self.assertEqual(second_result, "I AM SPEED!")

    def test_fncs_decorators_changecase_with_function_argument(self):
        # Arrange
        def changecase(func):
            def myinner(x):
                return func(x).upper()

            return myinner

        @changecase
        def myfunction(nam):
            return "Hello " + nam

        # Act
        result = myfunction("John")

        # Assert
        self.assertEqual(result, "HELLO JOHN")

    def test_fncs_decorators_changecase_with_parameter(self):
        # Arrange
        def changecase(n):
            def changecase_inner(func):
                def myinner():
                    if n == 1:
                        a = func().lower()
                    else:
                        a = func().upper()
                    return a

                return myinner

            return changecase_inner

        @changecase(1)
        def myfunction():
            return "Hello Linus"

        # Act
        result = myfunction()

        # Assert
        self.assertEqual(result, "hello linus")

    def test_fncs_decorators_changecase_with_addgreeting(self):
        # Arrange
        def changecase(func):
            def myinner():
                return func().upper()

            return myinner

        def addgreeting(func):
            def myinner():
                return "Hello " + func() + " Have a good day!"

            return myinner

        @changecase
        @addgreeting
        def myfunction():
            return "Tobias"

        # Act
        result = myfunction()

        # Assert
        self.assertEqual(result, "HELLO TOBIAS HAVE A GOOD DAY!")

    def test_fncs_function_metadata_name_and_doc(self):
        # Arrange
        def myfunction():
            "Return a positive message."
            return "Have a great day!"

        # Act
        function_name = myfunction.__name__
        function_doc = myfunction.__doc__

        # Assert
        self.assertEqual(function_name, "myfunction")
        self.assertEqual(function_doc, "Return a positive message.")

    def test_fncs_decorated_function_name_without_wraps(self):
        # Arrange
        def changecase(func):
            def myinner():
                return func().upper()

            return myinner

        @changecase
        def myfunction():
            return "Have a great day!"

        # Act
        decorated_name = myfunction.__name__

        # Assert
        # Without functools.wraps, __name__ points to the inner wrapper function.
        self.assertEqual(decorated_name, "myinner")

    def test_fncs_decorated_function_name_with_wraps(self):
        # Arrange
        def changecase(func):
            @functools.wraps(func)
            def myinner():
                return func().upper()

            return myinner

        @changecase
        def myfunction():
            return "Have a great day!"

        # Act
        decorated_name = myfunction.__name__

        # Assert
        self.assertEqual(decorated_name, "myfunction")


if __name__ == "__main__":
    unittest.main()
