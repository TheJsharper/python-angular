import unittest
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)


from objects.class_methods.person_class_method import PersonClassMethod


class PersonClassMethodTestCase(unittest.TestCase):
    def test_from_birth_year(self):

        person = PersonClassMethod.from_birth_year("Alice", 1990)
        self.assertEqual(person.name, "Alice")
        self.assertEqual(person.age, 34)  # Assuming the current year is 2024

    def test_change_species(self):
        person = PersonClassMethod("Bob", 30)
        self.assertEqual(person.species, "Human")
        PersonClassMethod.change_species("Alien")
        self.assertEqual(PersonClassMethod.species, "Alien")
        self.assertEqual(person.species, "Alien")

    def test_change_species_instance(self):
        person1 = PersonClassMethod("Charlie", 25)
        person2 = PersonClassMethod("Dave", 40)

        self.assertEqual(person1.species, "Human")
        self.assertEqual(person2.species, "Human")

        PersonClassMethod.change_species("Martian")

        self.assertEqual(person1.species, "Martian")
        self.assertEqual(person2.species, "Martian")

    def test_change_species_multiple_times(self):
        person = PersonClassMethod("Eve", 28)

        self.assertEqual(person.species, "Human")

        PersonClassMethod.change_species("Cyborg")
        self.assertEqual(person.species, "Cyborg")

        PersonClassMethod.change_species("Android")
        self.assertEqual(person.species, "Android")

    def test_from_birth_year_edge_case(self):
        person = PersonClassMethod.from_birth_year("Frank", 2024)
        self.assertEqual(person.name, "Frank")
        self.assertEqual(person.age, 0)  # Birth year is the current year

    def tearDown(self) -> None:
        # Reset species to "Human" after each test
        PersonClassMethod.change_species("Human")


if __name__ == "__main__":
    unittest.main()
