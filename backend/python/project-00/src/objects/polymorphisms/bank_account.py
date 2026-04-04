from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, owner: str, account_number: str, balance: float = 0) -> None:
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, amount: float) -> None:
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Balance cannot be negative.")

    def get_owner(self) -> str:
        return self.owner

    def get_account_number(self) -> str:
        return self.account_number

    def set_owner(self, owner: str) -> None:
        self.owner = owner

    def set_account_number(self, account_number: str) -> None:
        self.account_number = account_number

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner}, account_number={self.account_number}, balance=${self.__balance})"
