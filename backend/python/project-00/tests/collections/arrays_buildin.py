import unittest
from unittest import mock


class ArraysBuiltinTestCase(unittest.TestCase):
    def test_array_builtin_with_integers(self):
        # Arrange
        import array

        expected = [1, 2, 3, 4]

        # Act
        arr = array.array("i", expected)
        result = list(arr)

        # Assert
        self.assertEqual(result, expected)

    def test_array_builtin_with_floats(self):
        # Arrange
        import array

        expected = [1.0, 2.0, 3.0, 4.0]

        # Act
        arr = array.array("f", expected)
        result = list(arr)

        # Assert
        self.assertEqual(result, expected)

    def test_array_builtin_with_empty_array(self):
        # Arrange
        import array

        expected = []

        # Act
        arr = array.array("i")
        result = list(arr)

        # Assert
        self.assertEqual(result, expected)

    def test_array_builtin_with_different_typecode(self):
        # Arrange
        import array

        expected = [1, 2, 3, 4]

        # Act
        arr = array.array("l", expected)  # 'l' for long integers
        result = list(arr)

        # Assert
        self.assertEqual(result, expected)

    def test_list_builtin_cars(self):
        # Arrange & Act
        cars = ["Ford", "Volvo", "BMW"]

        # Assert
        self.assertEqual(cars, ["Ford", "Volvo", "BMW"])
        self.assertEqual(len(cars), 3)

    def test_get_first_array_item(self):
        # Arrange
        cars = ["Ford", "Volvo", "BMW"]

        # Act
        first_item = cars[0]

        # Assert
        self.assertEqual(first_item, "Ford")

    def test_modify_first_array_item(self):
        # Arrange
        cars = ["Ford", "Volvo", "BMW"]

        # Act
        cars[0] = "Toyota"

        # Assert
        self.assertEqual(cars[0], "Toyota")
        self.assertEqual(cars, ["Toyota", "Volvo", "BMW"])

    def test_print_each_item_in_cars_array(self):
        # Arrange
        cars = ["Ford", "Volvo", "BMW"]

        # Act & Assert
        with mock.patch("builtins.print") as mock_print:
            for item in cars:
                print(item)

            expected_calls = [
                mock.call("Ford"),
                mock.call("Volvo"),
                mock.call("BMW"),
            ]
            mock_print.assert_has_calls(expected_calls)
            self.assertEqual(mock_print.call_count, 3)

    def test_append_item_to_cars_array(self):
        # Arrange
        cars = ["Ford", "Volvo", "BMW"]

        # Act
        cars.append("Honda")

        # Assert
        self.assertEqual(cars[-1], "Honda")
        self.assertEqual(cars, ["Ford", "Volvo", "BMW", "Honda"])

    def test_pop_item_from_cars_array_by_index(self):
        # Arrange
        cars = ["Ford", "Volvo", "BMW"]

        # Act
        removed = cars.pop(1)

        # Assert
        self.assertEqual(removed, "Volvo")
        self.assertEqual(cars, ["Ford", "BMW"])

    def test_remove_item_from_cars_array_by_value(self):
        # Arrange
        cars = ["Ford", "Volvo", "BMW"]

        # Act
        cars.remove("Volvo")

        # Assert
        self.assertNotIn("Volvo", cars)
        self.assertEqual(cars, ["Ford", "BMW"])

    def test_list_builtin_methods_overview(self):
        # Arrange
        cars = ["Ford", "Volvo", "BMW"]

        # Act
        cars.append("Honda")
        cars.insert(1, "Toyota")
        cars.remove("Volvo")
        popped = cars.pop()
        index_bmw = cars.index("BMW")
        count_ford = cars.count("Ford")

        # Assert
        self.assertEqual(cars, ["Ford", "Toyota", "BMW"])
        self.assertEqual(popped, "Honda")
        self.assertEqual(index_bmw, 2)
        self.assertEqual(count_ford, 1)

    def test_list_clear(self):
        """
        clear()	Removes all the elements from the list
        """
        fruits = ["apple", "banana", "cherry"]
        fruits.clear()

        # Assert that the list is empty
        self.assertEqual(len(fruits), 0)
        self.assertEqual(fruits, [])

    def test_list_copy(self):
        """
        copy()	Returns a copy of the list
        """
        fruits = ["apple", "banana", "cherry"]
        fruits_copy = fruits.copy()

        # Assert that the lists are equal in content
        self.assertEqual(fruits, fruits_copy)
        # Assert that they are different objects (not the same reference)
        self.assertIsNot(fruits, fruits_copy)

        # Modify the original and ensure the copy remains unchanged
        fruits.append("orange")
        self.assertIn("orange", fruits)
        self.assertNotIn("orange", fruits_copy)

    def test_list_count(self):
        """
        count()	Returns the number of elements with the specified value
        """
        fruits = ["apple", "cherry", "banana", "cherry"]
        
        # Act & Assert
        self.assertEqual(fruits.count("cherry"), 2)
        self.assertEqual(fruits.count("apple"), 1)
        self.assertEqual(fruits.count("orange"), 0)

    def test_list_extend(self):
        """
        extend()	Add the elements of a list (or any iterable), to the end of the current list
        """
        fruits = ["apple", "banana", "cherry"]
        cars = ["Ford", "BMW", "Volvo"]
        
        # Act: Extend with a list
        fruits.extend(cars)
        
        # Assert: List is updated
        self.assertEqual(fruits, ["apple", "banana", "cherry", "Ford", "BMW", "Volvo"])
        
        # Act: Extend with a tuple (any iterable)
        points = (1, 2)
        fruits.extend(points)
        
        # Assert: List is updated again
        self.assertEqual(fruits[-2:], [1, 2])

    def test_list_index(self):
        """
        index()	Returns the index of the first element with the specified value
        """
        fruits = ["apple", "banana", "cherry", "orange", "cherry"]

        # Act & Assert: Find first occurrence
        self.assertEqual(fruits.index("cherry"), 2)
        self.assertEqual(fruits.index("banana"), 1)

        # Act & Assert: Throws ValueError if not found
        with self.assertRaises(ValueError):
            fruits.index("blueberry")

    def test_list_insert(self):
        """
        insert()	Adds an element at the specified position
        """
        fruits = ["apple", "banana", "cherry"]
        
        # Act: Insert "orange" at index 1
        fruits.insert(1, "orange")
        
        # Assert: List is updated correctly
        self.assertEqual(fruits, ["apple", "orange", "banana", "cherry"])
        self.assertEqual(fruits[1], "orange")

    def test_list_pop(self):
        """
        pop()	Removes the element at the specified position
        """
        fruits = ["apple", "banana", "cherry"]

        # Act: Pop element at index 1
        popped_element = fruits.pop(1)

        # Assert: Correct element returned and list updated
        self.assertEqual(popped_element, "banana")
        self.assertEqual(fruits, ["apple", "cherry"])

        # Act: Pop with no index (defaults to last element)
        last_element = fruits.pop()
        self.assertEqual(last_element, "cherry")
        self.assertEqual(fruits, ["apple"])

    def test_list_remove(self):
        """
        remove()	Removes the first item with the specified value
        """
        fruits = ["apple", "banana", "cherry", "banana"]

        # Act: Remove the first occurrence of "banana"
        fruits.remove("banana")

        # Assert: List is updated correctly (first "banana" is gone, second remains)
        self.assertEqual(fruits, ["apple", "cherry", "banana"])

        # Act & Assert: Throws ValueError if item not in list
        with self.assertRaises(ValueError):
            fruits.remove("orange")

    def test_list_reverse(self):
        """
        reverse()	Reverses the order of the list
        """
        fruits = ["apple", "banana", "cherry"]

        # Act: Reverse the list in place
        fruits.reverse()

        # Assert: List is reversed correctly
        self.assertEqual(fruits, ["cherry", "banana", "apple"])

    def test_list_sort(self):
        """
        sort()	Sorts the list
        """
        cars = ["Ford", "BMW", "Volvo"]

        # Act: Sort alphabetically (ascending by default)
        cars.sort()
        self.assertEqual(cars, ["BMW", "Ford", "Volvo"])

        # Act: Sort in descending order
        cars.sort(reverse=True)
        self.assertEqual(cars, ["Volvo", "Ford", "BMW"])

        # Act: Sort with a custom key function (by length)
        fruits = ["apple", "cherry", "banana", "kiwi"]
        fruits.sort(key=len)
        self.assertEqual(fruits, ["kiwi", "apple", "cherry", "banana"])


if __name__ == "__main__":
    unittest.main()
