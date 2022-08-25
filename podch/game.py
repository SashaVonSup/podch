from .board import Board
from .enums import Square, Player


class ImpossibleMoveError(Exception):
    # when raised, board should be safe
    pass


class Game:
    winner: Player

    def __init__(self, height: int, width: int):
        self._board = Board(height, width)
        self._used = {self._board.hash()}
        self.current_move = Player.FIRST
        self.is_over = False

    @property
    def height(self) -> int:
        return self._board.height

    @property
    def width(self) -> int:
        return self._board.width

    def is_possible(self, x: int, y: int, player: Player, message: bool = False) -> bool | str:
        if self._board[x, y] == Square((~player).value):
            return 'foreign stone in the square' if message else False
        self._board[x, y] = Square(player.value) if self._board[x, y] == Square.EMPTY else Square.EMPTY
        res = self._board.hash() not in self._used
        self._board.rollback()
        if message:
            return '' if res else 'situation used before'
        return res

    def possible_moves(self, player: Player) -> set[tuple[int, int]]:
        return {(i, j) for j in range(self.width) for i in range(self.height) if self.is_possible(i, j, player)}

    def move(self, x: int, y: int):
        if self.is_over:
            raise ImpossibleMoveError('game over')
        if message := self.is_possible(x, y, self.current_move, True):
            raise ImpossibleMoveError(message)
        self._board[x, y] = Square(self.current_move.value) if self._board[x, y] == Square.EMPTY else Square.EMPTY
        self._used.add(self._board.hash())
        if not self.possible_moves(~self.current_move):
            self.is_over = True
            self.winner = self.current_move
        self.current_move = ~self.current_move

    def __getitem__(self, item):
        return self._board[item]
