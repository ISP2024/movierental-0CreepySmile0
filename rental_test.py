import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
		self.regular_movie = Movie("Air", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", Movie.REGULAR)
		self.assertEqual("Air", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	# @unittest.skip("add this test when you refactor rental price")
	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 4)
		self.assertEqual(rental.get_price(), 5.0)
		rental = Rental(self.childrens_movie, 3)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

	# @unittest.skip("add this test of rental points when you add it to Rental")
	def test_rental_points(self):
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_rental_points(), 5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_rental_points(), 1)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_rental_points(), 1)
