import unittest


class TuplesUnpackTestCase(unittest.TestCase):
    def test_unpack_tuple(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected_a = 1
        expected_b = 2
        expected_c = 3

        # Act
        a, b, c = my_tuple

        # Assert
        self.assertEqual(a, expected_a)
        self.assertEqual(b, expected_b)
        self.assertEqual(c, expected_c)

    def test_unpack_tuple_with_different_length(self):
        # Arrange
        my_tuple = (1, 2, 3)

        # Act & Assert
        with self.assertRaises(ValueError):
            a, b = my_tuple  # ValueError: too many values to unpack (expected 2)

    def test_unpack_tuple_with_different_length_2(self):
        # Arrange
        my_tuple = (1, 2, 3)

        # Act & Assert
        with self.assertRaises(ValueError):
            a, b, c, d = (
                my_tuple  # ValueError: not enough values to unpack (expected 4)
            )

    def test_unpack_tuple_fruits(self):
        # Arrange
        fruits = ("apple", "banana", "cherry")

        # Act
        green, yellow, red = fruits

        # Assert
        self.assertEqual(green, "apple")
        self.assertEqual(yellow, "banana")
        self.assertEqual(red, "cherry")

    def test_unpack_tuple_fruits_with_different_length(self):
        # Arrange
        fruits = ("apple", "banana", "cherry")

        # Act & Assert
        with self.assertRaises(ValueError):
            green, yellow = fruits  # ValueError: too many values to unpack (expected 2)

    def test_unpack_tuple_fruits_with_different_length_2(self):
        # Arrange
        fruits = ("apple", "banana", "cherry")

        # Act & Assert
        with self.assertRaises(ValueError):
            green, yellow, red, orange = (
                fruits  # ValueError: not enough values to unpack (expected 4)
            )

    def test_unpack_tuple_with_asterisk(self):
        # Arrange
        my_tuple = (1, 2, 3, 4, 5)
        expected_a = 1
        expected_b = 2
        expected_c = [3, 4, 5]

        # Act
        a, b, *c = my_tuple

        # Assert
        self.assertEqual(a, expected_a)
        self.assertEqual(b, expected_b)
        self.assertEqual(c, expected_c)

    def test_generate_tuple_using_generator_expression(self):
        # Arrange
        expected = (0, 1, 4, 9, 16)

        # Act
        my_tuple = tuple(x * x for x in range(5))

        # Assert
        self.assertEqual(my_tuple, expected)

    def test_tuple_immutable(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected = (1, 2, 3)  # tuple is unchanged after TypeError

        # Act
        with self.assertRaises(TypeError):
            my_tuple[0] = (
                10  # TypeError: 'tuple' object does not support item assignment
            )

        # Assert
        self.assertEqual(my_tuple, expected)

    def test_tuple_immutable_with_slice(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected = (1, 2, 3)  # tuple is unchanged after TypeError

        # Act
        with self.assertRaises(TypeError):
            my_tuple[0:2] = (
                10,
                20,
            )  # TypeError: 'tuple' object does not support item assignment

        # Assert
        self.assertEqual(my_tuple, expected)

    def test_tuple_length(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected = 3

        # Act
        length = len(my_tuple)

        # Assert
        self.assertEqual(length, expected)

    def test_tuple_concatenation(self):
        # Arrange
        tuple1 = (1, 2)
        tuple2 = (3, 4)
        expected = (1, 2, 3, 4)

        # Act
        result = tuple1 + tuple2

        # Assert
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
