from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in ("FreshwaterAquarium", "SaltwaterAquarium"):
            return "Invalid aquarium type."
        aquarium = self.create_aquarium(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ("Ornament", "Plant"):
            return "Invalid decoration type."
        decoration = self.create_decoration(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    # Try with pop and first check if there is such aquarium than pop the decoration with method from deciration.(because of first occurence)
    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        if aquarium:
            decoration = self.decorations_repository.find_by_type(decoration_type)
            if decoration == "None":
                return f"There isn't a decoration of type {decoration_type}."
            # aquarium = self.find_aquarium_by_name(aquarium_name)
            # if aquarium:
            self.decorations_repository.remove(decoration)
            aquarium.add_decoration(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        # ll = [x for x in self.aquariums][5]
        if fish_type not in ("FreshwaterFish", "SaltwaterFish"):
            return f"There isn't a fish of type {fish_type}."
        fish = self.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.find_aquarium_by_name(aquarium_name)
        if not self.check_is_water_suitable(aquarium, fish_type):
            return "Water not suitable."
        result = aquarium.add_fish(fish)
        return result

    def feed_fish(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        fish_price = sum([x.price for x in aquarium.fish])
        decoration_price = sum([x.price for x in aquarium.decorations])
        result = fish_price + decoration_price
        return f"The value of Aquarium {aquarium_name} is {result:.2f}."

    def report(self):
        # ll = [x for x in self.aquariums][5]
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return '\n'.join(result)

    def find_aquarium_by_name(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium

    @staticmethod
    def check_is_water_suitable(aquarium, fish_type):
        aqua_type = aquarium.find_aquarium_type()
        if fish_type == "FreshwaterFish" and aqua_type == "FreshwaterAquarium":
            return True
        elif fish_type == "SaltwaterFish" and aqua_type == "SaltwaterAquarium":
            return True
        else:
            return False

    @staticmethod
    def create_fish(fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            return FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            return SaltwaterFish(fish_name, fish_species, price)

    @staticmethod
    def create_decoration(decoration_type):
        if decoration_type == "Plant":
            return Plant()
        elif decoration_type == "Ornament":
            return Ornament()

    @staticmethod
    def create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            return SaltwaterAquarium(aquarium_name)


controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Test1"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))
print(controller.insert_decoration("Test1", "Plant"))
print(controller.insert_decoration("Test1", "Plant"))
print(controller.add_fish("Test1", "FreshwaterFish", "TestFish", "FishSpecies", 5))
print(controller.add_fish("Test1", "FreshwaterFish", "TestFish", "FishSpecies", 5))
print(controller.add_fish("Test1", "FreshwaterFish", "TestFish", "FishSpecies", 5))
print(controller.feed_fish("Test1"))
print(controller.calculate_value("Test1"))

print(controller.add_aquarium("SaltwaterAquarium", "TestS"))
print(controller.add_decoration("Ornament"))
print(controller.add_decoration("Ornament"))
print(controller.insert_decoration("TestS", "Ornament"))
print(controller.insert_decoration("TestS", "Ornament"))
print(controller.add_fish("TestS", "SaltwaterFish", "TestFishS", "FishSpecies", 5))
print(controller.add_fish("TestS", "SaltwaterFish", "TestFishS", "FishSpecies", 5))
print(controller.add_fish("TestS", "SaltwaterFish", "TestFishS", "FishSpecies", 5))
print(controller.feed_fish("TestS"))
print(controller.calculate_value("TestS"))
print(controller.report())
