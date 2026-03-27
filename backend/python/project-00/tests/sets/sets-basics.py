import unittest


class SetsBasicsTestCase(unittest.TestCase):
    def test_set_length(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = 3

        # Act
        length = len(my_set)

        # Assert
        self.assertEqual(length, expected)

    def test_set_contains(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = True

        # Act
        contains = 2 in my_set

        # Assert
        self.assertEqual(contains, expected)

    def test_set_not_contains(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = True

        # Act
        not_contains = 4 not in my_set

        # Assert
        self.assertEqual(not_contains, expected)

    def test_set_add(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = {1, 2, 3, 4}

        # Act
        my_set.add(4)

        # Assert
        self.assertEqual(my_set, expected)

    def test_set_creation_with_fruits(self):
        # Arrange
        expected = {"apple", "banana", "cherry"}

        # Act
        thisset = {"apple", "banana", "cherry"}

        # Assert
        self.assertEqual(thisset, expected)

    def test_set_creation_with_fruits_and_duplicates(self):
        # Arrange
        expected = {"apple", "banana", "cherry"}

        # Act
        thisset = {"apple", "banana", "cherry", "apple"}

        # Assert
        self.assertEqual(thisset, expected)

    def test_set_creation_with_fruits_and_duplicates_and_different_length(self):
        # Arrange
        expected = {"apple", "banana", "cherry"}

        # Act
        thisset = {"apple", "banana", "cherry", "apple"}

        # Assert
        self.assertEqual(thisset, expected)

    def test_set_creation_with_fruits_and_duplicates_and_different_length_2(self):
        # Arrange
        expected = {"apple", "banana", "cherry"}

        # Act
        thisset = {"apple", "banana", "cherry", "apple"}

        # Assert
        self.assertEqual(thisset, expected)

    def test_set_properties_unordered_unchangeable_and_no_duplicates(self):
        # Arrange
        thisset = {"apple", "banana", "cherry", "apple"}

        # Assert: no duplicates
        self.assertEqual(len(thisset), 3)

        # Assert: unordered (compare as set, not by position)
        self.assertEqual(thisset, {"banana", "cherry", "apple"})

        # Assert: items are unchangeable
        with self.assertRaises(TypeError):
            thisset[0] = "orange"

    def test_set_is_unordered(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}

        # Assert: same members are equal regardless of literal order
        self.assertEqual(thisset, {"cherry", "apple", "banana"})

        # Assert: no defined positional order (cannot index by position)
        with self.assertRaises(TypeError):
            _ = thisset[0]

    def test_set_items_are_unchangeable(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        expected = {"apple", "banana", "cherry"}

        # Act & Assert: cannot change an item directly
        with self.assertRaises(TypeError):
            thisset[1] = "orange"

        # Assert: original set remains unchanged
        self.assertEqual(thisset, expected)

    def test_set_duplicates_not_allowed(self):
        # Arrange
        thisset = {"apple", "banana", "cherry", "apple", "banana"}
        expected = {"apple", "banana", "cherry"}

        # Assert
        self.assertEqual(thisset, expected)
        self.assertEqual(len(thisset), 3)

    def test_true_and_one_are_considered_same_value(self):
        # Arrange
        thisset = {"apple", "banana", "cherry", True, 1, 2}

        # Assert: True and 1 are the same set element
        self.assertEqual(len(thisset), 5)
        self.assertIn(True, thisset)
        self.assertIn(1, thisset)
        self.assertEqual(sum(1 for x in thisset if x is True or x == 1), 1)

    def test_false_and_zero_are_considered_same_value(self):
        # Arrange
        thisset = {"apple", "banana", "cherry", False, True, 0}

        # Assert: False and 0 are the same set element
        self.assertEqual(len(thisset), 5)
        self.assertIn(False, thisset)
        self.assertIn(0, thisset)
        self.assertEqual(sum(1 for x in thisset if x is False or x == 0), 1)

    def test_get_number_of_items_in_set(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        expected = 3

        # Act
        result = len(thisset)

        # Assert
        self.assertEqual(result, expected)

    def test_set_data_types_string_int_boolean(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {1, 5, 7, 9, 3}
        set3 = {True, False, False}

        # Assert
        self.assertTrue(all(isinstance(x, str) for x in set1))
        self.assertTrue(all(isinstance(x, int) for x in set2))
        self.assertTrue(all(isinstance(x, bool) for x in set3))
        self.assertEqual(len(set3), 2)

    def test_set_with_mixed_strings_integers_booleans(self):
        # Arrange
        set1 = {"abc", 34, True, 40, "male"}

        # Assert
        self.assertIn("abc", set1)
        self.assertIn("male", set1)
        self.assertIn(34, set1)
        self.assertIn(40, set1)
        self.assertIn(True, set1)
        self.assertEqual(len(set1), 5)

    def test_set_type(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}

        # Assert
        self.assertEqual(type(thisset), set)

    def test_set_constructor_with_tuple(self):
        # Arrange
        expected = {"apple", "banana", "cherry"}

        # Act
        thisset = set(("apple", "banana", "cherry"))

        # Assert
        self.assertEqual(thisset, expected)
        self.assertEqual(type(thisset), set)

    def test_set_core_properties(self):
        # Arrange
        thisset = {"apple", "banana", "cherry", "apple"}

        # Assert: no duplicate members
        self.assertEqual(thisset, {"apple", "banana", "cherry"})
        self.assertEqual(len(thisset), 3)

        # Assert: unordered (membership-based equality, not position-based)
        self.assertEqual(thisset, {"banana", "cherry", "apple"})

        # Assert: unindexed / items cannot be accessed by position
        with self.assertRaises(TypeError):
            _ = thisset[0]
        


if __name__ == "__main__":
    unittest.main()
