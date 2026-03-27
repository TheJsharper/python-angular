import unittest
from unittest import mock


class FncsGeneratorsTestCase(unittest.TestCase):
    def test_fncs_generators_with_simple_generator(self):
        # Arrange
        def simple_generator():
            yield 1
            yield 2
            yield 3

        expected = [1, 2, 3]

        # Act
        result = list(simple_generator())

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_generators_with_generator_expression(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5]
        expected = [1, 4, 9, 16, 25]

        # Act
        result = [x**2 for x in numbers]

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_generators_with_infinite_generator(self):
        # Arrange
        def infinite_generator():
            n = 0
            while True:
                yield n
                n += 1

        expected = [0, 1, 2, 3, 4]

        # Act
        result = []
        for i in infinite_generator():
            if i >= len(expected):
                break
            result.append(i)

        # Assert
        self.assertEqual(result, expected)

    def test_fncs_generators_count_up_to(self):
        # Arrange
        def count_up_to(n):
            count = 1
            while count <= n:
                yield count
                count += 1

        # Act
        result = list(count_up_to(5))

        # Assert
        self.assertEqual(result, [1, 2, 3, 4, 5])

        # Act & Assert - equivalent to: for num in count_up_to(5): print(num)
        with mock.patch("builtins.print") as mock_print:
            for num in count_up_to(5):
                print(num)

            expected_calls = [
                mock.call(1),
                mock.call(2),
                mock.call(3),
                mock.call(4),
                mock.call(5),
            ]
            mock_print.assert_has_calls(expected_calls)
            self.assertEqual(mock_print.call_count, 5)

    def test_fncs_generators_large_sequence_with_next(self):
        # Arrange
        def large_sequence(n):
            for i in range(n):
                yield i

        # This does not create one million numbers in memory at once.
        gen = large_sequence(1000000)

        # Act
        first = next(gen)
        second = next(gen)
        third = next(gen)

        # Assert
        self.assertEqual(first, 0)
        self.assertEqual(second, 1)
        self.assertEqual(third, 2)

    def test_fncs_generators_raises_stop_iteration_when_exhausted(self):
        # Arrange
        def simple_gen():
            yield 1
            yield 2

        gen = simple_gen()

        # Act
        first = next(gen)
        second = next(gen)

        # Assert
        self.assertEqual(first, 1)
        self.assertEqual(second, 2)
        with self.assertRaises(StopIteration):
            next(gen)


if __name__ == "__main__":
    unittest.main()
