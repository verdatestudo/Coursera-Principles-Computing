"""
Number of possible Tic-Tac-Toe boards where X goes first.
Note that not all boards count are legal
since they may have a win for both X and O.
"""

'''
Additional Note - Chess
A rough estimate for possible boards using Shannon's number:

64! # number of squares
(32!) x (8!)**2 x (2!)**2 x (2!)**2 x (2!)**2 x (1!)**2 x (1!)**2
# empty squares, pawns, rooks, bishops, knights, queen, king
# to the power of 2 as black and white pieces

Evaluating this formula in Python (which is a good practice exercise) yields approximately 4.6×1042 positions.
The size of this number gives a rough estimate of how difficult the problem of analyzing all chess positions is.
To appreciate the size of this number, let's assume that we can analyze a trillion (1012) positions per second using our fastest computer.
At that speed, it would take roughly 1031 seconds to analyze every possible position which is approximately 10 trillion times the estimated age of the universe.

In practice, modern chess playing programs don't take this approach of trying to analyze every position.
Instead, they use more sophisticated search methods which we will discuss in more detail in a future week.
'''

import math

'''
chess solution
a = math.factorial(64)
es = math.factorial(32)
b = math.factorial(8) ** 2
c = math.factorial(2) ** 2
d = math.factorial(2) ** 2
e = math.factorial(2) ** 2
f = math.factorial(1) ** 2
g = math.factorial(1) ** 2

print a / (es * b * c * d * e * f * g)
'''


NUM_SQUARES = 9 #Tic-Tac-Toe

def count_boards(num_X, num_O):
    """
    Compute the number of positions with num_X X's
    and num_O O's
    """
    num_E = NUM_SQUARES - num_X - num_O #number of empty spaces on board
    X_fact = math.factorial(num_X)
    O_fact = math.factorial(num_O)
    E_fact = math.factorial(num_E)

    return math.factorial(NUM_SQUARES) /  \
           (X_fact * O_fact * E_fact)
    # formula is n! / (k1!, k2!, ki!)

    # e.g let's take TTT where we have 4 x's, 3 o's and 2 e's:
    # count_boards(4,3)
    # 9! / (4! * 3! * 2!)
    # 1260 possible boards with 4 x's, 3 o's and 2 e's.

def total_boards():
    """
    Compute an estimate of the number of valid
    Tic-Tac-Toe boards
    """

    total = 0
    for num in range(0, int(NUM_SQUARES / 2)):
        total += count_boards(num, num)  #X, O
        total += count_boards(num + 1, num) # X+1, O (X is starting player, can have
                                            #at most one extra place on board)

    return total

#print count_boards(4, 3)
#print total_boards()
