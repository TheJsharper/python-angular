import unittest
import sys
import os
import unittest.mock

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from objects.person import Person


class PersonTestCase(unittest.TestCase):
    def test_person(self):
        person = Person("John", 30)
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 30)
        self.assertEqual(person.work(), "John is working.")
        self.assertEqual(str(person), "John is 30 years old.")

    def test_person_with_different_values(self):
        person = Person("Alice", 25)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 25)
        self.assertEqual(person.work(), "Alice is working.")
        self.assertEqual(str(person), "Alice is 25 years old.")

    @unittest.mock.patch("builtins.print")
    def test_person_print(self, mock_print):
        person = Person("Bob", 40)
        print(str(person))
        mock_print.assert_called_with("Bob is 40 years old.")

    @unittest.mock.patch("builtins.print")
    def test_person_work_print(self, mock_print):
        person = Person("Charlie", 35)
        print(person.work())
        mock_print.assert_called_with("Charlie is working.")

    @unittest.mock.patch("builtins.print")
    def test_person_str_print(self, mock_print):
        person = Person("David", 28)
        print(str(person))
        mock_print.assert_called_with("David is 28 years old.")

    @unittest.mock.patch("builtins.print")
    def test_person_work_str_print(self, mock_print):
        person = Person("Eve", 22)
        print(str(person.work()))
        mock_print.assert_called_with("Eve is working.")


if __name__ == "__main__":
    unittest.main()
