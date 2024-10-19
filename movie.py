import pricing


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = pricing.RegularPrice()
    NEW_RELEASE = pricing.NewRelease()
    CHILDRENS = pricing.ChildrenPrice()

    def __init__(self, title, price_code):
        # Initialize a new movie.
        if not isinstance(price_code, pricing.PriceStrategy):
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
