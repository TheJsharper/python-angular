import unittest


class SetsFrozenSetTestCase(unittest.TestCase):
    def test_frozenset_creation(self):
        # Arrange
        my_frozenset = frozenset([1, 2, 3])
        expected = frozenset({1, 2, 3})

        # Act
        result = my_frozenset

        # Assert
        self.assertEqual(result, expected)

    def test_frozenset_immutable(self):
        # Arrange
        my_frozenset = frozenset([1, 2, 3])

        # Act & Assert
        with self.assertRaises(AttributeError):
            my_frozenset.add(
                4
            )  # AttributeError: 'frozenset' object has no attribute 'add'
            my_frozenset.remove(
                1
            )  # AttributeError: 'frozenset' object has no attribute 'remove'
            my_frozenset.clear()  # AttributeError: 'frozenset' object has no attribute 'clear'
            my_frozenset.update(
                [4, 5, 6]
            )  # AttributeError: 'frozenset' object has no attribute 'update'
            my_frozenset.discard(
                2
            )  # AttributeError: 'frozenset' object has no attribute 'discard'
            my_frozenset.pop()  # AttributeError: 'frozenset' object has no attribute 'pop'
            my_frozenset.intersection_update(
                {2, 3, 4}
            )  # AttributeError: 'frozenset' object has no attribute 'intersection_update'
            my_frozenset.difference_update(
                {1, 2}
            )  # AttributeError: 'frozenset' object has no attribute 'difference_update'
            my_frozenset.symmetric_difference_update(
                {1, 3}
            )  # AttributeError: 'frozenset' object has no attribute 'symmetric_difference_update'

    def test_frozenset_creation_with_fruits_and_type(self):
        # Arrange
        expected = frozenset({"apple", "banana", "cherry"})

        # Act
        x = frozenset({"apple", "banana", "cherry"})

        # Assert
        self.assertEqual(x, expected)
        self.assertEqual(type(x), frozenset)

    def test_frozenset_copy(self):
        # Arrange
        original = frozenset({"apple", "banana", "cherry"})

        # Act
        copied = original.copy()

        # Assert
        self.assertEqual(copied, original)
        self.assertIs(copied, original)

    def test_difference_update_with_frozenset(self):
        # Arrange
        x = frozenset({"apple", "banana", "cherry"})
        y = frozenset({"google", "microsoft", "apple"})
        expected = frozenset({"banana", "cherry"})

        # Act
        result = x.difference(y)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(type(result), frozenset)

    def test_frozenset_difference(self):
        # Arrange
        x = frozenset({"apple", "banana", "cherry"})
        y = frozenset({"google", "microsoft", "apple"})
        expected = frozenset({"banana", "cherry"})

        # Act
        result = x.difference(y)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(type(result), frozenset)

    def test_frozenset_discard(self):
        # Arrange
        x = {"apple", "banana", "cherry"}
        expected = {"apple", "cherry"}

        # Act
        x.discard("banana")

        # Assert
        self.assertEqual(x, expected)

    def test_frozenset_intersection(self):
        # Arrange
        x = frozenset({"apple", "banana", "cherry"})
        y = frozenset({"google", "microsoft", "apple"})
        expected = frozenset({"apple"})

        # Act
        result = x.intersection(y)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(type(result), frozenset)

    def test_frozenset_isdisjoint(self):
        # Arrange
        x = frozenset({"apple", "banana", "cherry"})
        y = frozenset({"google", "microsoft", "apple"})
        z = frozenset({"orange", "kiwi"})

        # Act & Assert
        self.assertFalse(x.isdisjoint(y))
        self.assertTrue(x.isdisjoint(z))

    def test_frozenset_issubset(self):
        # Arrange
        x = frozenset({"apple", "banana"})
        y = frozenset({"apple", "banana", "cherry"})
        z = frozenset({"apple", "banana"})

        # Act & Assert
        self.assertTrue(x.issubset(y))
        self.assertTrue(x <= y)
        self.assertTrue(x < y)
        self.assertTrue(x.issubset(z))
        self.assertTrue(x <= z)
        self.assertFalse(x < z)

    def test_frozenset_issuperset(self):
        # Arrange
        x = frozenset({"apple", "banana", "cherry"})
        y = frozenset({"apple", "banana"})
        z = frozenset({"apple", "banana", "cherry"})

        # Act & Assert
        self.assertTrue(x.issuperset(y))
        self.assertTrue(x >= y)
        self.assertTrue(x > y)
        self.assertTrue(x.issuperset(z))
        self.assertTrue(x >= z)
        self.assertFalse(x > z)

    def test_frozenset_symmetric_difference(self):
        # Arrange
        x = frozenset({"apple", "banana", "cherry"})
        y = frozenset({"google", "microsoft", "apple"})
        expected = frozenset({"banana", "cherry", "google", "microsoft"})

        # Act
        result = x.symmetric_difference(y)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(type(result), frozenset)

    def test_frozenset_union(self):
        # Arrange
        x = frozenset({"apple", "banana", "cherry"})
        y = frozenset({"google", "microsoft", "apple"})
        expected = frozenset({"apple", "banana", "cherry", "google", "microsoft"})

        # Act
        result = x.union(y)

        # Assert
        self.assertEqual(result, expected)
        self.assertEqual(type(result), frozenset)


if __name__ == "__main__":
    unittest.main()
