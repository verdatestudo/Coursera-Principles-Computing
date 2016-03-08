
'''
Word Wrangler
Principles of Computing - week 6
Student code for Word Wrangler game
2016-Mar-06
Python 2.7
Chris
'''

# maximum recursion problem as, for practice, used recursion for more functions than required by guide.
# if want to play at some point then should add functions using python in-built functions (e.g remove duplicates) to improve speed.

import urllib2
#import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"
#WORDFILE = 'http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt'


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if len(list1) == 1:
        return [list1[0]]
    elif len(list1) == 0:
        return []

    new_list = list1[:]
    if new_list[-1] == new_list[-2]:
        new_list.pop()
        return remove_duplicates(new_list)
    else:
        return remove_duplicates(new_list[0:len(new_list)-1]) + [new_list[-1]]

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """

    if len(list1) == 0 or len(list2) == 0:
        return []

    new_list1 = list1[:]
    new_list2 = list2[:]

    if new_list1[-1] > new_list2[-1]:
        new_list1.pop()
    elif new_list1[-1] < new_list2[-1]:
        new_list2.pop()
    else:
        new_list2.pop()
        return intersect(new_list1, new_list2) + [new_list1.pop()]

    return intersect(new_list1, new_list2)

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    new_list1 = list1[:]
    new_list2 = list2[:]
    answer_list = []

    while len(new_list1) > 0 and len(new_list2) > 0:
        if new_list1[-1] > new_list2[-1]:
            pop = new_list1.pop()
        else:
            pop = new_list2.pop()
        answer_list = [pop] + answer_list

    if len(new_list1) == 0:
        answer_list = new_list2 + answer_list
    elif len(new_list2) == 0:
        answer_list = new_list1 + answer_list

    return answer_list

def merge_sort(list1):
    """
    Sort the elements of list1.
    Return a new sorted list with the same elements as list1.
    This function should be recursive.
    """
    if len(list1) == 0:
        return []

    answer_list = []
    new_list = list1[:]
    if len(new_list) == 1:
        answer_list.append(new_list[0])
    else:
        mid_point = len(new_list) / 2
        left_list = merge_sort(new_list[0:mid_point])
        right_list = merge_sort(new_list[mid_point:])
        answer_list = merge(left_list, right_list)

    return answer_list

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.

    The basic idea is as follows:
    Split the input word into two parts: the first character (first) and the remaining part (rest).
    Use gen_all_strings to generate all appropriate strings for rest. Call this list rest_strings.
    For each string in rest_strings, generate new strings by inserting the initial character, first, in all possible positions
    within the string.
    Return a list containing the strings in rest_strings as well as the new strings generated in step 3.
    """

    if len(word) == 0:
        return [""]
    elif len(word) == 1:
        return ["", word]
    else:
        first_letter = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        extra_strings = []
        for string in rest_strings:
            extra_strings.append(string + first_letter)
            if len(string) > 0:
                for idx in range(len(string)):
                    extra_strings.append(string[0:idx] + first_letter + string[idx:])
    return rest_strings + extra_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """

    # if using word file locally
    answer_list = []
    with open(WORDFILE) as word_file:
        answer_list = [word.strip('\n') for word in word_file]
    return answer_list

    '''
    # if using word file from internet
    answer_list = []
    word_file = urllib2.urlopen(filename)
    for word in word_file:
        word = word.strip('\n')
        answer_list.append(word)
    return answer_list
    '''

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

def cmd_run():
    '''
    Run game in cmd line, my additional code.
    '''
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    user_word = raw_input('Enter a word: ')
    if user_word not in words:
        print 'not a word'
    else:
        wrangler.start_game(user_word)

    # NOT FINISHED


#cmd_run()
# Uncomment when you are ready to try the game
# run()
