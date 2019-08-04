from six.moves import input

from go import goboard_f as goboard
from go import gotypes
from go import scoring
from go.monte import monte
from go.utils import print_board, print_move, get_valid_human_move

BOARD_SIZE = 9

#
# def capture_diff(game_state):
#     black_stones = 0
#     white_stones = 0
#     for r in range(1, game_state.board.num_rows + 1):
#         for c in range(1, game_state.board.num_cols + 1):
#             p = gotypes.Point(r, c)
#             color = game_state.board.get(p)
#             if color == gotypes.Player.black:
#                 black_stones += 1
#             elif color == gotypes.Player.white:
#                 white_stones += 1
#     diff = black_stones - white_stones
#     if game_state.next_player == gotypes.Player.black:
#         return diff
#     return -1 * diff


def main():
    game = goboard.GameState.new_game(BOARD_SIZE)
    bot = monte.MCTSAgent(1000, 1.5)

    while not game.is_over():
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            move = get_valid_human_move(game)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)

    print(f"WINNER: {game.winner()}")
    print(scoring.compute_game_result(game))


if __name__ == '__main__':
    main()
