"""
Run the full test suite with coverage and print a terminal report.
Also generates an HTML report in tests/coverage_html/.

Usage (from project-03 root):
    python tests/run_coverage.py
"""
import os
import sys
import coverage
import unittest

# Ensure src/ is importable
TESTS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(TESTS_DIR, "../src"))
PROJECT_DIR = os.path.abspath(os.path.join(TESTS_DIR, ".."))
sys.path.insert(0, SRC_DIR)
sys.path.insert(0, TESTS_DIR)

cov = coverage.Coverage(config_file=os.path.join(PROJECT_DIR, ".coveragerc"), source=[SRC_DIR])
cov.start()

loader = unittest.TestLoader()
suite = loader.discover(start_dir=TESTS_DIR, pattern="test_*.py")
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

cov.stop()
cov.save()

print("\n" + "=" * 70)
print("COVERAGE REPORT")
print("=" * 70)
cov.report()

html_dir = os.path.join(TESTS_DIR, "coverage_html")
cov.html_report(directory=html_dir)
print(f"\nHTML report saved to: {html_dir}/index.html")

sys.exit(0 if result.wasSuccessful() else 1)
