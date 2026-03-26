import unittest


class TuplesBasicsTestCase(unittest.TestCase):
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

    def test_tuple_length(self):
        # Arrange
        my_tuple = (1, 2, 3)

        # Act
        length = len(my_tuple)

        # Assert
        self.assertEqual(length, 3)

    def test_tuple_concatenation(self):
        # Arrange
        tuple1 = (1, 2)
        tuple2 = (3, 4)
        expected = (1, 2, 3, 4)

        # Act
        result = tuple1 + tuple2

        # Assert
        self.assertEqual(result, expected)

    def test_single_item_tuple_syntax(self):
        # Arrange
        tuple_value = ("apple",)
        not_tuple_value = "apple"

        # Assert
        self.assertIsInstance(tuple_value, tuple)
        self.assertIsInstance(not_tuple_value, str)

    def test_tuple_types(self):
        # Arrange
        tuple1 = ("apple", "banana", "cherry")
        tuple2 = (1, 5, 7, 9, 3)
        tuple3 = (True, False, False)

        # Assert
        self.assertIsInstance(tuple1, tuple)
        self.assertIsInstance(tuple2, tuple)
        self.assertIsInstance(tuple3, tuple)
        self.assertTrue(all(isinstance(x, str) for x in tuple1))
        self.assertTrue(all(isinstance(x, int) for x in tuple2))
        self.assertTrue(all(isinstance(x, bool) for x in tuple3))

    def test_tuple_mixed_types(self):
        # Arrange
        tuple1 = ("abc", 34, True, 40, "male")
        expected_types = (str, int, bool, int, str)

        # Assert
        self.assertIsInstance(tuple1, tuple)
        self.assertEqual(tuple(type(x) for x in tuple1), expected_types)

    def test_tuple_type(self):
        # Arrange
        mytuple = ("apple", "banana", "cherry")

        # Assert
        self.assertEqual(type(mytuple), tuple)

    def test_tuple_constructor_from_tuple_literal(self):
        # Arrange
        expected = ("apple", "banana", "cherry")

        # Act
        thistuple = tuple(("apple", "banana", "cherry"))

        # Assert
        self.assertEqual(thistuple, expected)
        self.assertIsInstance(thistuple, tuple)

    def test_tuple_constructor_from_list(self):
        # Arrange
        source = ["apple", "banana", "cherry"]
        expected = ("apple", "banana", "cherry")

        # Act
        thistuple = tuple(source)

        # Assert
        self.assertEqual(thistuple, expected)
        self.assertIsInstance(thistuple, tuple)

    def test_tuple_is_ordered_unchangeable_and_allows_duplicates(self):
        # Arrange
        mytuple = ("apple", "banana", "cherry", "apple")

        # Assert: ordered
        self.assertEqual(mytuple[0], "apple")
        self.assertEqual(mytuple[1], "banana")
        self.assertEqual(mytuple[2], "cherry")
        self.assertEqual(mytuple[3], "apple")

        # Assert: allows duplicates
        self.assertEqual(mytuple.count("apple"), 2)

        # Assert: unchangeable (immutable)
        with self.assertRaises(TypeError):
            mytuple[1] = "orange"

    def test_tuple_access_by_index(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")

        # Act
        result = thistuple[1]

        # Assert
        self.assertEqual(result, "banana")


if __name__ == "__main__":
    unittest.main()
