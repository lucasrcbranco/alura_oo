from random import randint
from abc import ABC
from collections.abc import MutableSequence

class Show:
    def __init__(self, title, year):
        self._title = title
        self._year = year
        self._likes = 0

    def __str__(self):
        return f"{self._title} - {self._year} - {self._likes}"

    def give_a_like(self):
        self._likes += 1

    @property
    def year(self):
        return f"Year of {self._year}"

    @property
    def title(self):
        return self._title.title()

    @property
    def duration(self):
        return f"{self._duration} minutes long"

    @property
    def likes(self):
        return f"Has {self._likes} likes."


class Movie(Show):
    def __init__(self, title, year, duration):
        super().__init__(title, year)
        self.__duration = duration

    def __str__(self):
        return f"{self.title} - {self.year} - {self.duration} - {self.likes}"

    @property
    def duration(self):
        return f"{self.__duration} minutes long"


class TvShow(Show):
    is_vecna_here: bool = False

    def __init__(self, title, year, lenght):
        super().__init__(title, year)
        self.__lenght = lenght

    def __str__(self):
        return f"{self.title} - {self.year} - {self.lenght} - {self.likes}"

    @property
    def lenght(self):
        return f"{self.__lenght} seasons"


    @classmethod
    def is_vecna_here(cls):
        is_vecna_here = bool(randint(0, 1))

        if is_vecna_here:
            return "Vecna is here."
        else:
            return "Vecna is not here... yet!"


class Playlist:
    def __init__(self, title: str, shows: [Show]):
        self._title = title
        self._shows = shows

    def __getitem__(self, item):
        return self._shows[item]

    def __len__(self):
        return len(self._shows)


class PlaylistABC(MutableSequence):
    pass


playlistABC = PlaylistABC()

morbius: Movie = Movie("Morbius", 2022, 108)

strangerThings: TvShow = TvShow("Stranger Things", 2016, 4)

playlistScaryMovies: Playlist = Playlist("Spoopy", [morbius, strangerThings])

print(len(playlistScaryMovies))

for show in playlistScaryMovies:
    print(show)