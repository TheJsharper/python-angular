import unittest

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)


from objects.static_methods.person_static_method import PersonStaticMethod


class PersonStaticMethodTestCase(unittest.TestCase):
    def test_static_method(self):
        person = PersonStaticMethod("Alice", 30)
        self.assertTrue(PersonStaticMethod.is_adult(person.age))

        person2 = PersonStaticMethod("Anne", 10)
        self.assertEqual(person2.is_adult(person2.age), False)

    def test_static_method_edge_cases(self):

        self.assertTrue(PersonStaticMethod.is_adult(18))  # Edge case: exactly 18

        self.assertFalse(PersonStaticMethod.is_adult(17))  # Edge case: just under 18

    def test_static_method_invalid_input(self):
        with self.assertRaises(TypeError):
            PersonStaticMethod.is_adult(
                "twenty"
            )  # Invalid input: string instead of int

        with self.assertRaises(TypeError):
            PersonStaticMethod.is_adult(None)  # Invalid input: None instead of int


if __name__ == "__main__":
    unittest.main()
