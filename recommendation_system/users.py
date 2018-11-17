#!/usr/bin/python3

import collections
import csv
from typing import Any, List

from .rating import Rating
from .user import NoSuchRating, User

WeightedScore = collections.namedtuple("WeightedScore", "movie, score")


class Users:
    def __init__(self, users: str, ratings: str) -> None:
        """
        Initialize the users with their respective ratings.

        Args:
            users: A CSV file with users.
            ratings: A CSV file with ratings.
        """
        self._users = self._parse(users, User, ["UserName", "UserID"])

        self._movies = []  # type: List[str]
        for r in self._parse(ratings, Rating, ["UserID", "Movie", "Rating"]):
            self._find(identifier=r.identifier).add_rating(r)
            # Store the titles of the rated movies.  We need this
            # information to calculate the weighted score for each user.
            # Not super thrilled about doing it like this; it feels very
            # hackish.
            if r.movie not in self._movies:
                self._movies.append(r.movie)

    def weighted_scores(self, name: str=None,
                        identifier: int=0) -> List[WeightedScore]:
        """
        Calculate the weighted score for every rated movie.

        Args:
            name: The target username
            identifier: The target user identifier

        Raises:
            NoSuchUser: If the user doesn't exist.

        Returns:
            list: A list of weighted scores sorted in descending order.
        """
        result = []
        user = self._find(name=name, identifier=identifier)

        for movie in self._movies:
            total = 0.0
            sim_sum = 0.0
            for other in self._users:
                # skip the target user
                if other == user:
                    continue

                try:
                    rating = other.get_rating(movie)
                    sim = self._euclidean(user, other)
                    sim_sum += sim
                    total += sim * rating
                except NoSuchRating:
                    pass

            result.append(WeightedScore(movie, total / sim_sum))
        result.sort(key=lambda ws: ws.score, reverse=True)
        return result

    def _find(self, name: str=None, identifier: int=0) -> User:
        """
        Retrieve a user.

        Args:
            name:       The name of the user to retrieve.
            identifier: The ID of the user to retrieve.

        Raises:
            NoSuchUser: If the user doesn't exist.

        Returns:
            object: A user or None if no user is found.
        """
        for user in self._users:
            if user.name == name or user.identifier == identifier:
                return user

        raise NoSuchUser("No user for name:{}, id:{}".format(name, identifier))

    @staticmethod
    def _euclidean(a: User, b: User) -> float:
        """
        Calculate the euclidean distance between two users.

        Args:
            a: The first user
            b: The second user

        Returns:
            float: The distance.
        """
        sim = 0.0
        n = 0

        for a_r in a.ratings:
            try:
                b_r = b.get_rating(a_r.movie)
                sim += (a_r.rating - b_r)**2
                n += 1
            except NoSuchRating:
                pass

        if n:
            return 1 / (1 + sim)
        return 0.0

    @staticmethod
    def _parse(filename: str, cls: Any, header: List[str]) -> List[Any]:
        """
        Parse a CSV file.

        Args:
            filename: Path to the CSV file.
            cls: Class to instantiate for each entry in the CSV file.
            header: Entries matching this header are ignored.

        Returns:
            list: A list of 'cls' instances.
        """
        result = []

        with open(filename, newline="") as f:
            for entry in csv.reader(f, delimiter=";"):
                if entry == header:
                    continue
                result.append(cls(*entry))

        return result


class NoSuchUser(Exception):
    pass
