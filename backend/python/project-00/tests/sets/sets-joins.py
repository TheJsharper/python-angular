import unittest
class SetsJoinsTestCase(unittest.TestCase):
    def test_set_join(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        result = " ".join(my_set)

        # Assert
        self.assertEqual(set(result.split(" ")), my_set)

    def test_set_join_with_different_separator(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        result = "-".join(my_set)

        # Assert
        self.assertEqual(set(result.split("-")), my_set)

    def test_set_join_with_empty_string_separator(self):
        # Arrange
        my_set = {"Hello", "World"}

        # Act
        result = "".join(my_set)

        # Assert
        self.assertIn(result, {"HelloWorld", "WorldHello"})

    def test_set_join_with_empty_set(self):
        # Arrange
        my_set = set()
        expected = ""

        # Act
        result = " ".join(my_set)

        # Assert
        self.assertEqual(result, expected)

    def test_set_join_with_single_element(self):
        # Arrange
        my_set = {"Hello"}
        expected = "Hello"

        # Act
        result = " ".join(my_set)

        # Assert
        self.assertEqual(result, expected)

    def test_set_join_with_non_string_elements(self):
        # Arrange
        my_set = {"Hello", 123, "World"}

        # Act
        result = " ".join(str(x) for x in my_set)

        # Assert
        self.assertEqual(set(result.split(" ")), {"123", "Hello", "World"})

    def test_set_union_with_mixed_types(self):
        # Arrange
        set1 = {"a", "b", "c"}
        set2 = {1, 2, 3}
        expected = {"a", "b", "c", 1, 2, 3}

        # Act
        set3 = set1.union(set2)

        # Assert
        self.assertEqual(set3, expected)

    def test_set_union_with_pipe_operator(self):
        # Arrange
        set1 = {"a", "b", "c"}
        set2 = {1, 2, 3}
        expected = {"a", "b", "c", 1, 2, 3}

        # Act
        set3 = set1 | set2

        # Assert
        self.assertEqual(set3, expected)

    def test_set_union_with_multiple_sets(self):
        # Arrange
        set1 = {"a", "b", "c"}
        set2 = {1, 2, 3}
        set3 = {"John", "Elena"}
        set4 = {"apple", "bananas", "cherry"}
        expected = {
            "a",
            "b",
            "c",
            1,
            2,
            3,
            "John",
            "Elena",
            "apple",
            "bananas",
            "cherry",
        }

        # Act
        myset = set1.union(set2, set3, set4)

        # Assert
        self.assertEqual(myset, expected)

    def test_set_union_with_multiple_sets_using_pipe(self):
        # Arrange
        set1 = {"a", "b", "c"}
        set2 = {1, 2, 3}
        set3 = {"John", "Elena"}
        set4 = {"apple", "bananas", "cherry"}
        expected = {
            "a",
            "b",
            "c",
            1,
            2,
            3,
            "John",
            "Elena",
            "apple",
            "bananas",
            "cherry",
        }

        # Act
        myset = set1 | set2 | set3 | set4

        # Assert
        self.assertEqual(myset, expected)

    def test_set_union_with_tuple(self):
        # Arrange
        x = {"a", "b", "c"}
        y = (1, 2, 3)
        expected = {"a", "b", "c", 1, 2, 3}

        # Act
        z = x.union(y)

        # Assert
        self.assertEqual(z, expected)

    def test_set_intersection(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"apple"}

        # Act
        set3 = set1.intersection(set2)

        # Assert
        self.assertEqual(set3, expected)

    def test_set_intersection_with_and_operator(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"apple"}

        # Act
        set3 = set1 & set2

        # Assert
        self.assertEqual(set3, expected)

    def test_set_intersection_with_mixed_types_and_bool_int_equivalence(self):
        # Arrange
        set1 = {"apple", 1, "banana", 0, "cherry"}
        set2 = {False, "google", 1, "apple", 2, True}
        expected = {"apple", 0, 1}

        # Act
        set3 = set1.intersection(set2)

        # Assert
        self.assertEqual(set3, expected)

    def test_set_difference(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry"}

        # Act
        set3 = set1.difference(set2)

        # Assert
        self.assertEqual(set3, expected)

    def test_set_difference_with_minus_operator(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry"}

        # Act
        set3 = set1 - set2

        # Assert
        self.assertEqual(set3, expected)

    def test_set_difference_update(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry"}

        # Act
        set1.difference_update(set2)

        # Assert
        self.assertEqual(set1, expected)

    def test_set_difference_update_with_minus_equal_operator(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry"}

        # Act
        set1 -= set2

        # Assert
        self.assertEqual(set1, expected)

    def test_set_symmetric_difference(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry", "google", "microsoft"}

        # Act
        set3 = set1.symmetric_difference(set2)

        # Assert
        self.assertEqual(set3, expected)

    def test_set_symmetric_difference_with_xor_operator(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry", "google", "microsoft"}

        # Act
        set3 = set1 ^ set2

        # Assert
        self.assertEqual(set3, expected)

    def test_set_symmetric_difference_update(self):
        # Arrange
        set1 = {"apple", "banana", "cherry"}
        set2 = {"google", "microsoft", "apple"}
        expected = {"banana", "cherry", "google", "microsoft"}

        # Act
        set1.symmetric_difference_update(set2)

        # Assert
        self.assertEqual(set1, expected)
        
if __name__ == "__main__":
    unittest.main()            