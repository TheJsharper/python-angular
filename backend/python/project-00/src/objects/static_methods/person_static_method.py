class PersonStaticMethod:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age: int) -> bool:
        return age >= 18

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
