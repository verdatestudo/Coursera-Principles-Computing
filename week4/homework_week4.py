
import itertools
import math

'''
Principles of Computing Week 4 Homework
'''

def q1():
    '''
    Enumeration
    Given the set of outcomes corresponding to a coin flip, {Heads,Tails},
    how many sequences of outcomes of length five (repetition allowed) are possible?
    '''
    return 2 ** 5 #32

def q2():
    '''
    Probability for sequences of trials
    Consider a sequence of trials in which a fair four-sided die (with faces numbered 1-4)
    is rolled twice. What is the expected value of the product of the two
    die rolls? Enter the answer as a floating point number below.
    '''
    die_ev = (1+2+3+4) / float(4) #2.5
    return die_ev * die_ev #6.25

def q3():
    '''
    Given a trial in which a decimal digit is selected from the list
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] with equal probability 0.1,
    consider a five-digit string created by a sequence of such trials
    (leading zeros and repeated digits are allowed).
    What is the probability that this five-digit string consists of five consecutive digits
    in either ascending or descending order (e.g; "34567" or "43210") ?
    Enter your answer as a floating point number with at least four significant digits of precision.
    '''
    one_pos = 0.1 ** 5 # 0.00001
    return one_pos * 12 #12 possibilities - 6 ascend (starting with 0-5), 6 descend (starting with 4-9)

def q4():
    '''
    Permutations
    Consider a trial in which five digit strings are formed as permutations of the digits
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]. (In this case, repetition of digits is not allowed.)
    If the probability of each permutation is the same, what is the probability that this five digits
    string consists of consecutive digits in either ascending or descending order (e.g; "34567" or "43210") ?
    Enter your answer as a floating point number with at least four significant digits of precision.
    '''
    all_permutations = math.factorial(10) / math.factorial(5) # permutation equation
    return 12 / all_permutations # 12 possibilities / all possibilities

def q5():
    '''
    In this week's lectures, we discussed an iterative approach to generating all sequences
    of outcomes where repeated outcomes were allowed. Starting from this program template,
    implement a function gen_permutations(outcomes, num_trials) that takes a list of outcomes
    and a number of trials and returns a set of all possible permutations of
    length num_trials (encoded as tuples) from this list of outcomes.
    Hint: gen_permutations can be built from gen_all_sequences by adding a single if statement
    that prevents repeated outcomes. When you believe that your code works correctly,
    select the answer printed at the bottom of the console.
    '''


    """
    Function to generate permutations of outcomes
    Repetition of outcomes not allowed
    """

    def gen_permutations(outcomes, length):
        """
        Iterative function that generates set of permutations of
        outcomes of length num_trials
        No repeated outcomes allowed
        """


        ans = set([()])
        for dummy_idx in range(length):
            temp = set()
            for seq in ans:
                for item in outcomes:
                    if item in seq:
                        continue
                    else:
                        new_seq = list(seq)
                        new_seq.append(item)
                        temp.add(tuple(new_seq))
            ans = temp
        return ans



    def run_example():

        # example for digits
        outcome = [0, 1, 2, 3]
        #outcome = ["Red", "Green", "Blue"]
        #outcome = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        length = 2
        permtutations = gen_permutations(outcome, length)
        print "Computed", len(permtutations), "permutations of length", str(length)
        print "Permutations were", permtutations

    #run_example()

    #######################################
    # Example output below
    #
    #Computed 90 permutations of length 2
    #Permutations were set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (5, 7), (5, 8), (5, 9), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (6, 8), (6, 9), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 8), (7, 9), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 9), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8)])#
    #
    #Computed 6 permutations of length 2
    #Permutations were set([('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Red'), ('Green', 'Blue'), ('Blue', 'Red'), ('Blue', 'Green')])
    #
    #Computed 210 permutations of length 3
    #Permutations were set([('Sunday', 'Monday', 'Tuesday'), ('Sunday', 'Monday', 'Wednesday'), ('Sunday', 'Monday', 'Thursday'), ('Sunday', 'Monday', 'Friday'), ('Sunday', 'Monday', 'Saturday'), ('Sunday', 'Tuesday', 'Monday'), ('Sunday', 'Tuesday', 'Wednesday'), ('Sunday', 'Tuesday', 'Thursday'), ('Sunday', 'Tuesday', 'Friday'), ('Sunday', 'Tuesday', 'Saturday'), ('Sunday', 'Wednesday', 'Monday'), ('Sunday', 'Wednesday', 'Tuesday'), ('Sunday', 'Wednesday', 'Thursday'), ('Sunday', 'Wednesday', 'Friday'), ('Sunday', 'Wednesday', 'Saturday'), ('Sunday', 'Thursday', 'Monday'), ('Sunday', 'Thursday', 'Tuesday'), ('Sunday', 'Thursday', 'Wednesday'), ('Sunday', 'Thursday', 'Friday'), ('Sunday', 'Thursday', 'Saturday'), ('Sunday', 'Friday', 'Monday'), ('Sunday', 'Friday', 'Tuesday'), ('Sunday', 'Friday', 'Wednesday'), ('Sunday', 'Friday', 'Thursday'), ('Sunday', 'Friday', 'Saturday'), ('Sunday', 'Saturday', 'Monday'), ('Sunday', 'Saturday', 'Tuesday'), ('Sunday', 'Saturday', 'Wednesday'), ('Sunday', 'Saturday', 'Thursday'), ('Sunday', 'Saturday', 'Friday'), ('Monday', 'Sunday', 'Tuesday'), ('Monday', 'Sunday', 'Wednesday'), ('Monday', 'Sunday', 'Thursday'), ('Monday', 'Sunday', 'Friday'), ('Monday', 'Sunday', 'Saturday'), ('Monday', 'Tuesday', 'Sunday'), ('Monday', 'Tuesday', 'Wednesday'), ('Monday', 'Tuesday', 'Thursday'), ('Monday', 'Tuesday', 'Friday'), ('Monday', 'Tuesday', 'Saturday'), ('Monday', 'Wednesday', 'Sunday'), ('Monday', 'Wednesday', 'Tuesday'), ('Monday', 'Wednesday', 'Thursday'), ('Monday', 'Wednesday', 'Friday'), ('Monday', 'Wednesday', 'Saturday'), ('Monday', 'Thursday', 'Sunday'), ('Monday', 'Thursday', 'Tuesday'), ('Monday', 'Thursday', 'Wednesday'), ('Monday', 'Thursday', 'Friday'), ('Monday', 'Thursday', 'Saturday'), ('Monday', 'Friday', 'Sunday'), ('Monday', 'Friday', 'Tuesday'), ('Monday', 'Friday', 'Wednesday'), ('Monday', 'Friday', 'Thursday'), ('Monday', 'Friday', 'Saturday'), ('Monday', 'Saturday', 'Sunday'), ('Monday', 'Saturday', 'Tuesday'), ('Monday', 'Saturday', 'Wednesday'), ('Monday', 'Saturday', 'Thursday'), ('Monday', 'Saturday', 'Friday'), ('Tuesday', 'Sunday', 'Monday'), ('Tuesday', 'Sunday', 'Wednesday'), ('Tuesday', 'Sunday', 'Thursday'), ('Tuesday', 'Sunday', 'Friday'), ('Tuesday', 'Sunday', 'Saturday'), ('Tuesday', 'Monday', 'Sunday'), ('Tuesday', 'Monday', 'Wednesday'), ('Tuesday', 'Monday', 'Thursday'), ('Tuesday', 'Monday', 'Friday'), ('Tuesday', 'Monday', 'Saturday'), ('Tuesday', 'Wednesday', 'Sunday'), ('Tuesday', 'Wednesday', 'Monday'), ('Tuesday', 'Wednesday', 'Thursday'), ('Tuesday', 'Wednesday', 'Friday'), ('Tuesday', 'Wednesday', 'Saturday'), ('Tuesday', 'Thursday', 'Sunday'), ('Tuesday', 'Thursday', 'Monday'), ('Tuesday', 'Thursday', 'Wednesday'), ('Tuesday', 'Thursday', 'Friday'), ('Tuesday', 'Thursday', 'Saturday'), ('Tuesday', 'Friday', 'Sunday'), ('Tuesday', 'Friday', 'Monday'), ('Tuesday', 'Friday', 'Wednesday'), ('Tuesday', 'Friday', 'Thursday'), ('Tuesday', 'Friday', 'Saturday'), ('Tuesday', 'Saturday', 'Sunday'), ('Tuesday', 'Saturday', 'Monday'), ('Tuesday', 'Saturday', 'Wednesday'), ('Tuesday', 'Saturday', 'Thursday'), ('Tuesday', 'Saturday', 'Friday'), ('Wednesday', 'Sunday', 'Monday'), ('Wednesday', 'Sunday', 'Tuesday'), ('Wednesday', 'Sunday', 'Thursday'), ('Wednesday', 'Sunday', 'Friday'), ('Wednesday', 'Sunday', 'Saturday'), ('Wednesday', 'Monday', 'Sunday'), ('Wednesday', 'Monday', 'Tuesday'), ('Wednesday', 'Monday', 'Thursday'), ('Wednesday', 'Monday', 'Friday'), ('Wednesday', 'Monday', 'Saturday'), ('Wednesday', 'Tuesday', 'Sunday'), ('Wednesday', 'Tuesday', 'Monday'), ('Wednesday', 'Tuesday', 'Thursday'), ('Wednesday', 'Tuesday', 'Friday'), ('Wednesday', 'Tuesday', 'Saturday'), ('Wednesday', 'Thursday', 'Sunday'), ('Wednesday', 'Thursday', 'Monday'), ('Wednesday', 'Thursday', 'Tuesday'), ('Wednesday', 'Thursday', 'Friday'), ('Wednesday', 'Thursday', 'Saturday'), ('Wednesday', 'Friday', 'Sunday'), ('Wednesday', 'Friday', 'Monday'), ('Wednesday', 'Friday', 'Tuesday'), ('Wednesday', 'Friday', 'Thursday'), ('Wednesday', 'Friday', 'Saturday'), ('Wednesday', 'Saturday', 'Sunday'), ('Wednesday', 'Saturday', 'Monday'), ('Wednesday', 'Saturday', 'Tuesday'), ('Wednesday', 'Saturday', 'Thursday'), ('Wednesday', 'Saturday', 'Friday'), ('Thursday', 'Sunday', 'Monday'), ('Thursday', 'Sunday', 'Tuesday'), ('Thursday', 'Sunday', 'Wednesday'), ('Thursday', 'Sunday', 'Friday'), ('Thursday', 'Sunday', 'Saturday'), ('Thursday', 'Monday', 'Sunday'), ('Thursday', 'Monday', 'Tuesday'), ('Thursday', 'Monday', 'Wednesday'), ('Thursday', 'Monday', 'Friday'), ('Thursday', 'Monday', 'Saturday'), ('Thursday', 'Tuesday', 'Sunday'), ('Thursday', 'Tuesday', 'Monday'), ('Thursday', 'Tuesday', 'Wednesday'), ('Thursday', 'Tuesday', 'Friday'), ('Thursday', 'Tuesday', 'Saturday'), ('Thursday', 'Wednesday', 'Sunday'), ('Thursday', 'Wednesday', 'Monday'), ('Thursday', 'Wednesday', 'Tuesday'), ('Thursday', 'Wednesday', 'Friday'), ('Thursday', 'Wednesday', 'Saturday'), ('Thursday', 'Friday', 'Sunday'), ('Thursday', 'Friday', 'Monday'), ('Thursday', 'Friday', 'Tuesday'), ('Thursday', 'Friday', 'Wednesday'), ('Thursday', 'Friday', 'Saturday'), ('Thursday', 'Saturday', 'Sunday'), ('Thursday', 'Saturday', 'Monday'), ('Thursday', 'Saturday', 'Tuesday'), ('Thursday', 'Saturday', 'Wednesday'), ('Thursday', 'Saturday', 'Friday'), ('Friday', 'Sunday', 'Monday'), ('Friday', 'Sunday', 'Tuesday'), ('Friday', 'Sunday', 'Wednesday'), ('Friday', 'Sunday', 'Thursday'), ('Friday', 'Sunday', 'Saturday'), ('Friday', 'Monday', 'Sunday'), ('Friday', 'Monday', 'Tuesday'), ('Friday', 'Monday', 'Wednesday'), ('Friday', 'Monday', 'Thursday'), ('Friday', 'Monday', 'Saturday'), ('Friday', 'Tuesday', 'Sunday'), ('Friday', 'Tuesday', 'Monday'), ('Friday', 'Tuesday', 'Wednesday'), ('Friday', 'Tuesday', 'Thursday'), ('Friday', 'Tuesday', 'Saturday'), ('Friday', 'Wednesday', 'Sunday'), ('Friday', 'Wednesday', 'Monday'), ('Friday', 'Wednesday', 'Tuesday'), ('Friday', 'Wednesday', 'Thursday'), ('Friday', 'Wednesday', 'Saturday'), ('Friday', 'Thursday', 'Sunday'), ('Friday', 'Thursday', 'Monday'), ('Friday', 'Thursday', 'Tuesday'), ('Friday', 'Thursday', 'Wednesday'), ('Friday', 'Thursday', 'Saturday'), ('Friday', 'Saturday', 'Sunday'), ('Friday', 'Saturday', 'Monday'), ('Friday', 'Saturday', 'Tuesday'), ('Friday', 'Saturday', 'Wednesday'), ('Friday', 'Saturday', 'Thursday'), ('Saturday', 'Sunday', 'Monday'), ('Saturday', 'Sunday', 'Tuesday'), ('Saturday', 'Sunday', 'Wednesday'), ('Saturday', 'Sunday', 'Thursday'), ('Saturday', 'Sunday', 'Friday'), ('Saturday', 'Monday', 'Sunday'), ('Saturday', 'Monday', 'Tuesday'), ('Saturday', 'Monday', 'Wednesday'), ('Saturday', 'Monday', 'Thursday'), ('Saturday', 'Monday', 'Friday'), ('Saturday', 'Tuesday', 'Sunday'), ('Saturday', 'Tuesday', 'Monday'), ('Saturday', 'Tuesday', 'Wednesday'), ('Saturday', 'Tuesday', 'Thursday'), ('Saturday', 'Tuesday', 'Friday'), ('Saturday', 'Wednesday', 'Sunday'), ('Saturday', 'Wednesday', 'Monday'), ('Saturday', 'Wednesday', 'Tuesday'), ('Saturday', 'Wednesday', 'Thursday'), ('Saturday', 'Wednesday', 'Friday'), ('Saturday', 'Thursday', 'Sunday'), ('Saturday', 'Thursday', 'Monday'), ('Saturday', 'Thursday', 'Tuesday'), ('Saturday', 'Thursday', 'Wednesday'), ('Saturday', 'Thursday', 'Friday'), ('Saturday', 'Friday', 'Sunday'), ('Saturday', 'Friday', 'Monday'), ('Saturday', 'Friday', 'Tuesday'), ('Saturday', 'Friday', 'Wednesday'), ('Saturday', 'Friday', 'Thursday')])

    ## Final example for homework problem
    #
    outcome = set(["a", "b", "c", "d", "e", "f"])
    #
    permutations = gen_permutations(outcome, 4)
    permutation_list = list(permutations)
    permutation_list.sort()
    print
    print "Answer is", permutation_list[100]


def q6():
    '''
    Subsets
    A set S is a subset of another set T (mathematically denoted as S⊆T) if every element x in S
    (mathematically denoted as x∈S) is also a member of T.
    Which of the following sets are subsets of the set {1,2}?

    # options = (1, 2, 3, 4), (1, 2), (), (1), (3,4)
    # answers = (1,2), (), (1)
    '''
    pass

def q7(n):
    '''
    If the set T has n members, how many distinct sets S are subsets of T?
    You may want to figure out the answer for a few specific values of n first.
    Enter the answer below as a math expression in n.
    '''
    return 2 ** n

def q8():
    '''
    Combinations
    Given a standard 52 card deck of playing cards, what is the probability of being dealt
    a five card hand where all five cards are of the same suit?
    Hint: Use the formula for combinations to compute the number of possible five card hands
    when the choice of cards is restricted to a single suit versus when the choice of cards is unrestricted.
    Compute your answer in Python using math.factorial and enter the answer below as a floating
    point number with at least four significant digits of precision.
    '''
    # flush - q8 #1st way to calc
    print (12 / float(51)) * \
    (11 / float(50)) * \
    (10 / float(49)) * \
    (9 / float(48))

    # q8 second way to count
    a = math.factorial(13) / (math.factorial(8) * math.factorial(5)) * 4 # number of possible flushes
    b = math.factorial(52) / (math.factorial(47) * math.factorial(5)) # number of possible 52 card hands combinations
    return a / float(b)


def q9():
    '''
    Pascal's triangle is a triangular array of numbers in which the entry on one row of the triangle
    corresponds to the sum of the two entries directly above the entry.
    This program prints out the first few rows of Pascal's triangle.
    Enter a math expression in m and n using factorial (!) that represents the value of the nth entry
    of the mth row of Pascal's triangle. (Both the row numbers and entry numbers are indexed starting at zero.)
    '''
    pascal_factor_size = 6
    for z in range(pascal_factor_size):
        for x in range(pascal_factor_size):
            if x <= z:
                print z, x, ' is ', pascal_factor(z, x)

def pascal_factor(m, n):

    top = math.factorial(m)
    bot = math.factorial(n) * math.factorial((m)-(n))
    return top / bot


def q10():
    '''
    See merge testing practice activity from week 2
    '''
    pass
