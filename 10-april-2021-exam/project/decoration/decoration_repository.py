from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        # Check maybe remove with for loop.
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    #Try to pop decoration and change logic in controller insert method
    def find_by_type(self, decoration_type):
        for i in range(len(self.decorations)):
            if self.decorations[i].__class__.__name__ == decoration_type:
                return self.decorations[i]
        return "None"