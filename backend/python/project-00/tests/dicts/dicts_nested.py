import unittest


class DictsNestedTestCase(unittest.TestCase):
    def test_dict_nested_access(self):
        # Arrange
        my_dict = {"person": {"name": "Alice", "age": 30}}

        # Act
        name = my_dict["person"]["name"]
        age = my_dict["person"]["age"]

        # Assert
        self.assertEqual(name, "Alice")
        self.assertEqual(age, 30)

    def test_dict_nested_update(self):
        # Arrange
        my_dict = {"person": {"name": "Alice", "age": 30}}
        expected = {"person": {"name": "Alice", "age": 31}}

        # Act
        my_dict["person"]["age"] += 1

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_nested_add_new_key(self):
        # Arrange
        my_dict = {"person": {"name": "Alice", "age": 30}}
        expected = {"person": {"name": "Alice", "age": 30, "country": "USA"}}

        # Act
        my_dict["person"]["country"] = "USA"

        # Assert
        self.assertEqual(my_dict, expected)

    def test_dict_nested_with_missing_key_raises_key_error(self):
        # Arrange
        my_dict = {"person": {"name": "Alice", "age": 30}}

        # Act & Assert
        with self.assertRaises(KeyError):
            _ = my_dict["person"]["country"]

    def test_dict_nested_three_dictionaries(self):
        # Arrange & Act
        myfamily = {
            "child1": {"name": "Emil", "year": 2004},
            "child2": {"name": "Tobias", "year": 2007},
            "child3": {"name": "Linus", "year": 2011},
        }

        # Assert
        self.assertEqual(myfamily["child1"], {"name": "Emil", "year": 2004})
        self.assertEqual(myfamily["child2"], {"name": "Tobias", "year": 2007})
        self.assertEqual(myfamily["child3"], {"name": "Linus", "year": 2011})
        self.assertEqual(myfamily["child1"]["name"], "Emil")
        self.assertEqual(myfamily["child2"]["year"], 2007)
        self.assertEqual(len(myfamily), 3)

    def test_dict_nested_with_separate_child_dictionaries(self):
        # Arrange
        child1 = {"name": "Emil", "year": 2004}
        child2 = {"name": "Tobias", "year": 2007}
        child3 = {"name": "Linus", "year": 2011}

        # Act
        myfamily = {
            "child1": child1,
            "child2": child2,
            "child3": child3,
        }

        # Assert
        self.assertEqual(myfamily["child1"], child1)
        self.assertEqual(myfamily["child2"], child2)
        self.assertEqual(myfamily["child3"], child3)
        self.assertEqual(myfamily["child1"]["name"], "Emil")
        self.assertEqual(myfamily["child3"]["year"], 2011)
        self.assertEqual(len(myfamily), 3)

    def test_dict_nested_access_from_outer_to_inner_dictionary(self):
        # Arrange
        myfamily = {
            "child1": {"name": "Emil", "year": 2004},
            "child2": {"name": "Tobias", "year": 2007},
            "child3": {"name": "Linus", "year": 2011},
        }

        # Act
        child2_name = myfamily["child2"]["name"]

        # Assert
        self.assertEqual(child2_name, "Tobias")

    def test_dict_nested_loop_with_items_method(self):
        # Arrange
        myfamily = {
            "child1": {"name": "Emil", "year": 2004},
            "child2": {"name": "Tobias", "year": 2007},
            "child3": {"name": "Linus", "year": 2011},
        }

        # Act
        output = []
        for child_key, child_obj in myfamily.items():
            output.append(child_key)
            for inner_key in child_obj:
                output.append(f"{inner_key}: {child_obj[inner_key]}")

        # Assert
        expected_output = [
            "child1",
            "name: Emil",
            "year: 2004",
            "child2",
            "name: Tobias",
            "year: 2007",
            "child3",
            "name: Linus",
            "year: 2011",
        ]
        self.assertEqual(output, expected_output)

    def test_dict_nested_update_child_with_update_method(self):
        # Arrange
        myfamily = {
            "child1": {"name": "Emil", "year": 2004},
            "child2": {"name": "Tobias", "year": 2007},
            "child3": {"name": "Linus", "year": 2011},
        }

        # Act
        myfamily["child2"].update({"year": 2008})

        # Assert
        self.assertEqual(myfamily["child2"]["name"], "Tobias")
        self.assertEqual(myfamily["child2"]["year"], 2008)

    def test_dict_nested_update_with_invalid_set_input_raises_value_error(self):
        # Arrange
        myfamily = {
            "child1": {"name": "Emil", "year": 2004},
            "child2": {"name": "Tobias", "year": 2007},
            "child3": {"name": "Linus", "year": 2011},
        }

        # Act & Assert
        with self.assertRaises(ValueError):
            myfamily["child1"].update({"invalid", "pair"})

    def test_dict_nested_missing_outer_key_raises_key_error(self):
        # Arrange
        myfamily = {
            "child1": {"name": "Emil", "year": 2004},
            "child2": {"name": "Tobias", "year": 2007},
            "child3": {"name": "Linus", "year": 2011},
        }

        # Act & Assert
        with self.assertRaises(KeyError):
            _ = myfamily["child4"]["name"]


if __name__ == "__main__":
    unittest.main()
