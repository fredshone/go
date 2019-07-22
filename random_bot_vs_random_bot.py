from go.agent import naive
from go import goboard_slow as board
from go import gotypes
from go.utils import print_board, print_move
import time


def main():
    board_size = 9
    game = board.GameState.new_game(board_size)
    bots = {
            gotypes.Player.black: naive.RandomBot(),
            gotypes.Player.white: naive.RandomBot(),
            }
    while not game.is_over():
        # time.sleep(.3)
        print(chr(27) + "[2J")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()
