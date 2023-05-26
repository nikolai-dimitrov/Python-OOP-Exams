from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if any([x.username == username for x in self.users_collection]):
            raise Exception("User already exists!")
        new_user = self.create_user(username, age)
        # if new_user not in self.users_collection:  # check maybe this is usless.
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):  # check
        current_user = self.find_user_by_name(username)
        if not current_user:
            raise Exception("This user does not exist!")
        if any([x.title == movie.title for x in self.movies_collection]):
            raise Exception("Movie already added to the collection!")
        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        current_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not any([x.title == movie.title for x in self.movies_collection]):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for attribute, value in kwargs.items():
            setattr(movie,attribute,value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if not any([x.title == movie.title for x in self.movies_collection]):
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        current_user = self.find_user_by_name(username)
        current_user.movies_owned.remove(
            movie)  # check if it is needed to be removed from all users who have this film in collection.
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        current_user = self.find_user_by_name(username)
        for c_movie in current_user.movies_liked:  # try with if movie(object) in current_user.liked_movies ..!
            if c_movie.title == movie.title:
                raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        current_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        current_user = self.find_user_by_name(username)
        for c_movie in current_user.movies_liked:
            if c_movie.title == movie.title:
                current_user.movies_liked.remove(movie)
                movie.likes -= 1
                return f"{username} disliked {movie.title} movie."
        raise Exception(f"{username} has not liked the movie {movie.title}!")

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return '\n'.join([x.details() for x in sorted_movies])

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += f"All users: {', '.join(x.username for x in self.users_collection)}\n"
        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join(x.title for x in self.movies_collection)}\n"
        return result.strip()

    @staticmethod
    def create_user(username, age):
        return User(username, age)

    def find_user_by_name(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user


# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)

