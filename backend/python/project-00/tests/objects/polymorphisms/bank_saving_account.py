import unittest
import sys
import os
import unittest.mock

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)
from objects.polymorphisms.saving_account import SavingAccount


class BankSavingAccountTestCase(unittest.TestCase):
    def test_bank_account(self):

        account = SavingAccount("John Doe", "123456789", 1000)
        self.assertEqual(account.get_owner(), "John Doe")
        self.assertEqual(account.get_balance(), 1000)

    def test_deposit(self):
        account = SavingAccount("John Doe", "123456789", 1000)
        account.deposit(500)
        self.assertEqual(account.get_balance(), 1500)

    def test_deposit_negative_amount(self):
        account = SavingAccount("John Doe", "123456789", 1000)
        with self.assertRaises(ValueError):
            account.deposit(-100)

    @unittest.mock.patch("builtins.print")
    def test_deposit_with_print(self, mock_print):
        account = SavingAccount("John Doe", "123456789", 1000)
        account.deposit(500)
        mock_print.assert_called_with("Deposited $500. New balance: $1500")

    def test_withdraw(self):
        account = SavingAccount("John Doe", "123456789", 1000)
        account.withdraw(300)
        self.assertEqual(account.get_balance(), 700)

    def test_withdraw_insufficient_funds(self):
        account = SavingAccount("John Doe", "123456789", 1000)
        with self.assertRaises(ValueError):
            account.withdraw(1500)

    def test_apply_interest(self):
        account = SavingAccount("John Doe", "123456789", 1000, interest_rate=0.05)
        account.apply_interest()
        self.assertEqual(account.get_balance(), 1050)

    def test_str_representation(self):
        account = SavingAccount("John Doe", "123456789", 1000, interest_rate=0.05)
        expected_str = "SavingAccount(owner=John Doe, account_number=123456789, balance=$1000, interest_rate=0.05)"
        self.assertEqual(str(account), expected_str)

    @unittest.mock.patch("builtins.print")
    def test_deposit_with_print(self, mock_print):
        account = SavingAccount("John Doe", "123456789", 1000)
        account.deposit(500)
        mock_print.assert_called_with("Deposited $500. New balance: $1500")

    @unittest.mock.patch("builtins.print")
    def test_withdraw_with_print(self, mock_print):
        account = SavingAccount("John Doe", "123456789", 1000)
        account.withdraw(300)
        mock_print.assert_called_with("Withdrew $300. New balance: $700")

    @unittest.mock.patch("builtins.print")
    def test_apply_interest_with_print(self, mock_print):
        account = SavingAccount("John Doe", "123456789", 1000, interest_rate=0.05)
        account.apply_interest()
        mock_print.assert_called_with("Applied interest of $50.0. New balance: $1050.0")


if __name__ == "__main__":
    unittest.main()
