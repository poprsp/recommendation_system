#!/usr/bin/python3


class Rating:
    def __init__(self, identifier: str, movie: str, rating: str) -> None:
        self._identifier = int(identifier)
        self._movie = movie
        self._rating = float(rating)

    @property
    def identifier(self) -> int:
        return self._identifier

    @property
    def movie(self) -> str:
        return self._movie

    @property
    def rating(self) -> float:
        return self._rating
