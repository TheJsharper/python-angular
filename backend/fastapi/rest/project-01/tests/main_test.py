import unittest
import os


if __name__ == "__main__":
    loader = unittest.defaultTestLoader
    test_dir = os.path.dirname(__file__)
    suite = loader.discover(start_dir=test_dir, pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
