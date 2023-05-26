from project.movie_specification.movie import Movie
from project.user import User


class Action(Movie):
    MIN_AGE = 12

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter  # check
    def age_restriction(self, value):
        if value < self.MIN_AGE:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value

    # def details(self):  # check
    #     return f"{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
