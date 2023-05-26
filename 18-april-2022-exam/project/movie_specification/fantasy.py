from project.movie_specification.movie import Movie
from project.user import User


class Fantasy(Movie):
    MIN_AGE = 6

    def __init__(self, title: str, year: int, owner: User, age_restriction: int):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter#check
    def age_restriction(self, value):
        if value < self.MIN_AGE:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    # def details(self):#check
    #     return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
