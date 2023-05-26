class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.validate_name(value, "Planet name cannot be empty string or whitespace!")
        self.__name = value

    @staticmethod
    def validate_name(name, message):
        if name == "" or name.isspace():
            raise ValueError(message)
