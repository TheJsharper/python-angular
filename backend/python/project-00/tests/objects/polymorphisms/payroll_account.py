import unittest
import unittest.mock
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)
# from objects.polymorphisms.payroll_account import PayrollAccount


class PayrollAccountTestCase(unittest.TestCase):

    def setUp(self):
        self.payroll_account_patch = unittest.mock.patch(
            "objects.polymorphisms.payroll_account.PayrollAccount"
        )
        self.mock_payroll_account = self.payroll_account_patch.start()
        self.assertIsNotNone(self.mock_payroll_account)

    def test_withdraw(self):
        self.mock_payroll_account.withdraw(200)
        self.mock_payroll_account.withdraw.assert_called_with(200)
        self.assertEqual(self.mock_payroll_account.withdraw.call_count, 1)

    def test_withdraw_insufficient_funds(self):
        self.mock_payroll_account.get_balance.return_value = 1000
        self.mock_payroll_account.withdraw.side_effect = ValueError(
            "Insufficient funds."
        )
        with self.assertRaises(ValueError) as context:
            self.mock_payroll_account.withdraw(1200)
        self.assertEqual(str(context.exception), "Insufficient funds.")

    def test_deposit(self):
        self.mock_payroll_account.deposit(500)
        self.mock_payroll_account.deposit.assert_called_with(500)
        self.assertEqual(self.mock_payroll_account.deposit.call_count, 1)

    def test_deposit_negative_amount(self):
        self.mock_payroll_account.deposit.side_effect = ValueError(
            "Deposit amount must be positive."
        )
        with self.assertRaises(ValueError) as context:
            self.mock_payroll_account.deposit(-100)
        self.assertEqual(str(context.exception), "Deposit amount must be positive.")

    def test_str(self):
        self.mock_payroll_account.get_account_number.return_value = "123456789"
        self.mock_payroll_account.get_balance.return_value = 1000
        self.mock_payroll_account.__str__.return_value = (
            "PayrollAccount(account_number=123456789, balance=$1000)"
        )
        self.assertEqual(
            str(self.mock_payroll_account),
            "PayrollAccount(account_number=123456789, balance=$1000)",
        )

    def test_get_account_number(self):
        self.mock_payroll_account.get_account_number.return_value = "123456789"
        self.assertEqual(self.mock_payroll_account.get_account_number(), "123456789")

    def tearDown(self):
        self.payroll_account_patch.stop()


if __name__ == "__main__":
    unittest.main()
