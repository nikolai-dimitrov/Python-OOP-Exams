from project.Validators.validator import name_validator
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if any([x.name == name for x in self.food_menu]):
            raise Exception(f"{food_type} {name} is already in the menu!")
        new_food = self.create_food(food_type, name, price)
        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if any([x.name == name for x in self.drinks_menu]):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        new_drink = self.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if any([x.table_number == table_number for x in self.drinks_menu]):
            raise Exception(f"Table {table_number} is already in the bakery!")
        new_table = self.create_table(table_type, table_number, capacity)
        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            # check try with if table is reserved == False
            if table.is_reserved == False:
                if number_of_people <= table.capacity:
                    table.reserve(number_of_people)
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        ordered_foods = f"Table {table_number} ordered:\n"
        skipped_ordered_foods = f"{self.name} does not have in the menu:\n"
        for food_name in food_names:
            food = self.find_food_by_name(food_name)
            if food is None:
                skipped_ordered_foods += food_name + '\n'
            else:
                table.order_food(food)
                ordered_foods += repr(food) + '\n'
        result = ordered_foods.strip() + '\n' + skipped_ordered_foods.strip()
        return result

    def order_drink(self, table_number: int, *drink_names):
        table = self.find_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        ordered_drinks = f"Table {table_number} ordered:\n"
        skipped_ordered_drinks = f"{self.name} does not have in the menu:\n"
        for drink_name in drink_names:
            drink = self.find_drink_by_name(drink_name)
            if drink is None:
                skipped_ordered_drinks += drink_name + '\n'
            else:
                table.order_drink(drink)
                ordered_drinks += repr(drink) + '\n'
        result = ordered_drinks.strip() + '\n' + skipped_ordered_drinks.strip()
        return result

    def leave_table(self, table_number: int):  # here
        table = self.find_table_by_number(table_number)
        if table:
            income = table.get_bill()
            self.total_income += income
            result = f"Table: {table_number}\n"
            result += f"Bill: {income:.2f}"
            table.clear()
            return result

    def get_free_tables_info(self):
        result = ''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result.strip()

    def get_total_income(self):  # here
        return f"Total income: {self.total_income:.2f}lv"

    @staticmethod
    def create_food(food_type: str, name: str, price: float):
        possible_types = {"Bread": Bread, "Cake": Cake}
        return possible_types[food_type](name, price)

    @staticmethod
    def create_drink(drink_type: str, name: str, portion: float, brand: str):
        possible_types = {"Water": Water, "Tea": Tea}
        return possible_types[drink_type](name, portion, brand)

    @staticmethod
    def create_table(table_type: str, table_number: int, capacity: int):
        possible_types = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}
        return possible_types[table_type](table_number, capacity)

    def find_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink


b = Bakery("RandomBakery")
print(b.add_table("InsideTable", 40, 20))
print(b.add_table("OutsideTable", 80, 20))
print(b.add_food("Cake", "Banana", 3.30))
print(b.add_food("Cake", "Apple", 5.70))
print(b.add_food("Cake", "Carrot", 10))
print(b.add_food("Bread", "Bread", 30))
print(b.add_drink("Water", "Mineral", 250, "Devin"))
print(b.add_drink("Tea", "Green", 400, "Nestea"))
print(b.reserve_table(10))
print(b.order_food(40, "Banana", "Apple", "Carrot", "Chicken", "Bread"))
print(b.order_drink(40, "Mineral", "Green", "NoExistingTea"))
print(b.leave_table(40))
