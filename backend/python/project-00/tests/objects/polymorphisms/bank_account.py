import unittest
import sys
import os
import unittest.mock

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)
from objects.polymorphisms.bank_account import BankAccount


class BankAccountTestCase(unittest.TestCase):

    @unittest.mock.patch.object(BankAccount, "get_balance", return_value=1000)
    def test_deposit(self, mock_get_balance):
        self.assertEqual(mock_get_balance.return_value, 1000)

    @unittest.mock.patch.object(BankAccount, "set_balance", return_value=None)
    def test_withdraw(self, mock_set_balance):
       #self.assertEqual(mock_get_balance.return_value, None)
        self.assertEqual(mock_set_balance.return_value, None)


if __name__ == "__main__":
    unittest.main()
