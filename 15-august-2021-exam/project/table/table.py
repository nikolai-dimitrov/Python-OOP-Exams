from abc import ABC, abstractmethod

from project.Validators.validator import number_validator
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    TABLE_TYPE = 'None'
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    CAPACITY_ERROR_MESSAGE = "Capacity has to be greater than 0!"

    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not self.MIN_NUMBER <= value <= self.MAX_NUMBER:
            raise ValueError(
                f"{self.TABLE_TYPE} table's number must be between {self.MIN_NUMBER} and {self.MAX_NUMBER} inclusive!")
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        number_validator(value, self.CAPACITY_ERROR_MESSAGE)
        self.__capacity = value

    def reserve(self, number_of_people: int):
        if number_of_people <= self.capacity:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_cost = sum([x.price for x in self.food_orders])
        drink_cost = sum([x.price for x in self.drink_orders])
        total_price = food_cost + drink_cost
        return total_price

    def clear(self):
        self.is_reserved = False
        self.number_of_people = 0  # Not in docs.
        self.food_orders = []
        self.drink_orders = []

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.TABLE_TYPE}Table\n" \
                   f"Capacity: {self.capacity}"
