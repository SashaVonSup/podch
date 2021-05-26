from podch import Game

if __name__ == '__main__':
    height = int(input('Board height: '))
    width = int(input('Board width: '))
    game = Game(height, width)

    while not game.is_over:
        for i in range(height):
            print(''.join(str(game[i, j].value) for j in range(width)))
        game.move(*map(int, input(f"{game.current_move}'s move (e.g. 0 1): ").split()))
    print(f'Game over: {game.winner} won!')
