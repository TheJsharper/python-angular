import unittest

import sys
import os
import unittest.mock

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)

from libraries.wrap_cowpy import WrapCowpy


class WrapCowpyTestCase(unittest.TestCase):
    def setUp(self):
        from cowpy import cow

        self.cowpy = cow.Cower()
        self.wrapper = WrapCowpy(self.cowpy)

    def test_say(self):
        message = "Hello, World!"
        result = self.wrapper.say(message)
        self.assertIn(message, result)

    @unittest.mock.patch("cowpy.cow.Cower.milk")
    def test_say_with_library_cower_milk(self, mock_milk):
        mock_milk.return_value = "Mocked cow says: Hello!"
        result = self.wrapper.say("Hello!")
        self.assertEqual(result, "Mocked cow says: Hello!")

    def test_say_with_milk(self):
        class MockCowpy:
            def milk(self, message):
                return f"Mocked cow says: {message}"

        wrapper = WrapCowpy(MockCowpy())
        result = wrapper.say("Hello!")
        self.assertEqual(result, "Mocked cow says: Hello!")

    def test_say_with_no_milk_methods(self):
        class MockCowpy:
            pass

        wrapper = WrapCowpy(MockCowpy())
        with self.assertRaises(AttributeError):
            wrapper.say("Hello!")

    def test_say_with_milk_random_cow(self):
        class MockCowpy:
            def milk_random_cow(self, message):
                return f"Mocked random cow says: {message}"

        wrapper = WrapCowpy(MockCowpy())
        result = wrapper.say("Hello!")
        self.assertEqual(result, "Mocked random cow says: Hello!")

    def test_say_with_milk_random_cow_over_milk(self):
        class MockCowpy:
            def milk_random_cow(self, message):
                return f"Mocked random cow says: {message}"

            def milk(self, message):
                return f"Mocked cow says: {message}"

        wrapper = WrapCowpy(MockCowpy())
        result = wrapper.say("Hello!")
        self.assertEqual(result, "Mocked random cow says: Hello!")

    def test_say_with_milk_over_library_cowpy(self):
        class MockCowpy:
            def milk(self, message):
                return f"Mocked cow says: {message}"

        wrapper = WrapCowpy(MockCowpy())
        result = wrapper.say("Hello!")
        self.assertEqual(result, "Mocked cow says: Hello!")

    @unittest.mock.patch("cowpy.cow.Cower.milk_random_cow", create=True)
    def test_say_with_library_cower_milk_random_cow(self, mock_milk_random_cow):
        mock_milk_random_cow.return_value = "Mocked random cow says: Hello!"
        result = self.wrapper.say("Hello!")
        self.assertEqual(result, "Mocked random cow says: Hello!")

    @unittest.mock.patch("cowpy.cow.Cower.milk_random_cow", create=True)
    @unittest.mock.patch("cowpy.cow.Cower.milk")
    def test_say_with_library_cower_milk_random_cow_over_milk(
        self, mock_milk, mock_milk_random_cow
    ):
        mock_milk_random_cow.return_value = "Mocked random cow says: Hello!"
        mock_milk.return_value = "Mocked cow says: Hello!"
        result = self.wrapper.say("Hello!")
        self.assertEqual(result, "Mocked random cow says: Hello!")

    @unittest.mock.patch("cowpy.cow.Cower.milk", create=True)
    def test_say_with_library_cower_milk_over_milk_random_cow(self, mock_milk):
        mock_milk.return_value = "Mocked cow says: Hello!"
        result = self.wrapper.say("Hello!")
        self.assertEqual(result, "Mocked cow says: Hello!")

    @unittest.mock.patch("cowpy.cow.Cower.milk_random_cow", create=True)
    @unittest.mock.patch("cowpy.cow.Cower.milk", create=True)
    def test_say_with_library_cower_milk_over_milk_random_cow(
        self, mock_milk, mock_milk_random_cow
    ):
        mock_milk.return_value = "Mocked cow says: Hello!"
        mock_milk_random_cow.return_value = "Mocked random cow says: Hello!"
        result = self.wrapper.say("Hello!")
        self.assertEqual(result, "Mocked random cow says: Hello!")

    @unittest.mock.patch("cowpy.cow.Cower.milk_random_cow", create=True)
    @unittest.mock.patch("cowpy.cow.Cower.milk", create=True)
    def test_say_with_library_cower_milk_random_cow_over_milk(
        self, mock_milk, mock_milk_random_cow
    ):
        mock_milk.return_value = "Mocked cow says: Hello!"
        mock_milk_random_cow.return_value = "Mocked random cow says: Hello!"
        result = self.wrapper.say("Hello!")
        self.assertEqual(result, "Mocked random cow says: Hello!")

    def tearDown(self):
        self.cowpy = None
        self.wrapper = None


if __name__ == "__main__":
    unittest.main()
