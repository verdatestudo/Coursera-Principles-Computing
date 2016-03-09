"""
Analyzing a simple dice game
"""


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """

    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

# example for digits


def max_repeats(seq):
    """
    Compute the maximum number of times that an outcome is repeated
    in a sequence
    """
    #max_repeat = 0
    #return max([seq.count(item) for item in seq if seq.count(item) > max_repeat])
    return max([seq.count(item) for item in seq])

def compute_expected_value(outcomes, rolls):
    """
    Function to compute expected value of simple dice game
    """
    # set $ value for single, double and triple dice roll
    value_roll = {1: 0, 2: 10, 3: 200}
    # all possible sequences of roll
    all_seq = gen_all_sequences(outcomes, rolls)

    # for each possible dice roll, see if it's 1, 2, 3 and multiply by value of roll
    total = 0
    for seq in all_seq:
        total += value_roll[max_repeats(seq)]

    # EV = total value / number of possibilities
    return round(total / float(len(all_seq)), 2)

def run_test():
    """
    Testing code, note that the initial cost of playing the game
    has been subtracted
    """
    outcomes = set([1, 2, 3, 4, 5, 6])
    print "All possible sequences of three dice are"
    print len(gen_all_sequences(outcomes, 3))
    print gen_all_sequences(outcomes, 3)
    print
    print "Test for max repeats"
    print "Max repeat for (3, 1, 2) is", max_repeats((3, 1, 2))
    print "Max repeat for (3, 3, 2) is", max_repeats((3, 3, 2))
    print "Max repeat for (3, 3, 3) is", max_repeats((3, 3, 3))
    print
    print "Ignoring the initial $10, the expected value was $", compute_expected_value(outcomes, 3)

run_test()
