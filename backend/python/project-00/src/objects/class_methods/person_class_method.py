from typing_extensions import Self


class PersonClassMethod:
    species = "Human"

    def __init__(self: type[Self], name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls: type[Self], name: str, birth_year: int) -> Self:
        current_year = 2024
        age = current_year - birth_year
        return cls(name, age)

    @classmethod
    def change_species(cls: type[Self], new_species: str) -> None:
        cls.species = new_species
