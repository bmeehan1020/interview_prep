from enum import Enum, auto
from typing import List


class Genre(Enum):
    POP: auto()
    COUNTRY: auto()


class JukeBox:
    volume_min = 0
    volume_max = 100

    def __init__(self, songs: List[Song]):
        self.songs = songs
        self.volume = 50
        self.credits = 0
        self.isPlaying = False

    def play(self, song):
        return None

    def pause(self):
        return None

    def shuffle(self):
        return None

    def resume(self):
        return None

    def incrementVolume(self):
        return None

    def decrementVolume(self):
        return None

    def addCredits(self, dollars: int) -> int:
        return self.credits

    def useCredits(self, cost: int) -> bool:
        return True

    def search(self, query: str) -> List[Song]:
        return None

    def filter(self, genre: Genre) -> List[Song]:
        return None

    def sort_by_popularity(self) -> List[Song]:
        return None


class Song:
    def __init__(self, title: str, artist: str, album: str, data, genre: Genre, runtime: int):
        self.title = ...
        self.numPlays = 0
