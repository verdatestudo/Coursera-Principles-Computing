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

TEST_CASES = [(1, 1, 1), (2,3,4,5,6,7), (2, 2, 4, 8, 8, 8), (3,)]
