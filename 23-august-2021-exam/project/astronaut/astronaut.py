from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_UNITS_DECREASE = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value, "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.OXYGEN_UNITS_DECREASE

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    @staticmethod
    def validate_name(name, message):
        if name == "" or name.isspace():
            raise ValueError(message)
