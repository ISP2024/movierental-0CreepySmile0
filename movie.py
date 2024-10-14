from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""


class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_price(self, days: int) -> float:
        """Charge $3 per day."""
        return days * 3

    def get_rental_points(self, days: int) -> int:
        """New release rentals earn 1 point for each day rented."""
        return days


class ChildrenPrice(PriceStrategy):
    """Pricing rules for Children movies."""

    def get_price(self, days: int) -> float:
        """Charge $1.50 for first three days, additional $1.50 per day."""
        if days > 3:
            return 1.5 + (1.5 * (days - 3))
        return 1.5

    def get_rental_points(self, days: int) -> int:
        """Children movie rentals always earn 1 point."""
        return 1


class RegularPrice(PriceStrategy):
    """Pricing rules for Regular movies."""

    def get_price(self, days: int) -> float:
        """Charge $2 for first two days, additional $1.50 per day."""
        if days > 2:
            return 2 + (1.5 * (days - 2))
        return 2

    def get_rental_points(self, days: int) -> int:
        """Regular movie rentals always earn 1 point."""
        return 1


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = RegularPrice()
    NEW_RELEASE = NewRelease()
    CHILDRENS = ChildrenPrice()

    def __init__(self, title, price_code):
        # Initialize a new movie.
        if not isinstance(price_code, PriceStrategy):
            raise TypeError(f"{price_code} is not subclass of PriceStrategy")
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
