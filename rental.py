import datetime
from movie import Movie
from pricing import NewRelease, RegularPrice, ChildrenPrice


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie, days_rented):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = self._price_code_for_movie()

    def get_movie(self) -> Movie:
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def _price_code_for_movie(self):
        """
        Deciding price code depends on attributes of movie.

        The movie that release this year will follow NewRelease pricing rule.
        The movie that consider as children movie will follow ChildrenPrice pricing rule.
        Otherwise, follow Regular pricing rule
        """
        if self.movie.year == datetime.datetime.now().year:
            return NewRelease()
        if "Children" in self.movie.genre or "Childrens" in self.movie.genre:
            return ChildrenPrice()
        return RegularPrice()

    def get_price(self):
        # compute rental change
        return self.price_code.get_price(self.days_rented)

    def get_rental_points(self):
        # compute the frequent renter points based on movie price code
        return self.price_code.get_rental_points(self.days_rented)
