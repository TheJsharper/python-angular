import unittest


class TuplesJoinTestCase(unittest.TestCase):
    def test_tuple_join(self):
        # Arrange
        my_tuple = ("Hello", "World")
        expected = "Hello World"

        # Act
        result = " ".join(my_tuple)

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_join_with_different_separator(self):
        # Arrange
        my_tuple = ("Hello", "World")
        expected = "Hello-World"

        # Act
        result = "-".join(my_tuple)

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_join_with_empty_string_separator(self):
        # Arrange
        my_tuple = ("Hello", "World")
        expected = "HelloWorld"

        # Act
        result = "".join(my_tuple)

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_join_with_empty_tuple(self):
        # Arrange
        my_tuple = ()
        expected = ""

        # Act
        result = " ".join(my_tuple)

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_join_with_single_element(self):
        # Arrange
        my_tuple = ("Hello",)
        expected = "Hello"

        # Act
        result = " ".join(my_tuple)

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_concatenation_with_plus_operator(self):
        # Arrange
        tuple1 = ("a", "b", "c")
        tuple2 = (1, 2, 3)
        expected = ("a", "b", "c", 1, 2, 3)

        # Act
        tuple3 = tuple1 + tuple2

        # Assert
        self.assertEqual(tuple3, expected)

    def test_tuple_repetition_with_multiplication(self):
        # Arrange
        fruits = ("apple", "banana", "cherry")
        expected = (
            "apple",
            "banana",
            "cherry",
            "apple",
            "banana",
            "cherry",
        )

        # Act
        mytuple = fruits * 2

        # Assert
        self.assertEqual(mytuple, expected)


if __name__ == "__main__":
    unittest.main()
