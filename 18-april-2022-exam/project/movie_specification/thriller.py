from project.movie_specification.movie import Movie
from project.user import User


class Thriller(Movie):
    MIN_AGE = 16

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter  # check
    def age_restriction(self, value):
        if value < self.MIN_AGE:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value
