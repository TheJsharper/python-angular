import unittest


class TestStringMethod(unittest.TestCase):

    def test_istitleTrue(self):
        # Arrange
        line = "Foo Bar"

        # Act
        result = line.istitle()

        # Assert
        self.assertTrue(result)

    def test_istitleFalse(self):
        # Arrange
        line = "foo bar"

        # Act
        result = line.istitle()

        # Assert
        self.assertFalse(result)
    def test_isupperFalse(self):
        # Arrange
        line = "Foo"

        # Act
        result = line.isupper()

        # Assert
        self.assertFalse(result)
    def test_isupperTrue(self):
        # Arrange
        line = "FOO"

        # Act
        result = line.isupper()

        # Assert
        self.assertTrue(result)
    
    def test_join(self):
        # Arrange
        line = ["foo", "bar", "baz"]
        expected = "foo-bar-baz"

        # Act
        result = "-".join(line)

        # Assert
        self.assertEqual(result, expected)
    def test_lstrip(self):
        # Arrange
        line = "   foo"
        expected = "foo"

        # Act
        result = line.lstrip()

        # Assert
        self.assertEqual(result, expected)
    def test_maketrans(self):
        # Arrange
        line = "foo bar"
        expected = "f00 b4r"

        # Act
        translation_table = str.maketrans("oar", "04r")
        result = line.translate(translation_table)

        # Assert
        self.assertEqual(result, expected)
    def test_partition(self):
        # Arrange
        line = "foo bar baz"
        expected = ("foo", " ", "bar baz")

        # Act
        result = line.partition(" ")

        # Assert
        self.assertEqual(result, expected)
    def test_replace(self):
        # Arrange
        line = "foo bar foo"
        expected = "foo baz foo"

        # Act
        result = line.replace("bar", "baz")

        # Assert
        self.assertEqual(result, expected)
    def test_rfind(self):
        # Arrange
        line = "foo bar foo"
        expected = 8

        # Act
        result = line.rfind("foo")

        # Assert
        self.assertEqual(result, expected)
    def test_rindex(self):
        # Arrange
        line = "foo bar foo"
        expected = 8

        # Act
        result = line.rindex("foo")

        # Assert
        self.assertEqual(result, expected)
    def test_rjust(self):
        # Arrange
        line = "foo"
        expected = "  foo"

        # Act
        result = line.rjust(5)

        # Assert
        self.assertEqual(result, expected)
    def test_rpartition(self):
        # Arrange
        line = "foo bar baz"
        expected = ("foo bar", " ", "baz")

        # Act
        result = line.rpartition(" ")

        # Assert
        self.assertEqual(result, expected)
    def test_rsplit(self):
        # Arrange
        line = "foo bar baz"
        expected = ["foo", "bar", "baz"]

        # Act
        result = line.rsplit()

        # Assert
        self.assertEqual(result, expected)
    def test_rstrip(self):
        # Arrange
        line = "foo   "
        expected = "foo"

        # Act
        result = line.rstrip()

        # Assert
        self.assertEqual(result, expected)
    def test_split(self):
        # Arrange
        line = "foo bar baz"
        expected = ["foo", "bar", "baz"]

        # Act
        result = line.split()

        # Assert
        self.assertEqual(result, expected)
    def test_splitlines(self):
        # Arrange
        line = "foo\nbar\nbaz"
        expected = ["foo", "bar", "baz"]

        # Act
        result = line.splitlines()

        # Assert
        self.assertEqual(result, expected)
    def test_startswith(self):
        # Arrange
        line = "foo bar"
        expected = True

        # Act
        result = line.startswith("foo")

        # Assert
        self.assertEqual(result, expected)
    def test_strip(self):
        # Arrange
        line = "   foo   "
        expected = "foo"

        # Act
        result = line.strip()

        # Assert
        self.assertEqual(result, expected)
    def test_swapcase(self):
        # Arrange
        line = "Foo Bar"
        expected = "fOO bAR"

        # Act
        result = line.swapcase()

        # Assert
        self.assertEqual(result, expected)
    def test_title(self):
        # Arrange
        line = "foo bar"
        expected = "Foo Bar"

        # Act
        result = line.title()

        # Assert
        self.assertEqual(result, expected)
    def test_translate(self):
        # Arrange
        line = "foo bar"
        expected = "f00 b4r"

        # Act
        translation_table = str.maketrans("oar", "04r")
        result = line.translate(translation_table)

        # Assert
        self.assertEqual(result, expected)
    def test_upper(self):
        # Arrange
        line = "foo"
        expected = "FOO"

        # Act
        result = line.upper()

        # Assert
        self.assertEqual(result, expected)
    def test_zfill(self):
        # Arrange
        line = "foo"
        expected = "000foo"

        # Act
        result = line.zfill(6)

        # Assert
        self.assertEqual(result, expected)
                                                                                                   

if __name__ == "__main__":
    unittest.main()
