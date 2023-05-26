from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    # All passed names would be unique and it will not be necessary to check if a given name already exists.
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total_comfort = sum([x.comfort for x in self.decorations])
        return total_comfort

    def add_fish(self, fish):
        # Possible fish_types are: "FreshwaterFish" and "SaltwaterFish".
        # if fish.__class__.__name__ in ("FreshwaterFish", "SaltwaterFish"):
        if len(self.fish) >= self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def find_aquarium_type(self):
        return self.__class__.__name__

    def __str__(self):
        result = f"{self.name}:\n"
        if self.fish:
            fishes = ' '.join([x.name for x in self.fish])
            result += f"Fish: {fishes}" + "\n"
        else:
            result += "Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result.rstrip()
