from .bank_account import BankAccount


class PayrollAccount(BankAccount):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        if amount > self.get_balance():
            raise ValueError("Insufficient funds.")
        self.set_balance(self.get_balance() - amount)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.set_balance(self.get_balance() + amount)

    def __str__(self):
        return f"PayrollAccount(account_number={self.get_account_number()}, balance=${self.get_balance()})"
