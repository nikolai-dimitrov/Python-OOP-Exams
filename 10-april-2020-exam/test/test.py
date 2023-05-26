from unittest import TestCase

from project.movie import Movie


class MovieTests(TestCase):
    NAME = 'Test'
    YEAR = 2000
    RATING = 10

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)
        self.movie.actors = ["Test Actor"]

    def test_init_work_correct(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual(["Test Actor"], self.movie.actors)

    # def test_getter_work_correct(self):
    def test_name_setter_with_wrong_value_raises(self):
        with self.assertRaises(ValueError) as error:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(error.exception))
        # it is tested in init (init test setters)
        # self.movie.name = "Gosho"
        # self.assertEqual("Gosho",self.movie.name)

    def test_year_setter_with_wrong_value_raises(self):
        with self.assertRaises(ValueError) as error:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_actor_with_non_existing_name_work_correct(self):
        self.movie.actors = []
        self.movie.add_actor("Test")
        self.assertEqual(["Test"], self.movie.actors)

    def test_actor_with_already_existing_actor(self):
        name = 'Test Actor'
        result = self.movie.add_actor(name)
        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual(["Test Actor"], self.movie.actors)

    def test_gt_work_correct(self):
        movie2 = Movie("Test1", 1900, 9)
        result = self.movie > movie2
        self.assertEqual(f'"Test" is better than "Test1"', result)
        movie2 = Movie("Test1", 1900, 12)
        result1 = self.movie > movie2
        self.assertEqual(f'"Test1" is better than "Test"', result1)

    def test_repr_work_correct(self):
        # f"Name: {self.name}\n" \
        # f"Year of Release: {self.year}\n" \
        # f"Rating: {self.rating:.2f}\n" \
        # f"Cast: {', '.join(self.actors)}"
        result = repr(self.movie)
        expected_result = f"Name: {self.NAME}\n" \
                          f"Year of Release: {self.YEAR}\n" \
                          f"Rating: {self.RATING:.2f}\n" \
                          f"Cast: {'Test Actor'}"
        self.assertEqual(expected_result,result)
