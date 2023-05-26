from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_UNITS_DECREASE = 5
    INITIAL_OXYGEN = 70

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN)
