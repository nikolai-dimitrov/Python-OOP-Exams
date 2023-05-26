from abc import ABC, abstractmethod

from project.Validators.validator import name_validator, number_validator


class Drink(ABC):
    NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"
    PORTION_ERROR_MESSAGE = "Portion cannot be less than or equal to zero!"
    BRAND_ERROR_MESSAGE = "Brand cannot be empty string or white space!"

    @abstractmethod
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        number_validator(value, self.PORTION_ERROR_MESSAGE)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        name_validator(value, self.BRAND_ERROR_MESSAGE)
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
