from objects.oop.bank_account import BankAccount


class SavingAccount(BankAccount):
    def __init__(
        self,
        owner: str,
        account_number: str,
        balance: float = 0,
        interest_rate: float = 0.01,
    ) -> None:
        super().__init__(owner, account_number, balance)
        self.__interest_rate = interest_rate

    def apply_interest(self) -> None:
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)
        print(f"Applied interest of ${interest}. New balance: ${self.get_balance()}")

    def withdraw(self, amount: float) -> None:
        if amount > 0:
            if self.get_balance() >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.get_balance()}")
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.get_balance()}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def __str__(self) -> str:
        return f"SavingAccount(owner={self.get_owner()}, account_number={self.account_number}, balance=${self.get_balance()}, interest_rate={self.__interest_rate})"
