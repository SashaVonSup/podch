from enum import Enum


class Square(Enum):
    EMPTY = 0
    FIRST = 1
    SECOND = 2

    def __invert__(self):
        match self:
            case Square.EMPTY:
                return Square.EMPTY
            case Square.FIRST:
                return Square.SECOND
            case Square.SECOND:
                return Square.FIRST


class Player(Enum):
    FIRST = 1
    SECOND = 2

    def __invert__(self):
        match self:
            case Player.FIRST:
                return Player.SECOND
            case Player.SECOND:
                return Player.FIRST
