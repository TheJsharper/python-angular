import unittest


class SetsAddItemsTestCase(unittest.TestCase):
    def test_add_set_items_with_add(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = {1, 2, 3, 4}

        # Act
        my_set.add(4)

        # Assert
        self.assertEqual(my_set, expected)

    def test_add_set_items_with_update(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = {1, 2, 3, 4, 5}

        # Act
        my_set.update([4, 5])

        # Assert
        self.assertEqual(my_set, expected)

    def test_update_set_with_list(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        mylist = ["kiwi", "orange"]
        expected = {"apple", "banana", "cherry", "kiwi", "orange"}

        # Act
        thisset.update(mylist)

        # Assert
        self.assertEqual(thisset, expected)

    def test_update_set_with_another_set(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        tropical = {"pineapple", "mango", "papaya"}
        expected = {"apple", "banana", "cherry", "pineapple", "mango", "papaya"}

        # Act
        thisset.update(tropical)

        # Assert
        self.assertEqual(thisset, expected)


if __name__ == "__main__":
    unittest.main()
