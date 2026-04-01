import unittest
import sys
import os
import unittest.mock

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)
from objects.person import Person
from objects.person_protected import PersonProtected


class PersonProtectedTestCase(unittest.TestCase):
    def test_person_protected(self):
        person = PersonProtected("John", 30)
        self.assertEqual(str(person), "John is 30 years old.")
        self.assertEqual(person.work(), "John is working.")

    def test_person_protected_with_different_values(self):
        person = PersonProtected("Alice", 25)
        self.assertEqual(str(person), "Alice is 25 years old.")
        self.assertEqual(person.work(), "Alice is working.")

    @unittest.mock.patch("builtins.print")
    def test_person_protected_print(self, mock_print):
        person = PersonProtected("Bob", 40)
        print(str(person))
        mock_print.assert_called_with("Bob is 40 years old.")

    @unittest.mock.patch("builtins.print")
    def test_person_protected_work_print(self, mock_print):
        person = PersonProtected("Charlie", 35)
        print(person.work())
        mock_print.assert_called_with("Charlie is working.")

    def test_person_protected_energy_depletion(self):
        person = PersonProtected("Dave", 28)
        for _ in range(10):
            person.work()  # Deplete energy
        self.assertEqual(person.work(), "Dave is too tired to work.")

    def test_person_protected_energy_recovery(self):
        person = PersonProtected("Eve", 22)
        for _ in range(10):
            person.work()  # Deplete energy
        self.assertEqual(person.work(), "Eve is too tired to work.")
        # Simulate energy recovery
        # In a real implementation, you might have a method to recover energy, but for this test, we will just reset it directly.
        person._energy = 100
        self.assertEqual(person.work(), "Eve is working.")

    def test_person_protected_energy_insufficient(self):
        person = PersonProtected("Frank", 40)
        person._energy = 5  # Set energy to a low value
        self.assertEqual(person.work(), "Frank is too tired to work.")
        self.assertEqual(person._energy, 5)  # Ensure energy is not depleted

    def test_person_protected_energy_exact(self):
        person = PersonProtected("Grace", 30)
        person._energy = 10  # Set energy to the exact amount needed
        self.assertEqual(person.work(), "Grace is working.")
        self.assertEqual(person._energy, 0)  # Ensure energy is depleted

    def test_wase_energy_directly(self):
        person = PersonProtected("Hank", 45)
        self.assertTrue(person._waseEnergy(10))  # Should succeed

    def test_wase_energy_insufficient(self):
        person = PersonProtected("Ivy", 27)
        person._energy = 5  # Set energy to a low value
        self.assertFalse(person._waseEnergy(10))  # Should fail


if __name__ == "__main__":
    unittest.main()
