def crypto(password):
    """Simulate password encryption."""
    return f"encrypted_{password}"


class PersonPrivatedAttr:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__password = "secret 123"

    def __str__(self):
        return f"{self.__name} is {self.__age} years old."

    def get_password(self) -> str:
        return crypto(self.__password)  # Simulate password encryption

    def set_password(self, new_password) -> None:
        self.__password = new_password  # Update the password

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def work(self):
        return f"{self.__name} is working."
