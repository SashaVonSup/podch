from .enums import Enum, Square


class Board:
    def __init__(self, height: int, width: int):
        if height <= 0 or width <= 0:
            raise ValueError('height or width not natural')
        self._board = [[Square.EMPTY] * width for _ in range(height)]

    @property
    def height(self) -> int:
        return len(self._board)

    @property
    def width(self) -> int:
        return len(self._board[0])

    def __getitem__(self, item: tuple[int, int]) -> Square:
        if len(item) != 2:
            raise IndexError(f'expected size of key 2, {len(item)} found')
        return self._board[item[0]][item[1]]

    def __setitem__(self, key: tuple[int, int], value):
        if len(key) != 2:
            raise IndexError(f'expected size of key 2, {len(key)} found')
        self._last_key = key
        self._last_square = self._board[key[0]][key[1]]
        if isinstance(value, Enum):
            value = value.value
        self._board[key[0]][key[1]] = Square(value)

    def rollback(self):
        self[self._last_key] = self._last_square

    def __hash__(self) -> int:
        res = 0
        for row in self._board:
            for square in row:
                res *= 4  # len(Square) + 1
                res += square.value + 1
        return res
