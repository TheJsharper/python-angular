class PersonProtected:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
        self._energy = 100

    def __str__(self) -> str:
        return f"{self._name} is {self._age} years old."

    def _waseEnergy(self, amount) -> bool:
        if self._energy >= amount:
            self._energy -= amount
            return True
        else:
            return False

    def work(self):
        if self._waseEnergy(10):
            return f"{self._name} is working."
        else:
            return f"{self._name} is too tired to work."
