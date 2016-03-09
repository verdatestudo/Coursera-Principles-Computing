"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level

2016-Jan-31
Python 2.7
Chris
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import random

# DO NOT modify
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    # list count each 1-6
    # multiply
    # return max
    possible_scores = [(hand.count(xyz) * xyz) for xyz in range(1, 7)]
    return max(possible_scores)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    all_dice = [x for x in range(1, num_die_sides+1)]
    all_seq = gen_all_sequences(tuple(all_dice), num_free_dice)
    final_seq = [held_dice + item for item in all_seq]
    total_list = []
    for seq in final_seq:
        new_vals = [seq.count(xxx) * xxx for xxx in range(1,num_die_sides+1)]
        total_list.append(max(new_vals))
    return sum(total_list) / float(len(total_list))
    #return final_seq

    # need to return EV
    # total score (add all items in final_seq) / len(final_seq)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_hold_seq = set([])
    # can only have 3 1's, 1 FIVE and 1 SIX
    #for xxx in range(0, len(hand)+1):
    for xxx in range(0, len(hand)+1):
        all_hold_seq.update(gen_all_limit_seq(hand, xxx))
    return all_hold_seq

    # use total count board formula to check len(all_hold_seq) is right


def gen_all_limit_seq(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                if partial_sequence.count(item) < outcomes.count(item):
                    new_sequence = list(partial_sequence)
                    new_sequence.append(item)
                    new_sequence.sort()
                    temp_set.add(tuple(new_sequence))
        answer_set = sorted(temp_set)
    return answer_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_combos = gen_all_holds(hand)
    best_ev = 0
    best_combo = None
    for combo in all_combos:
        temp_ev = expected_value(combo, num_die_sides, len(hand)-len(combo))  # need to re-roll all dice to get 3.5
        if temp_ev > best_ev:
            best_ev = temp_ev
            best_combo = combo
    return (best_ev, best_combo)
    # full hand
    # all possible permutations, holding 0 to 5 dice
    # calculate EV for each of these
    # return below values

    # return TUPLE of max EV and SORTED TUPLE of best die to hold
    # if more than one max, return random.choice



def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """

    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

#print strategy((1,), 6), 'expected (3.5, ())'
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
