import unittest
import sys
import os
from unittest import mock
import unittest.mock as mock

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)

from objects.oop.bank_account import BankAccount


class TestBankAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("John Doe", "123456789", 1000)

    def test_initialization(self):
        self.assertEqual(self.account.owner, "John Doe")
        self.assertEqual(self.account.account_number, "123456789")
        self.assertEqual(self.account.balance, 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    @mock.patch("builtins.print")
    def test_deposit_print(self, mock_print):
        self.account.deposit(500)
        mock_print.assert_called_with("Deposited $500. New balance: $1500")

    @mock.patch("builtins.print")
    def test_withdraw_print(self, mock_print):
        self.account.withdraw(300)
        mock_print.assert_called_with("Withdrew $300. New balance: $700")

    @mock.patch("builtins.print")
    def test_str_representation(self, mock_print):
        expected_str = (
            "BankAccount(owner=John Doe, account_number=123456789, balance=$1000)"
        )
        self.assertEqual(str(self.account), expected_str)

    @mock.patch("builtins.print")
    def test_get_account_info(self, mock_print):
        expected_info = "Owner: John Doe, Account Number: 123456789, Balance: $1000"
        self.assertEqual(self.account.get_account_info(), expected_info)


if __name__ == "__main__":
    unittest.main()
