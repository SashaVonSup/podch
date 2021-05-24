from enum import Enum


class Square(Enum):
    EMPTY = 0
    FIRST = 1
    SECOND = 2


class Player(Enum):
    FIRST = 1
    SECOND = 2

    def __invert__(self):
        return Player.SECOND if self == Player.FIRST else Player.FIRST
