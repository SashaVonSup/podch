from podch import Game
from podch.game import ImpossibleMoveError

if __name__ == '__main__':
    while True:
        try:
            height, width = map(int, input('Board heigth and width (e.g. 2 3): ').split())
            game = Game(height, width)
        except TypeError:
            print('Size does not match format')
        except ValueError:
            print('Size does not match format')
        else:
            break

    while not game.is_over:
        for i in range(height):
            print(''.join(str(game[i, j].value) for j in range(width)))
        while True:
            try:
                game.move(*map(int, input(f"{game.current_move}'s move (e.g. 0 1): ").split()))
            except ImpossibleMoveError as e:
                print('Impossible move: ' + e.args[0])
            except IndexError:
                print('Coordinates out of the board')
            except TypeError:
                print('Move does not match format')
            except ValueError:
                print('Move does not match format')
            else:
                break
    print(f'Game over: {game.winner} won!')
