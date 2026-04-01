import unittest
import sys
import os
import unittest.mock

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)
from objects.person import Person
from objects.person_privated_attr import PersonPrivatedAttr


class PersonPrivatedAttrTestCase(unittest.TestCase):
    @unittest.mock.patch("builtins.print")
    def test_person_privated_attr_print(self, mock_print):
        person = PersonPrivatedAttr("David", 28)
        print(str(person))
        mock_print.assert_called_with("David is 28 years old.")

    def test_person_privated_attr(self):
        person = PersonPrivatedAttr("John", 30)
        self.assertEqual(str(person), "John is 30 years old.")
        self.assertEqual(person.work(), "John is working.")
        self.assertEqual(person.get_password(), "encrypted_secret 123")
        person.set_password("new secret 456")
        self.assertEqual(person.get_password(), "encrypted_new secret 456")

    def test_person_privated_attr_with_different_values(self):
        person = PersonPrivatedAttr("Alice", 25)
        self.assertEqual(str(person), "Alice is 25 years old.")
        self.assertEqual(person.work(), "Alice is working.")
        self.assertEqual(person.get_password(), "encrypted_secret 123")
        person.set_password("another secret 789")
        self.assertEqual(person.get_password(), "encrypted_another secret 789")

    def test_person_privated_attr_getters(self):
        person = PersonPrivatedAttr("Bob", 40)
        self.assertEqual(person.get_name(), "Bob")
        self.assertEqual(person.get_age(), 40)

    def test_person_privated_attr_access_private_attributes(self):
        person = PersonPrivatedAttr("Charlie", 35)
        with self.assertRaises(AttributeError):
            _ = person.__name
        with self.assertRaises(AttributeError):
            _ = person.__age
        with self.assertRaises(AttributeError):
            _ = person.__password

    @unittest.mock.patch("builtins.print")
    def test_person_privated_attr_work_print(self, mock_print):
        person = PersonPrivatedAttr("Charlie", 35)
        print(person.work())
        mock_print.assert_called_with("Charlie is working.")


if __name__ == "__main__":
    unittest.main()
