import unittest
class DictsCopyTestCase(unittest.TestCase): 
    def test_dict_copy_with_copy_method(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 30}

        # Act
        copied_dict = my_dict.copy()

        # Assert
        self.assertEqual(copied_dict, expected)
        self.assertIsNot(copied_dict, my_dict)

    def test_dict_copy_with_constructor(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}
        expected = {"name": "Alice", "age": 30}

        # Act
        copied_dict = dict(my_dict)

        # Assert
        self.assertEqual(copied_dict, expected)
        self.assertIsNot(copied_dict, my_dict)

    def test_dict_copy_with_assignment(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act
        copied_dict = my_dict

        # Assert
        self.assertEqual(copied_dict, my_dict)
        self.assertIs(copied_dict, my_dict)

    def test_dict_copy_method_with_argument_raises_type_error(self):
        # Arrange
        my_dict = {"name": "Alice", "age": 30}

        # Act & Assert
        with self.assertRaises(TypeError):
            my_dict.copy({"country": "USA"})

    def test_dict_constructor_with_non_iterable_raises_type_error(self):
        # Arrange
        invalid_source = None

        # Act & Assert
        with self.assertRaises(TypeError):
            dict(invalid_source)

if __name__ == "__main__":
    unittest.main()        