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

    def test_capitalize(self):
        # Arrange
        line = "foo"
        expected = "Foo"

        # Act
        result = line.capitalize()

        # Assert
        self.assertEqual(result, expected)

    def test_casefold(self):
        # Arrange
        line = "FOO"
        expected = "foo"

        # Act
        result = line.casefold()

        # Assert
        self.assertEqual(result, expected)

    def test_center(self):
        # Arrange
        line = "foo"
        expected = '   foo    '

        # Act
        result = line.center(10)

        # Assert
        self.assertEqual(result, expected)

    def test_count(self):
        # Arrange
        line = "foo bar foo"
        expected = 2

        # Act
        result = line.count("foo")

        # Assert
        self.assertEqual(result, expected)

    def test_enconde(self):
        # Arrange
        line = "foo"
        expected = b"foo"

        # Act
        result = line.encode()

        # Assert
        self.assertEqual(result, expected)
    def test_endswith(self):
        # Arrange
        line = "foo"
        expected = True

        # Act
        result = line.endswith("o")

        # Assert
        self.assertEqual(result, expected)
    def test_expandtabs(self):
        # Arrange
        line = "foo\tbar"
        expected = "foo     bar"

        # Act
        result = line.expandtabs(8)

        # Assert
        self.assertEqual(result, expected)
    def test_find(self):
        # Arrange
        line = "foo bar foo"
        expected = 4

        # Act
        result = line.find("bar")

        # Assert
        self.assertEqual(result, expected)
    def test_format(self):
        # Arrange
        line = "foo {}"
        expected = "foo bar"

        # Act
        result = line.format("bar")

        # Assert
        self.assertEqual(result, expected)
    def test_format_map(self):
        # Arrange
        line = "foo {name}"
        expected = "foo bar"
        mapping = {"name": "bar"}

        # Act
        result = line.format_map(mapping)

        # Assert
        self.assertEqual(result, expected)
    def test_index(self):
        # Arrange
        line = "foo bar foo"
        expected = 4

        # Act
        result = line.index("bar")

        # Assert
        self.assertEqual(result, expected)
    def test_isalnum(self):
        # Arrange
        line = "foo123"
        expected = True

        # Act
        result = line.isalnum()

        # Assert
        self.assertEqual(result, expected)
    def test_isalpha(self):
        # Arrange
        line = "foo"
        expected = True

        # Act
        result = line.isalpha()

        # Assert
        self.assertEqual(result, expected)
    def test_isdigit(self):
        # Arrange
        line = "123"
        expected = True

        # Act
        result = line.isdigit()

        # Assert
        self.assertEqual(result, expected)
    def test_islower(self):
        # Arrange
        line = "foo"
        expected = True

        # Act
        result = line.islower()

        # Assert
        self.assertEqual(result, expected)
    def test_isspace(self):
        # Arrange
        line = "   "
        expected = True

        # Act
        result = line.isspace()

        # Assert
        self.assertEqual(result, expected)
    def test_istitle(self):
        # Arrange
        line = "Foo Bar"
        expected = True

        # Act
        result = line.istitle()

        # Assert
        self.assertEqual(result, expected)                                            


if __name__ == "__main__":
    unittest.main()
