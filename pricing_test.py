import unittest
from movie import Movie
from rental import Rental
from pricing import NewRelease, ChildrenPrice, RegularPrice


class PricingTest(unittest.TestCase):
    """Test pricing decision."""

    def setUp(self):
        self.new_movie = Movie("TeeYod 2", 2024, ["Horror", "Thriller", "Action"])
        self.children_movie = Movie("Mulan", 1998, ["Animation", "Adventure", "Children"])
        self.regular_movie = Movie("Meg 2: The Trench", 2023, ["Action", "Thriller", "Sci-Fi"])

    def test_new_movie(self):
        rental = Rental(self.new_movie, 5)
        self.assertIsInstance(rental.price_code, NewRelease)
        self.assertEqual(rental.get_price(), 15)
        self.assertEqual(rental.get_rental_points(), 5)

    def test_regular_movie(self):
        rental = Rental(self.regular_movie, 4)
        self.assertIsInstance(rental.price_code, RegularPrice)
        self.assertEqual(rental.get_price(), 5)
        self.assertEqual(rental.get_rental_points(), 1)

    def test_children_movie(self):
        rental = Rental(self.children_movie, 5)
        self.assertIsInstance(rental.price_code, ChildrenPrice)
        self.assertEqual(rental.get_price(), 4.5)
        self.assertEqual(rental.get_rental_points(), 1)
