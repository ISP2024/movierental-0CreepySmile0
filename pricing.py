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

