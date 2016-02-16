"""
Principles of Computing - Week 3
2016-Jan
Python 2.7
Chris

A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
#import codeskulptor
#codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 100000

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    print "Calculating for %d items ..." % (num_items)
    move_score = [0, 0, 0, 0]
    for int_move in range(1, MAX_REMOVE + 1):
        for _ in range(TRIALS):
            move_score[int_move] += test_game(num_items, int_move)
    print "Results for %d items" % (num_items), move_score[1:]
    return move_score.index(max(move_score[1:]))

def test_game(num_items, start_move):
    current_items = num_items - start_move
    if current_items <= 0:
        return 1
    while True:
        player_move = random.randint(1, MAX_REMOVE)
        current_items -= player_move
        if current_items <= 0:
            return -1
            break
        comp_move = random.randint(1, MAX_REMOVE)
        current_items -= comp_move
        if current_items <= 0:
            return 1
            break

def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """

    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move: "))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

print "Please choose starting number of items."
print "21 is the most common game - 11 (and lower) has optimal AI play."
play_game(int(raw_input("Choice: ")))
