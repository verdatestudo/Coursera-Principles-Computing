"""
Provided code for Word Wrangler game
"""

#import poc_wrangler_gui

class WordWrangler:
    """
    Game class for Word Wrangler
    """

    def __init__(self, word_list, remdup, intersect, mergesort, substrs):
        self._word_list = word_list
        self._subset_strings = []
        self._guessed_strings = []

        self._remove_duplicates = remdup
        self._intersect = intersect
        self._merge_sort = mergesort
        self._substrs = substrs

    def start_game(self, entered_word):
        """
        Start a new game of Word Wrangler
        """
        if entered_word not in self._word_list:
            print "Not a word"
            return

        strings = self._substrs(entered_word)
        sorted_strings = self._merge_sort(strings)
        all_strings = self._remove_duplicates(sorted_strings)
        self._subset_strings = self._intersect(self._word_list, all_strings)
        self._guessed_strings = []
        for word in self._subset_strings:
            self._guessed_strings.append("*" * len(word))
        self.enter_guess(entered_word)

    def enter_guess(self, guess):
        """
        Take an entered guess and update the game
        """
        if ((guess in self._subset_strings) and
            (guess not in self._guessed_strings)):
            guess_idx = self._subset_strings.index(guess)
            self._guessed_strings[guess_idx] = self._subset_strings[guess_idx]

    def peek(self, peek_index):
        """
        Exposed a word given in index into the list self._subset_strings
        """
        self.enter_guess(self._subset_strings[peek_index])

    def get_strings(self):
        """
        Return the list of strings for the GUI
        """
        return self._guessed_strings


def run_game(wrangler):
    """
    Start the game.
    """
    poc_wrangler_gui.run_gui(wrangler)
