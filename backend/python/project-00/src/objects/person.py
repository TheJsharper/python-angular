class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def work(self) -> str:
        return f"{self.name} is working."

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."
