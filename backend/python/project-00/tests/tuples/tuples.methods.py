import unittest


class TuplesMethodsTestCase(unittest.TestCase):
    def test_tuple_concatenation_with_plus_operator(self):
        # Arrange
        tuple1 = (1, 2, 3)
        tuple2 = (4, 5)
        expected = (1, 2, 3, 4, 5)

        # Act
        result = tuple1 + tuple2

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_repetition_with_multiply_operator(self):
        # Arrange
        my_tuple = (1, 2)
        expected = (1, 2, 1, 2, 1, 2)

        # Act
        result = my_tuple * 3

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_concatenation_with_plus_operator_and_different_types(self):
        # Arrange
        tuple1 = (1, 2, 3)
        tuple2 = ("a", "b")
        expected = (1, 2, 3, "a", "b")

        # Act
        result = tuple1 + tuple2

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_count(self):
        # Arrange
        my_tuple = (1, 2, 3, 1, 1, 4)
        expected = 3

        # Act
        result = my_tuple.count(1)

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_index(self):
        # Arrange
        my_tuple = ("apple", "banana", "cherry")
        expected = 1

        # Act
        result = my_tuple.index("banana")

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_index_with_non_existent_value(self):
        # Arrange
        my_tuple = ("apple", "banana", "cherry")

        # Act & Assert
        with self.assertRaises(ValueError):
            my_tuple.index("orange")  # ValueError: tuple.index(x): x not found

    def test_tuple_immutable(self):
        # Arrange
        my_tuple = (1, 2, 3)

        # Act & Assert
        with self.assertRaises(TypeError):
            my_tuple[0] = (
                10  # TypeError: 'tuple' object does not support item assignment
            )

    def test_tuple_immutable_with_slice(self):
        # Arrange
        my_tuple = (1, 2, 3)

        # Act & Assert
        with self.assertRaises(TypeError):
            my_tuple[0:2] = (
                10,
                20,
            )  # TypeError: 'tuple' object does not support item assignment


if __name__ == "__main__":
    unittest.main()
