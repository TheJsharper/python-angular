import unittest


class SetsAccessItemsTestCase(unittest.TestCase):
    def test_access_set_items(self):
        # Arrange
        my_set = {1, 2, 3}

        # Act
        result = 2 in my_set

        # Assert
        self.assertTrue(result)

    def test_access_set_items_with_negative_index(self):
        # Arrange
        my_set = {1, 2, 3}

        # Act
        result = 3 in my_set

        # Assert
        self.assertTrue(result)

    def test_access_set_items_with_slice(self):
        # Arrange
        my_set = {1, 2, 3, 4, 5}
        expected = {2, 3, 4}

        # Act
        result = {x for x in my_set if x in expected}

        # Assert
        self.assertEqual(result, expected)

    def test_access_set_items_with_slice_and_step(self):
        # Arrange
        my_set = {1, 2, 3, 4, 5}
        expected = {1, 3, 5}

        # Act
        result = {x for x in my_set if x % 2 == 1}

        # Assert
        self.assertEqual(result, expected)

    def test_access_set_items_with_slice_and_negative_step(self):
        # Arrange
        my_set = {1, 2, 3, 4, 5}
        expected = {5, 4, 3}

        # Act
        result = {x for x in my_set if x >= 3}

        # Assert
        self.assertEqual(result, expected)

    def test_iterate_over_set_items(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        result = set()

        # Act
        for x in thisset:
            result.add(x)

        # Assert
        self.assertEqual(result, thisset)

    def test_membership_banana_in_set(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}

        # Act
        result = "banana" in thisset

        # Assert
        self.assertTrue(result)

    def test_membership_banana_not_in_set(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}

        # Act
        result = "banana" not in thisset

        # Assert
        self.assertFalse(result)
        


if __name__ == "__main__":
    unittest.main()
