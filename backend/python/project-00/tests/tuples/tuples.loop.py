import unittest


class TuplesLoopTestCase(unittest.TestCase):
    def test_loop_over_tuple(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected = [1, 2, 3]
        result = []

        # Act
        for item in my_tuple:
            result.append(item)

        # Assert
        self.assertEqual(result, expected)

    def test_loop_over_tuple_with_enumerate(self):
        # Arrange
        my_tuple = (10, 20, 30)
        expected = [(0, 10), (1, 20), (2, 30)]
        result = []

        # Act
        for index, item in enumerate(my_tuple):
            result.append((index, item))

        # Assert
        self.assertEqual(result, expected)

    def test_loop_over_tuple_strings(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")
        expected = ["apple", "banana", "cherry"]
        result = []

        # Act
        for x in thistuple:
            result.append(x)

        # Assert
        self.assertEqual(result, expected)

    def test_loop_over_tuple_by_index(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")
        expected = ["apple", "banana", "cherry"]
        result = []

        # Act
        for i in range(len(thistuple)):
            result.append(thistuple[i])

        # Assert
        self.assertEqual(result, expected)

    def test_loop_over_tuple_with_while(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")
        expected = ["apple", "banana", "cherry"]
        result = []
        i = 0

        # Act
        while i < len(thistuple):
            result.append(thistuple[i])
            i = i + 1

        # Assert
        self.assertEqual(result, expected)

    def test_generate_tuple_using_filtered_generator_expression(self):
        # Arrange
        thistuple = (1, 2, 3, 4, 5)
        expected = (2, 4)

        # Act
        result = tuple(x for x in thistuple if x % 2 == 0)

        # Assert
        self.assertEqual(result, expected)

    def test_find_name_in_tuple(self):
        # Arrange
        names = ("John", "Jane", "Alice", "Bob")
        target = "Alice"
        found = False

        # Act
        for name in names:
            if name == target:
                found = True
                break

        # Assert
        self.assertTrue(found)
    def test_tuple_immutable(self):
        # Arrange
        my_tuple = (1, 2, 3)

        # Act & Assert
        with self.assertRaises(TypeError):
            my_tuple[0] = (
                10  # TypeError: 'tuple' object does not support item assignment
            )
    def test_generate_tuple_using_generator_expression(self):
        # Arrange
        expected = (0, 1, 4, 9, 16)

        # Act
        my_tuple = tuple(x * x for x in range(5))   

        # Assert
        self.assertEqual(my_tuple, expected)
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
