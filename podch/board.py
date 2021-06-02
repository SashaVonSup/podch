from .enums import Enum, Square


class RollbackError(Exception):
    pass


class Board:
    def __init__(self, height: int, width: int):
        if height <= 0 or width <= 0:
            raise ValueError('height or width not natural')
        self._board = [[Square.EMPTY] * width for _ in range(height)]
        self._last_key = (0, 0)
        self._last_square = Square.EMPTY

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
        if self[self._last_key] == self._last_square:
            raise RollbackError('nothing to rollback')
        self[self._last_key] = self._last_square

    def __hash__(self) -> int:
        res = 0
        for row in self._board:
            for square in row:
                res *= 5  # len(Square) + 2
                res += square.value + 1
            res += 4  # len(Square) + 1 means a newline
        return res

    @property
    def _transforms(self):
        def transforms(board_):
            def reflects(board):
                yield board
                yield board[::-1]
                yield [row[::-1] for row in board]
                yield [row[::-1] for row in board[::-1]]

            for form in reflects(board_):
                yield form
            if self.height == self.width:
                for form in reflects([[board_[j][i] for j in range(self.width)] for i in range(self.height)]):
                    yield form

        for transform in transforms(self._board):
            yield transform
        for transform in transforms([[~square for square in row] for row in self._board]):
            yield transform

    def hash(self) -> int:  # min hash of all transformations
        temp = Board(self.height, self.width)
        res = hash(self)
        for board in self._transforms:
            temp._board = board
            res = min(res, hash(temp))
        return res
