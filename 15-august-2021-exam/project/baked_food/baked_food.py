from abc import ABC, abstractmethod

from project.Validators.validator import name_validator, number_validator


class BakedFood(ABC):
    NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"
    PRICE_ERROR_MESSAGE = "Price cannot be less than or equal to zero!"

    @abstractmethod
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        number_validator(value, self.PRICE_ERROR_MESSAGE)
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
