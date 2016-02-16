"""
Principles of Computing - week 3
2016-Jan
Python 2.7
Chris

Monte Carlo Tic-Tac-Toe Player
"""

import random
#import poc_ttt_gui
import poc_ttt_provided as provided
#import codeskulptor
#codeskulptor.set_timeout(10)  # default value is 5 seconds.

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):

    '''
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves,
    alternating between players.
     The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.
    In other words, the function should modify the board input.
    '''

    winner = None
    while winner == None:
        random_move = random.choice(board.get_empty_squares())
        board.move(random_move[0], random_move[1], player)
        winner = board.check_win()
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):

    '''
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board
     a board from a completed game, and which player the machine player is.
    The function should score the completed board and update the scores grid.
    As the function updates the scores grid directly, it does not return anything,
    '''

    winner = board.check_win()

    if winner == provided.DRAW:
        pass
    elif winner == player:
        for xxx in range(board.get_dim()):
            for yyy in range(board.get_dim()):
                if board.square(xxx, yyy) == player:
                    scores[xxx][yyy] += SCORE_CURRENT
                # pylint likes a max of 12 branches, hence the long elif.
                # possibly look into a better way of doing this
                elif board.square(xxx, yyy) != provided.EMPTY and board.square(xxx, yyy) != player:
                    scores[xxx][yyy] -= SCORE_OTHER
    else:
        for xxx in range(board.get_dim()):
            for yyy in range(board.get_dim()):
                if board.square(xxx, yyy) == player:
                    scores[xxx][yyy] -= SCORE_CURRENT
                elif board.square(xxx, yyy) == provided.EMPTY:
                    pass
                else:
                    scores[xxx][yyy] += SCORE_OTHER


def get_best_move(board, scores):

    '''
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the maximum score
     and randomly return one of them as a (row, column) tuple.
     It is an error to call this function with a board that has no empty squares
    (there is no possible next move), so your function may do whatever it wants in that case.
    The case where the board is full will not be tested.
    '''

    # get empty BOARD spots
    # for these empty BOARD sports, find MAX VALUE of spot in SCORES
    # return ROW, COLUMN tuple

    if not board.get_empty_squares():
        pass
    empty_board_spots = board.get_empty_squares()
    choice_spot_dict = {}
    for spot in empty_board_spots:
        choice_spot_dict[spot] = scores[spot[0]][spot[1]]
    max_value = max(choice_spot_dict.values())
    max_options = [k for k, v in choice_spot_dict.items() if v == max_value]
    return random.choice(max_options)

def mc_move(board, player, trials):

    '''
    This function takes a current board, which player the machine player is, and the number of trials to run.
    The function should use the Monte Carlo simulation described above to return
    a move for the machine player in the form of a (row, column) tuple.
    Be sure to use the other functions you have written!
    '''
    # get best move!
    # run multiple trials to get value!
    # so loop through each of my functions!
    clone_board = board.clone()
    empty_board = board.clone()
    board_scores = []
    for _ in range(board.get_dim()):
        board_scores.append([0] * board.get_dim())
    for dummy in range(trials):
        mc_trial(clone_board, player)
        mc_update_scores(board_scores, clone_board, player)
        clone_board = empty_board.clone()
    best_move = get_best_move(clone_board, board_scores)
    del board_scores[:]
    for dummy in range(board.get_dim()):
        board_scores.append([0] * board.get_dim())
    return best_move

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

provided.play_game(mc_move, NTRIALS, False)

# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
# # GUI arguments = size of board, comp player, move_func, NTRIALS, normal(False)/reverse(True) TTT game
