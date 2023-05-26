from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_UNITS_DECREASE = 15
    INITIAL_OXYGEN = 90

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)
