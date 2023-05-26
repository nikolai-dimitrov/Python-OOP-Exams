from project.car.car import Car
from project.race import Race
from project.driver import Driver
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def find_existing_model(collection, searched_model):  # static or not
        for item in collection:
            if item.model == searched_model:
                return True
        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        valid_car_types = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}
        if car_type in valid_car_types.keys():
            if any(car.model == model for car in self.cars):
                raise Exception(f"Car {model} is already created!")
            new_car = valid_car_types[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_race(self, race_name: str):
        if any([race.name == race_name for race in self.races]):
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def create_driver(self, driver_name: str):
        if any([driver.name == driver_name for driver in self.drivers]):
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver
        raise Exception(f"Driver {driver_name} could not be found!")

    def find_car(self, car_type):
        avaible_cars = ["MuscleCar", "SportsCar"]
        if car_type in avaible_cars:
            for car in reversed(self.cars):
                if car.__class__.__name__ == car_type and car.is_taken == False:
                    # if not car.is_taken:
                    return car
        raise Exception(f"Car {car_type} could not be found!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.find_driver(driver_name)
        car = self.find_car(car_type)
        if driver.car is None:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."
        driver.car.is_taken = False
        old_car = driver.car  # MAYBE I have to REMOVE TAKEN CAR FROM LIST?
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} changed his car from {old_car} to {car.model}."

    # ------------------------
    def find_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    @staticmethod
    def check_for_driver_in_race(driver_name, race):
        for driver in race.drivers:
            if driver.name == driver_name:
                return True
        return False

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.find_race(race_name)
        driver = self.find_driver(driver_name)
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if self.check_for_driver_in_race(driver_name, race):
            raise Exception(f"Driver {driver_name} is already added in {race_name} race.")
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.find_race(race_name)
        if len(race.drivers) < 3:
            return f"Race {race_name} cannot start with less than 3 participants!"
        race_result = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]
        result = ''
        for driver in race_result:
            driver.number_of_wins += 1
            result += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"
        return result.strip()

# DA VIDQ NA LUBOMIR V GITHUBA 88 RED KAK RABOTI TOVA AKO NE NAMERI NAME == NAME KAKVO VRUSHTA I KAK IF SE SPRQVA S VRUSHTANETO NA NONE!
controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]
