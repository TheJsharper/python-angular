import unittest


class TestStringMethod(unittest.TestCase):

    def test_upper(self):
        # Arrange
        line = "foo"
        expected = "FOO"

        # Act
        result = line.upper()

        # Assert
        self.assertEqual(result, expected)

    def test_lower(self):
        # Arrange
        line = "FOO"
        expected = "foo"

        # Act
        result = line.lower()

        # Assert
        self.assertEqual(result, expected)

    def test_isupperTrue(self):
        # Arrange
        line = "FOO"

        # Act
        result = line.isupper()

        # Assert
        self.assertTrue(result)

    def test_isupperFalse(self):
        # Arrange
        line = "Foo"

        # Act
        result = line.isupper()

        # Assert
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
