
import unittest
from unittest import mock


class IteratorsBuiltinTestCase(unittest.TestCase):
    def test_iterator_with_list(self):
        # Arrange
        expected = [1, 2, 3, 4]

        # Act
        iterator = iter(expected)
        result = list(iterator)

        # Assert
        self.assertEqual(result, expected)

    def test_iterator_with_tuple(self):
        # Arrange
        expected = (1, 2, 3, 4)

        # Act
        iterator = iter(expected)
        result = tuple(iterator)

        # Assert
        self.assertEqual(result, expected)

    def test_iterator_with_string(self):
        # Arrange
        expected = "Hello"

        # Act
        iterator = iter(expected)
        result = list(iterator)

        # Assert
        self.assertEqual(result, list(expected))

    def test_iterator_with_empty_list(self):
        # Arrange
        expected = []

        # Act
        iterator = iter(expected)
        result = list(iterator)

        # Assert
        self.assertEqual(result, expected)

    def test_iterator_with_different_types(self):
        # Arrange
        expected = [1, "Hello", 3.14, True]

        # Act
        iterator = iter(expected)
        result = list(iterator)

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_iterator_next(self):
        """
        Tests the use of iter() and next() on a tuple.
        """
        # Arrange
        mytuple = ("apple", "banana", "cherry")

        # Act
        myit = iter(mytuple)

        # Assert
        self.assertEqual(next(myit), "apple")
        self.assertEqual(next(myit), "banana")
        self.assertEqual(next(myit), "cherry")

        # Verify StopIteration at the end
        with self.assertRaises(StopIteration):
            next(myit)

    def test_string_iterator_next(self):
        """
        Tests the use of iter() and next() on a string.
        """
        # Arrange
        mystr = "banana"

        # Act
        myit = iter(mystr)

        # Assert
        self.assertEqual(next(myit), "b")
        self.assertEqual(next(myit), "a")
        self.assertEqual(next(myit), "n")
        self.assertEqual(next(myit), "a")
        self.assertEqual(next(myit), "n")
        self.assertEqual(next(myit), "a")

        # Verify StopIteration at the end
        with self.assertRaises(StopIteration):
            next(myit)

    @mock.patch("builtins.print")
    def test_for_loop_with_tuple(self, mock_print):
        """
        Tests for-loop iteration over a tuple.
        """
        # Arrange
        mytuple = ("apple", "banana", "cherry")

        # Act
        for x in mytuple:
            print(x)

        # Assert: print was called with each element
        mock_print.assert_any_call("apple")
        mock_print.assert_any_call("banana")
        mock_print.assert_any_call("cherry")
        self.assertEqual(mock_print.call_count, 3)

    def test_custom_iterator_mynumbers(self):
        """
        Tests a custom iterator class implementing __iter__ and __next__.
        """
        # Arrange
        class MyNumbers:
            def __iter__(self):
                self.a = 1
                return self

            def __next__(self):
                x = self.a
                self.a += 1
                return x

        # Act
        myclass = MyNumbers()
        myiter = iter(myclass)

        # Assert: Verify sequence of numbers
        self.assertEqual(next(myiter), 1)
        self.assertEqual(next(myiter), 2)
        self.assertEqual(next(myiter), 3)
        self.assertEqual(next(myiter), 4)
        self.assertEqual(next(myiter), 5)

    @mock.patch("builtins.print")
    def test_custom_iterator_mynumbers_stopiteration(self, mock_print):
        """
        Tests a custom iterator that raises StopIteration at a limit.
        """
        # Arrange
        class MyNumbers:
            def __iter__(self):
                self.a = 1
                return self

            def __next__(self):
                if self.a <= 20:
                    x = self.a
                    self.a += 1
                    return x
                else:
                    raise StopIteration

        # Act
        myclass = MyNumbers()
        myiter = iter(myclass)

        for x in myiter:
            print(x)

        # Assert: print was called exactly 20 times with values 1 to 20
        self.assertEqual(mock_print.call_count, 20)
        mock_print.assert_any_call(1)
        mock_print.assert_any_call(20)


if __name__ == "__main__":
    unittest.main()         