import unittest
class ListJoinTests(unittest.TestCase):
    def test_list_join(self):
        # Arrange
        my_list = ["Hello", "World"]
        expected = "Hello World"

        # Act
        result = " ".join(my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_list_join_with_different_separator(self):
        # Arrange
        my_list = ["Hello", "World"]
        expected = "Hello-World"

        # Act
        result = "-".join(my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_list_join_with_empty_string_separator(self):
        # Arrange
        my_list = ["Hello", "World"]
        expected = "HelloWorld"

        # Act
        result = "".join(my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_list_join_with_empty_list(self):
        # Arrange
        my_list = []
        expected = ""

        # Act
        result = " ".join(my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_list_join_with_single_element(self):
        # Arrange
        my_list = ["Hello"]
        expected = "Hello"

        # Act
        result = " ".join(my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_list_join_with_non_string_elements(self):
        # Arrange
        my_list = ["Hello", 123, "World"]
        expected = "Hello 123 World"

        # Act
        result = " ".join(str(x) for x in my_list)

        # Assert
        self.assertEqual(result, expected)
    def test_list_join_with_non_string_elements_and_different_separator(self):
        # Arrange
        my_list = ["Hello", 123, "World"]
        expected = "Hello-123-World"

        # Act
        result = "-".join(str(x) for x in my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_list_join_with_non_string_elements_and_empty_string_separator(self):
        # Arrange
        my_list = ["Hello", 123, "World"]
        expected = "Hello123World"

        # Act
        result = "".join(str(x) for x in my_list)

        # Assert
        self.assertEqual(result, expected)  
    def test_list_join_with_non_string_elements_and_empty_list(self):
        # Arrange
        my_list = []
        expected = ""

        # Act
        result = " ".join(str(x) for x in my_list)

        # Assert
        self.assertEqual(result, expected)

    def test_list_concat_with_plus_operator(self):
        # Arrange
        list1 = ["a", "b", "c"]
        list2 = [1, 2, 3]
        expected = ["a", "b", "c", 1, 2, 3]

        # Act
        list3 = list1 + list2

        # Assert
        self.assertEqual(list3, expected)

    def test_list_concat_with_append_in_loop(self):
        # Arrange
        list1 = ["a", "b", "c"]
        list2 = [1, 2, 3]
        expected = ["a", "b", "c", 1, 2, 3]

        # Act
        for x in list2:
            list1.append(x)

        # Assert
        self.assertEqual(list1, expected)

    def test_list_concat_with_extend(self):
        # Arrange
        list1 = ["a", "b", "c"]
        list2 = [1, 2, 3]
        expected = ["a", "b", "c", 1, 2, 3]

        # Act
        list1.extend(list2)

        # Assert
        self.assertEqual(list1, expected)
                        


if __name__ == "__main__":
    unittest.main()        