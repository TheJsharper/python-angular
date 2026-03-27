import unittest


class SetsMethodsTestCase(unittest.TestCase):
    def test_set_add(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        my_set.add("Python")

        # Assert
        self.assertIn("Python", my_set)

    def test_set_remove(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        my_set.remove("Hello")

        # Assert
        self.assertNotIn("Hello", my_set)

    def test_set_discard(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        my_set.discard("Hello")

        # Assert
        self.assertNotIn("Hello", my_set)

    def test_set_clear(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        my_set.clear()

        # Assert
        self.assertEqual(len(my_set), 0)

    def test_copy_set(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        copied_set = my_set.copy()

        # Assert
        self.assertEqual(copied_set, my_set)
        self.assertIsNot(copied_set, my_set)

    def test_difference(self):
        # Arrange
        set_a = {"Hello", "World", "Python"}
        set_b = {"World", "Java"}

        # Act
        result = set_a.difference(set_b)

        # Assert
        self.assertEqual(result, {"Hello", "Python"})

    def test_difference_update(self):
        # Arrange
        set_a = {"Hello", "World", "Python"}
        set_b = {"World", "Java"}

        # Act
        set_a.difference_update(set_b)

        # Assert
        self.assertEqual(set_a, {"Hello", "Python"})

    def test_intersection(self):
        # Arrange
        set1 = {"apple", "banana", "cherry", 0, 1}
        set2 = {"google", "microsoft", "apple", 0, 1}
        expected = {"apple", 0, 1}

        # Act
        result = set1.intersection(set2)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(type(result), set)

    def test_intercetion_update(self):
        # Arrange
        set1 = {"apple", "banana", "cherry", 0, 1}
        set2 = {"google", "microsoft", "apple", 0, 1}
        expected = {"apple", 0, 1}

        # Act
        set1.intersection_update(set2)

        # Assert
        self.assertEqual(set1, expected)
        self.assertEqual(type(set1), set)

    def test_isdisjoint(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "amazon"}

        # Act
        result = set1.isdisjoint(set2)

        # Assert
        self.assertTrue(result)

    def test_issubset(self):
        # Arrange
        set1 = {"apple", "banana"}
        set2 = {"apple", "banana", "cherry"}

        # Act
        result = set1.issubset(set2)

        # Assert
        self.assertTrue(result)

    def test_issuperset(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"apple", "banana"}

        # Act
        result = set1.issuperset(set2)

        # Assert
        self.assertTrue(result)

    def test_pop(self):
        # Arrange
        my_set = {"apple", "banana", "cherry"}

        # Act
        popped_element = my_set.pop()

        # Assert
        self.assertNotIn(popped_element, my_set)
        self.assertEqual(len(my_set), 2)

    def test_remove_non_existent_element(self):
        # Arrange
        my_set = {"apple", "banana", "cherry"}

        # Act & Assert
        with self.assertRaises(KeyError):
            my_set.remove("orange")

    def test_symmetric_difference(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry", "google", "microsoft"}

        # Act
        set3 = set1.symmetric_difference(set2)

        # Assert
        self.assertEqual(set3, expected)

    def test_symmetric_difference_update(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry", "google", "microsoft"}

        # Act
        set1.symmetric_difference_update(set2)

        # Assert
        self.assertEqual(set1, expected)

    def test_union(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"apple", "banana", "cherry", "google", "microsoft"}

        # Act
        set3 = set1.union(set2)

        # Assert
        self.assertEqual(set3, expected)
        self.assertEqual(type(set3), set)

    def test_update(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"apple", "banana", "cherry", "google", "microsoft"}

        # Act
        set1.update(set2)

        # Assert
        self.assertEqual(set1, expected)
        self.assertEqual(type(set1), set)


if __name__ == "__main__":
    unittest.main()
