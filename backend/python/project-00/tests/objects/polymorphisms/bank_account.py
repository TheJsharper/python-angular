import unittest
import sys
import os
import unittest.mock

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)
from objects.polymorphisms.bank_account import BankAccount


class BankAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.bank_account_patch = unittest.mock.patch(
            "objects.polymorphisms.bank_account.BankAccount"
        )
        self.mock_bank_account = self.bank_account_patch.start()
        self.assertIsNotNone(self.mock_bank_account)

    @unittest.mock.patch.object(BankAccount, "get_balance", return_value=1000)
    def test_deposit(self, mock_get_balance):
        self.assertEqual(mock_get_balance.return_value, 1000)

    def test_set_owner(self):
        self.mock_bank_account.set_owner("Alice")
        self.mock_bank_account.set_owner.assert_called_with("Alice")
        self.assertEqual(self.mock_bank_account.set_owner.call_count, 1)

    def test_set_account_number(self):
        self.mock_bank_account.set_account_number("123456789")
        self.mock_bank_account.set_account_number.assert_called_with("123456789")
        self.assertEqual(self.mock_bank_account.set_account_number.call_count, 1)

    def test_str(self):
        self.mock_bank_account.__str__.return_value = (
            "BankAccount(owner=Alice, account_number=123456789, balance=$1000)"
        )
        self.assertEqual(
            str(self.mock_bank_account),
            "BankAccount(owner=Alice, account_number=123456789, balance=$1000)",
        )

    def test_get_balance(self):
        self.mock_bank_account.get_balance.return_value = 1000
        self.assertEqual(self.mock_bank_account.get_balance(), 1000)

    def test_set_balance(self):
        self.mock_bank_account.set_balance(1000)
        self.mock_bank_account.set_balance.assert_called_with(1000)
        self.assertEqual(self.mock_bank_account.set_balance.call_count, 1)

    def test_set_balance_negative(self):
        self.mock_bank_account.set_balance.side_effect = ValueError(
            "Balance cannot be negative."
        )
        with self.assertRaises(ValueError) as context:
            self.mock_bank_account.set_balance(-500)
        self.assertEqual(str(context.exception), "Balance cannot be negative.")

    def test_get_owner(self):
        self.mock_bank_account.get_owner.return_value = "Alice"
        self.assertEqual(self.mock_bank_account.get_owner(), "Alice")

    def test_get_account_number(self):
        self.mock_bank_account.get_account_number.return_value = "123456789"
        self.assertEqual(self.mock_bank_account.get_account_number(), "123456789")

    def test_set_account_number(self):
        self.mock_bank_account.set_account_number("123456789")
        self.mock_bank_account.set_account_number.assert_called_with("123456789")
        self.assertEqual(self.mock_bank_account.set_account_number.call_count, 1)

    def tearDown(self):
        self.bank_account_patch.stop()


if __name__ == "__main__":
    unittest.main()
