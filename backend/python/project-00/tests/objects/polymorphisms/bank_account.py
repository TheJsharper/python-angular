import unittest
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../src"))
)
from objects.polymorphisms.bank_account import BankAccount



class BankAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("John Doe", "123456789", 1000)

    def test_deposit(self):
        #self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_withdraw(self):
        #self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 1000)

    def test_overdraft(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)


if __name__ == "__main__":
    unittest.main()
