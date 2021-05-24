from enum import Enum


class Square(Enum):
    EMPTY = 0
    FIRST = 1
    SECOND = 2

    def __invert__(self):
        return Square.EMPTY if self == Square.EMPTY else Square.SECOND if self == Square.FIRST else Square.FIRST


class Player(Enum):
    FIRST = 1
    SECOND = 2

    def __invert__(self):
        return Player.SECOND if self == Player.FIRST else Player.FIRST
