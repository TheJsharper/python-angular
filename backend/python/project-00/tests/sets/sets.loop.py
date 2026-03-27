import unittest


class SetsLoopTestCase(unittest.TestCase):
    def test_loop_over_set_items(self):
        # Arrange
        my_set = {1, 2, 3}
        expected = [1, 2, 3]

        # Act
        result = []
        for item in my_set:
            result.append(item)

        # Assert
        self.assertCountEqual(result, expected)  # order does not matter in sets

    def test_loop_over_empty_set(self):
        # Arrange
        my_set = set()
        expected = []

        # Act
        result = []
        for item in my_set:
            result.append(item)

        # Assert
        self.assertCountEqual(result, expected)  # order does not matter in sets
    def test_loop_over_set_strings(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        expected = ["apple", "banana", "cherry"]

        # Act
        result = []
        for x in thisset:
            result.append(x)

        # Assert
        self.assertCountEqual(result, expected)  # order does not matter in sets
    def test_loop_over_set_with_enumerate(self):
        # Arrange
        my_set = {10, 20, 30}
        expected = [(0, 10), (1, 20), (2, 30)]

        # Act
        result = []
        for index, item in enumerate(my_set):
            result.append((index, item))

        # Assert
        self.assertCountEqual(result, expected)  # order does not matter in sets


    def test_loop_over_set_by_index(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        expected = ["apple", "banana", "cherry"]

        # Act
        result = []
        for i in range(len(thisset)):
            result.append(list(thisset)[i])  # convert set to list for indexing

        # Assert
        self.assertCountEqual(result, expected)  # order does not matter in sets

    def test_loop_over_set_with_while(self):
        # Arrange
        thisset = {"apple", "banana", "cherry"}
        expected = ["apple", "banana", "cherry"]
        result = []
        i = 0

        # Act
        while i < len(thisset):
            result.append(list(thisset)[i])  # convert set to list for indexing
            i = i + 1   
            # Assert    
            # order does not matter in sets, so we use assertCountEqual
        self.assertCountEqual(result, expected) 
    def test_loop_over_set_with_enumerate_and_condition(self):
        # Arrange
        my_set = {10, 20, 30}
        expected = [(0, 10), (1, 20)]

        # Act
        result = []
        for index, item in enumerate(my_set):
            if item < 30:
                result.append((index, item))
        self.assertCountEqual(result, expected)  # order does not matter in sets
    def test_loop_over_set_with_enumerate_and_condition_and_different_length(self):
        # Arrange
        my_set = {10, 20, 30}
        expected = [(0, 10), (1, 20)]

        # Act
        result = []
        for index, item in enumerate(my_set):
            if item < 30:
                result.append((index, item))
        self.assertCountEqual(result, expected)  # order does not matter in sets

    def test_set_comprehension_with_filter(self):
        # Arrange
        numbers = {1, 2, 3, 4, 5, 6}
        expected = {2, 4, 6}

        # Act
        result = {x for x in numbers if x % 2 == 0}

        # Assert
        self.assertEqual(result, expected)

    def test_set_comprehension_with_transformation(self):
        # Arrange
        numbers = {1, 2, 3, 4}
        expected = {1, 4, 9, 16}

        # Act
        result = {x * x for x in numbers}

        # Assert
        self.assertEqual(result, expected)
                                 
if __name__ == "__main__":
    unittest.main()