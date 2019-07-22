from go.agent import naive
from go import goboard as board
from go import gotypes
from go.utils import print_board, print_move, point_from_coords
import time


def main():
    board_size = 9
    game = board.GameState.new_game(board_size)
    bot = naive.RandomBot()

    while not game.is_over():
        # time.sleep(.3)
        print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            while True:
                try:
                    human_move = input('--')
                    point = point_from_coords(human_move)
                    move = board.Move.play(point)
                    print_move(game.next_player, move)
                    game = game.apply_move(move)
                    break
                except IndexError:
                    print(f'invalid input, try again:')
                    continue
                except AssertionError:
                    print(f'invalid move, try again:')
                    continue
        else:
            move = bot.select_move(game)
            print_move(game.next_player, move)
            game = game.apply_move(move)


if __name__ == '__main__':
    main()
