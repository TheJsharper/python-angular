import unittest


class TuplesAccessTestCase(unittest.TestCase):
    def test_access_tuple_items(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected = 2

        # Act
        result = my_tuple[1]

        # Assert
        self.assertEqual(result, expected)

    def test_access_tuple_items_with_negative_index(self):
        # Arrange
        my_tuple = (1, 2, 3)
        expected = 3

        # Act
        result = my_tuple[-1]

        # Assert
        self.assertEqual(result, expected)

    def test_access_tuple_items_with_slice(self):
        # Arrange
        my_tuple = (1, 2, 3, 4, 5)
        expected = (2, 3, 4)

        # Act
        result = my_tuple[1:4]

        # Assert
        self.assertEqual(result, expected)

    def test_access_tuple_items_with_slice_and_step(self):
        # Arrange
        my_tuple = (1, 2, 3, 4, 5)
        expected = (1, 3, 5)

        # Act
        result = my_tuple[0:5:2]

        # Assert
        self.assertEqual(result, expected)

    def test_access_tuple_items_with_slice_and_negative_step(self):
        # Arrange
        my_tuple = (1, 2, 3, 4, 5)
        expected = (5, 4, 3)

        # Act
        result = my_tuple[4:1:-1]

        # Assert
        self.assertEqual(result, expected)

    def test_access_tuple_slice_from_start(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        expected = ("apple", "banana", "cherry", "orange")

        # Act
        result = thistuple[:4]

        # Assert
        self.assertEqual(result, expected)

    def test_access_tuple_slice_to_end(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        expected = ("cherry", "orange", "kiwi", "melon", "mango")

        # Act
        result = thistuple[2:]

        # Assert
        self.assertEqual(result, expected)

    def test_access_tuple_slice_with_negative_indices(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
        expected = ("orange", "kiwi", "melon")

        # Act
        result = thistuple[-4:-1]

        # Assert
        self.assertEqual(result, expected)

    def test_tuple_membership_check(self):
        # Arrange
        thistuple = ("apple", "banana", "cherry")

        # Assert
        self.assertIn("apple", thistuple)
        self.assertNotIn("mango", thistuple)


if __name__ == "__main__":
    unittest.main()
