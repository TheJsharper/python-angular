import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(TESTS_DIR, "../src"))
PROJECT_DIR = os.path.abspath(os.path.join(TESTS_DIR, ".."))
sys.path.insert(0, SRC_DIR)
sys.path.insert(0, TESTS_DIR)

from test_health import TestHealth  # noqa: F401
from test_get_users import TestGetUsers  # noqa: F401
from test_get_user_by_id import TestGetUserById  # noqa: F401
from test_post_users import TestPostUsers  # noqa: F401
from test_put_users import TestPutUsers  # noqa: F401
from test_patch_users import TestPatchUsers  # noqa: F401
from test_delete_users import TestDeleteUsers  # noqa: F401

if __name__ == "__main__":
    import coverage

    cov = coverage.Coverage(
        config_file=os.path.join(PROJECT_DIR, ".coveragerc"),
        source=[SRC_DIR],
    )
    cov.start()

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromNames([
        "test_health",
        "test_get_users",
        "test_get_user_by_id",
        "test_post_users",
        "test_put_users",
        "test_patch_users",
        "test_delete_users",
    ])
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
