import unittest
import unittest.mock as mock
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)
from fncs import fncs_hofs


class FncsHofsTestCase(unittest.TestCase):
    @mock.patch("builtins.print")
    def test_fncs_hofs_with_map(self, mock_print):
        fncs_hofs.require_auth(lambda user: print(f"Access granted to {user}"))(
            "authenticated_user"
        )
        mock_print.assert_called_once_with("Access granted to authenticated_user")

    def test_require_auth_raises_exception_for_unauthenticated_user(self):
        protected_fn = fncs_hofs.require_auth(
            lambda user: print(f"Access granted to {user}")
        )

        with self.assertRaises(Exception) as context:
            protected_fn("unauthenticated_user")

        self.assertEqual(
            str(context.exception),
            "User must be authenticated to access this function.",
        )

    @mock.patch("builtins.print")
    def test_fncs_hofs_with_filter(self, mock_print):
        users = ["authenticated_user", "unauthenticated_user", "authenticated_user2"]
        authenticated_users = filter(
            lambda user: user.startswith("authenticated"), users
        )
        for user in authenticated_users:
            print(f"Authenticated user: {user}")
        expected_calls = [
            mock.call("Authenticated user: authenticated_user"),
            mock.call("Authenticated user: authenticated_user2"),
        ]
        mock_print.assert_has_calls(expected_calls)
        self.assertEqual(mock_print.call_count, 2)

    @mock.patch("builtins.print")
    def test_fncs_hofs_with_reduce(self, mock_print):
        fncs_hofs.require_auth(lambda user: print(f"Access granted to {user}"))(
            "authenticated_user"
        )
        from functools import reduce

        numbers = [1, 2, 3, 4]
        total = reduce(lambda x, y: x + y, numbers)
        print(f"Total: {total}")
        expected_calls = [
            mock.call("Access granted to authenticated_user"),
            mock.call("Total: 10"),
        ]
        mock_print.assert_has_calls(expected_calls)
        self.assertEqual(mock_print.call_count, 2)


if __name__ == "__main__":
    unittest.main()
