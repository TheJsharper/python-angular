class BasicsOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self) -> float:
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both a and b must be numbers")
        return self.a + self.b

    def subtract(self) -> float:
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both a and b must be numbers")
        return self.a - self.b

    def multiply(self) -> float:
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both a and b must be numbers")
        return self.a * self.b

    def divide(self) -> float:
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)):
            raise TypeError("Both a and b must be numbers")
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

    def __str__(self):
        return f"BasicsOperation(a={self.a}, b={self.b})"
