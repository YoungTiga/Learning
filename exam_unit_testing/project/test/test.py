from project.movie import Movie
from unittest import TestCase,main

class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("S",2002,8.5)

    def test_init(self):
        movie = Movie("S",2002,8.5)
        self.assertEqual("S",movie.name)
        self.assertEqual(2002,movie.year)
        self.assertEqual(8.5,movie.rating)
        self.assertEqual([],movie.actors)

    def test_name_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!",str(ex.exception))

    def test_year_setter_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!",str(ex.exception))

    def test_year_setter_edge_case(self):

        self.movie.year = 1887
        self.assertEqual(1887,self.movie.year)

    def test_add_actor_with_non_existing_actor(self):
        self.movie.add_actor("Ivan")
        self.assertEqual(["Ivan"],self.movie.actors)

    def test_add_actor_existing_actor(self):
        self.movie.actors = ["Ivan"]
        res = self.movie.add_actor("Ivan")
        self.assertEqual("Ivan is already added in the list of actors!",res)

    def test_gt_method_self_rating_greater(self):
        other_movie = Movie("D",2002,8.4)
        res = self.movie>other_movie
        self.assertEqual('"S" is better than "D"',res)

    def test_gt_method_other_rating_greater(self):
        other_movie = Movie("D", 2002, 8.7)
        res = self.movie > other_movie
        self.assertEqual('"D" is better than "S"', res)

    def test_gt_method_equal_ratings(self):
        other_movie = Movie("D", 2002, 8.5)
        res = self.movie > other_movie
        self.assertEqual('"D" is better than "S"', res)

    def test_repr_method(self):
        self.movie.actors = ["Ivan"]
        expected = "Name: S\n"
        expected +="Year of Release: 2002\n"
        expected +="Rating: 8.50\n"
        expected += "Cast: Ivan"
        res = self.movie.__repr__()
        self.assertEqual(expected,res)


if __name__ == "__main__":
    main()