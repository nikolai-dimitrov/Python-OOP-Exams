from abc import ABC, abstractmethod


class BaseFish(ABC):
    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    # All passed names would be unique and it will not be necessary to check if a given name already exists.
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if value == "":
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be equal to or below zero.")
        self.__price = value

    def find_fish_type(self):
        return self.__class__.__name__

    @abstractmethod
    def eat(self):
        self.size += 5
