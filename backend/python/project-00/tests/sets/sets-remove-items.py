import unittest


class SetsRemoveItemsTestCase(unittest.TestCase):
    def test_remove_set_items(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = {1, 3}

        # Act
        my_set.remove(2)

        # Assert
        self.assertEqual(my_set, expected)

    def test_remove_non_existent_item_raises_key_error(self):
        # Arrange
        my_set = {1, 2, 3}

        # Act & Assert
        with self.assertRaises(KeyError):
            my_set.remove(4)  # KeyError: 4 not found in set

    def test_discard_non_existent_item_does_not_raise_error(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = {1, 2, 3}

        # Act
        my_set.discard(4)  # no error raised

        # Assert
        self.assertEqual(my_set, expected)

    def test_pop_removes_and_returns_an_item(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        original = thisset.copy()

        # Act
        x = thisset.pop()

        # Assert
        self.assertIn(x, original)
        self.assertNotIn(x, thisset)
        self.assertEqual(len(thisset), len(original) - 1)

    def test_clear_removes_all_items(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}

        # Act
        thisset.clear()

        # Assert
        self.assertEqual(thisset, set())
        self.assertEqual(len(thisset), 0)

    def test_discard_non_existing_value_2_does_not_raise_error(self):
        # Arrange
        my_set = {1, 3}
        expected = {1, 3}

        # Act
        my_set.discard(2)  # no error raised even though 2 is missing

        # Assert
        self.assertEqual(my_set, expected)
    



if __name__ == "__main__":
    unittest.main()
