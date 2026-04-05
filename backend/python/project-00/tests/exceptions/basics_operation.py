import unittest
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "../src"))
)
from exceptions.basics_operation import BasicsOperation


class BasicsOperationTestCase(unittest.TestCase):
    def test_division_by_zero(self):
        operation = BasicsOperation(10, 0)
        with self.assertRaises(ValueError):
            operation.divide()

    def test_invalid_type_addition(self):
        with self.assertRaises(TypeError):
            operation = BasicsOperation("string", 5)
            operation.add()

    def test_invalid_type_subtraction(self):
        with self.assertRaises(TypeError):
            operation = BasicsOperation(5, "string")
            operation.subtract()

    def test_invalid_type_multiplication(self):
        with self.assertRaises(TypeError):
            operation = BasicsOperation("string", "string")
            operation.multiply()

    def test_invalid_type_division(self):
        with self.assertRaises(TypeError):
            operation = BasicsOperation("string", 5)
            operation.divide()

    def test_division(self):
        operation = BasicsOperation(10, 2)
        self.assertEqual(operation.divide(), 5)

    def test_addition(self):
        operation = BasicsOperation(10, 5)
        self.assertEqual(operation.add(), 15)

    def test_subtraction(self):
        operation = BasicsOperation(10, 5)
        self.assertEqual(operation.subtract(), 5)

    def test_multiplication(self):
        operation = BasicsOperation(10, 5)
        self.assertEqual(operation.multiply(), 50)

    def test_str_representation(self):
        operation = BasicsOperation(10, 5)
        self.assertEqual(str(operation), "BasicsOperation(a=10, b=5)")

    def test_str_representation_with_floats(self):
        operation = BasicsOperation(10.5, 5.5)
        self.assertEqual(str(operation), "BasicsOperation(a=10.5, b=5.5)")

    def test_str_representation_with_invalid_types(self):
        operation = BasicsOperation("string", "string")
        self.assertEqual(str(operation), "BasicsOperation(a=string, b=string)")

    def test_str_representation_with_mixed_types(self):
        operation = BasicsOperation(10, "string")
        self.assertEqual(str(operation), "BasicsOperation(a=10, b=string)")

    def test_str_representation_with_none(self):
        operation = BasicsOperation(None, None)
        self.assertEqual(str(operation), "BasicsOperation(a=None, b=None)")

    def test_add_type_error_message(self):
        with self.assertRaises(TypeError) as context:
            operation = BasicsOperation("string", 5)
            operation.add()
        self.assertEqual(str(context.exception), "Both a and b must be numbers")

    def test_division_by_zero_error_message(self):
        with self.assertRaises(ValueError) as context:
            operation = BasicsOperation(10, 0)
            operation.divide()
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_subtract_type_error_message(self):
        with self.assertRaises(TypeError) as context:
            operation = BasicsOperation(5, "string")
            operation.subtract()
        self.assertEqual(str(context.exception), "Both a and b must be numbers")

    def test_multiply_type_error_message(self):
        with self.assertRaises(TypeError) as context:
            operation = BasicsOperation("string", "string")
            operation.multiply()
        self.assertEqual(str(context.exception), "Both a and b must be numbers")

    def test_divide_type_error_message(self):
        with self.assertRaises(TypeError) as context:
            operation = BasicsOperation("string", 5)
            operation.divide()
        self.assertEqual(str(context.exception), "Both a and b must be numbers")


if __name__ == "__main__":
    unittest.main()
