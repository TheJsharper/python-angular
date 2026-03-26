
import unittest


class ListCopyTests(unittest.TestCase):
    def test_list_copy(self):
        # Arrange
        my_list = [1, 2, 3]
        expected = [1, 2, 3]

        # Act
        copied_list = my_list.copy()

        # Assert
        self.assertEqual(copied_list, expected)
        self.assertIsNot(copied_list, my_list)
    def test_list_copy_with_nested_lists(self):
        # Arrange
        my_list = [1, 2, [3, 4]]
        expected = [1, 2, [3, 4]]

        # Act
        copied_list = my_list.copy()

        # Assert
        self.assertEqual(copied_list, expected)
        self.assertIsNot(copied_list, my_list)
        self.assertIs(copied_list[2], my_list[2])  # nested list is the same object
    def test_list_copy_with_nested_lists_and_modification(self):
        # Arrange
        my_list = [1, 2, [3, 4]]
        expected = [1, 2, [3, 4]]

        # Act
        copied_list = my_list.copy()
        copied_list[2][0] = 30

        # Assert
        self.assertEqual(copied_list, [1, 2, [30, 4]])
        self.assertEqual(my_list, [1, 2, [30, 4]])  # original list is also modified
        self.assertIsNot(copied_list, my_list)
        self.assertIs(copied_list[2], my_list[2])  # nested

    def test_list_copy_using_list_constructor(self):
        # Arrange
        thislist = ["apple", "banana", "cherry"]
        expected = ["apple", "banana", "cherry"]

        # Act
        mylist = list(thislist)

        # Assert
        self.assertEqual(mylist, expected)
        self.assertIsNot(mylist, thislist)

    def test_list_copy_using_slice(self):
        # Arrange
        thislist = ["apple", "banana", "cherry"]
        expected = ["apple", "banana", "cherry"]

        # Act
        mylist = thislist[:]

        # Assert
        self.assertEqual(mylist, expected)
        self.assertIsNot(mylist, thislist)
    def test_list_copy_using_copy_module(self):
        import copy

        # Arrange
        thislist = ["apple", "banana", "cherry"]
        expected = ["apple", "banana", "cherry"]

        # Act
        mylist = copy.copy(thislist)

        # Assert
        self.assertEqual(mylist, expected)
        self.assertIsNot(mylist, thislist)


if __name__ == "__main__":
    unittest.main()