import unittest
import sys
import os
from unittest import mock
#from  src.own_module import mymodule
# Add src to path to import mymodule
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src")))

from own_module import mymodule

class MyModuleTestCase(unittest.TestCase):
    @mock.patch("builtins.print")
    def test_greeting(self, mock_print):
        # Arrange
        name = "Jonathan"

        # Act
        mymodule.greeting(name)

        # Assert
        mock_print.assert_called_once_with("Hello, " + name)

    def test_person1_variable(self):
        # Arrange
        #from own_module import mymodule

        # Act
        person = mymodule.person1

        # Assert
        self.assertEqual(person["name"], "John")
        self.assertEqual(person["age"], 36)
        self.assertEqual(person["country"], "Norway")

    def test_import_mymodule_access_age(self):
        """
        from own_module import mymodule
        a = mymodule.person1["age"]
        """
        # Arrange

        #from own_module import mymodule

        # Act
        a = mymodule.person1["age"]

        # Assert
        self.assertEqual(a, 36)

if __name__ == "__main__":
    unittest.main()        