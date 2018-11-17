#!/usr/bin/python3

from typing import List

from .rating import Rating


class User:
    def __init__(self, name: str, identifier: str) -> None:
        self._name = name
        self._identifier = int(identifier)
        self._ratings = []  # type: List[Rating]

    def add_rating(self, rating: Rating) -> None:
        """
        Add a movie rating.

        Args:
            rating: The rating to add.
        """
        self._ratings.append(rating)

    def get_rating(self, movie: str) -> float:
        """
        Retrieve a rating for a movie.

        Args:
            movie: The movie for which to retrieve a rating

        Raises:
            NoSuchRating: If the movie hasn't been rated.

        Returns:
            float: The movie rating
        """
        for rating in self._ratings:
            if rating.movie == movie:
                return rating.rating

        raise NoSuchRating("No ratings for {}".format(movie))

    def has_seen(self, movie: str) -> bool:
        """
        Check if the user has seen the specified movie.

        Args:
            movie: The movie to check.

        Returns:
            bool: True if the user has seen the movie, False otherwise.
        """
        try:
            self.get_rating(movie)
        except NoSuchRating:
            return False
        return True

    @property
    def name(self) -> str:
        return self._name

    @property
    def identifier(self) -> int:
        return self._identifier

    @property
    def ratings(self) -> List[Rating]:
        return self._ratings


class NoSuchRating(Exception):
    pass
