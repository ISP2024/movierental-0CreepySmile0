import pricing


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).
    REGULAR = pricing.RegularPrice()
    NEW_RELEASE = pricing.NewRelease()
    CHILDRENS = pricing.ChildrenPrice()

    def __init__(self, title):
        # Initialize a new movie.
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
