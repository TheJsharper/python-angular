class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float = 0) -> None:
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def get_balance(self) -> float:
        return self.balance

    def get_owner(self) -> str:
        return self.owner

    def get_account_info(self) -> str:
        return f"Owner: {self.owner}, Account Number: {self.account_number}, Balance: ${self.balance}"

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner}, account_number={self.account_number}, balance=${self.balance})"
