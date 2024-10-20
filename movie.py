import csv
import logging
from dataclasses import dataclass
from typing import Collection


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str):
        return genre.capitalize() in self.genre

    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieCatalog:
    _instance = None
    _movies = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            line = 0
            with open("movies.csv", mode="r") as file:
                csv_file = csv.reader(file)
                for lines in csv_file:
                    line += 1
                    try:
                        cls._movies.append(Movie(lines[1], int(lines[2]), set(lines[3])))
                    except ValueError:
                        logger.error(f"Line {line} in movies.csv: Unrecognized format {lines}")
                        continue
        return cls._instance

    def get_movie(self, title: str, year: int = None):
        if year is None:
            return next(
                filter(lambda x: x.title.capitalize() == title.capitalize(), self._movies),
                None
            )
        return next(
            filter(
                lambda x: x.titlecapitalize() == title.capitalize() and x.year == year,
                self._movies
            ),
            None
        )
