"""
Principles of Computing - Week 9
Loyd's Fifteen puzzle - solver and visualizer

2016-Mar-23
Python 2.7
Chris

Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

#import poc_fifteen_gui
import random

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean

        Tile zero is positioned at (i,j).
        All tiles in rows i+1 or below are positioned at their solved location.
        All tiles in row i to the right of position (i,j) are positioned at their solved location.
        """
        if self.get_number(target_row, target_col) != 0:
            print "error 1"
            return False

        for row in range(target_row + 1, self.get_height()):
            for col in range(self.get_width()):
                predicted_cell_value = (row * self.get_width()) + col
                if predicted_cell_value != self.get_number(row, col):
                    print "error 2"
                    return False

        for col in range(target_col + 1, self.get_width()):
            predicted_cell_value = (target_row * self.get_width()) + col
            if predicted_cell_value != self.get_number(target_row, col):
                print "error 3"
                return False

        return True

    def _move_zero_to_start_pos(self):
        '''
        Move zero to the starting position in the bottom right of board
        '''
        move_string = ''
        zero_tile_target_pos = (self.get_height() - 1, self.get_width() - 1)
        move_string += 'd' * (zero_tile_target_pos[0] - self.current_position(0, 0)[0])
        move_string += 'r' * (zero_tile_target_pos[1] - self.current_position(0, 0)[1])

        self.update_puzzle(move_string)
        return move_string


    def hit_target_with_zero(self, target_tile_cur_pos, target_tile_end_pos):
        '''
        Helper function
        Moves the zero tile until it "hits" the target tile
        '''
        move_string = ''
        # move up to target tile row
        for _ in range(target_tile_end_pos[0] - target_tile_cur_pos[0]):
            move_string += "u"

        # then go left or right until we hit it.
        left_right_move = target_tile_cur_pos[1] - target_tile_end_pos[1]
        if left_right_move > 0:
            for _ in range(left_right_move):
                move_string += "r"
        elif left_right_move < 0:
            for _ in range(abs(left_right_move)):
                move_string += "l"

        self.update_puzzle(move_string)
        return move_string


    def put_target_in_temp_col(self, target_tile_end_pos, temp_target_end_pos):
        '''
        Helper function
        Move the target tile until it's in the correct column
        Note: this is used to move a target into a TEMP correct column, not the final column needed
        '''
        move_string = ''

        # while the current position of target tile is to the right of temp target
        while self.current_position(target_tile_end_pos[0], target_tile_end_pos[1])[1] > temp_target_end_pos[1]:
            if self.current_position(0, 0)[0] > 0: # we try to go up first, but obviously must go down at row 0
                next_move = 'ulldr'
            else:
                next_move = 'dllur'
            move_string += next_move
            self.update_puzzle(next_move)

        # while the current position of target tile is to the left of temp target
        while self.current_position(target_tile_end_pos[0], target_tile_end_pos[1])[1] < temp_target_end_pos[1]:
            if self.current_position(0, 0)[0] > 0:
                next_move = 'urrdl'
            else:
                next_move = 'drrul'
            move_string += next_move
            self.update_puzzle(next_move)

        return move_string

    def put_target_in_col(self, target_tile_end_pos):
        '''
        Helper function
        Move the target tile until it's in the correct column
        '''
        move_string = ''
        # check if target tile is in the correct column.
        while self.current_position(target_tile_end_pos[0], target_tile_end_pos[1])[1] < target_tile_end_pos[1]: # if target tile is too far left
            if self.current_position(0, 0)[0] > 0:
                next_move = 'urrdl'
            else:
                next_move = 'drrul'
            move_string += next_move
            self.update_puzzle(next_move)

        while self.current_position(target_tile_end_pos[0], target_tile_end_pos[1])[1] > target_tile_end_pos[1]: #if target tile is too far right
            if self.current_position(0, 0)[0] > 0:
                next_move = 'ulldr'
            else:
                next_move = 'dllur'
            move_string += next_move
            self.update_puzzle(next_move)

        return move_string

    def get_final_seq(self, target_tile_cur_pos, target_tile_end_pos, target_row_col, if_temp_target = None):
        '''
        Helper function
        Target tile has been "hit" and is in the correct column.
        This function now moves it into the correct final position.
        '''
        move_string = ''

        # once zero hits target, we have three possibilities
        if self.current_position(0, 0)[1] == (target_tile_cur_pos[1] - 1): # if zero is to the left
            seq_string = 'druld'
        elif self.current_position(0, 0)[0] == (target_tile_cur_pos[0] - 1): # if zero is above
            seq_string = 'lddru'
        elif self.current_position(0, 0)[1] == (target_tile_cur_pos[1] + 1): # if zero is to the right
            if self.current_position(0, 0)[0] != 0: # try up first to avoid messing up solved squares. places zero above.
                next_move = 'ul'
            else:
                next_move = 'dlu'
            move_string += next_move
            self.update_puzzle(next_move)
            seq_string = 'lddru'
        else:
            print 'possible error!'

        if if_temp_target != None:
            count = 0
            # cycle through the seq string until both the target tile and the zero tile are in their correct places.
            # if we have a temp target, get there first
            while target_tile_end_pos != self.current_position(if_temp_target[0], if_temp_target[1]) or self.current_position(0, 0) != (target_row_col[0], target_row_col[1] - 1):
                next_move = seq_string[count % len(seq_string)]
                self.update_puzzle(next_move)
                move_string += next_move
                count += 1

            return move_string

        count = 0
        # cycle through the seq string until both the target tile and the zero tile are in their correct places.
        while target_tile_end_pos != self.current_position(target_row_col[0], target_row_col[1]) or self.current_position(0, 0) != (target_row_col[0], target_row_col[1] - 1):
            next_move = seq_string[count % len(seq_string)]
            self.update_puzzle(next_move)
            move_string += next_move
            count += 1

        return move_string

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string

        The method solve_interior_tile(i, j) is designed to solve the puzzle at position (i,j) where i>1 and j>0.
        Specifically, this method takes a puzzle for which lower_row_invariant(i, j) is true and repositions
        the tiles in the puzzle such that lower_row_invariant(i, j - 1) is true.
        To implement solve_interior_tile, we suggest that you review problem #8 on the homework.

        Question 8
        Implementing solve_interior_tile
        We are now ready to formulate the basic algorithm for solve_interior_tile(i, j).
        Given a target position (i,j), we start by finding the current position of the tile that should appear at this position to a solved puzzle.
        We refer to this tile as the target tile.

        While moving the target tile to the target position, we can leverage the fact that lower_row_invariant(i, j) is true prior
        to execution of solve_interior_tile(i, j).
        First, we know that the zero tile is positioned at (i,j).
        Also, the target tile's current position (k,l) must be either above the target position (k<i) or on the same row to the left (i=k and l<j).

        Our solution strategy will be to move the zero tile up and across to the target tile.

        Then we will move the target tile back to the target position by applying a series of cyclic moves to the zero tile that move the target tile
        back to the target position one position at a time.

        Our implementation of this strategy will have three cases depending on the relative horizontal positions of the zero tile and the target tile.
        The three images below show an example in which the target tile (with number 13) is directly above the target position.
        The left image shows the configuration at the start of solve_interior_tile(3, 1), the middle image shows the configuration after
        the zero tile has been moved to the target tile's current position using the move string "uuu",
        and the right image shows the configuration after the target tile has been moved down one position towards the target position using the move string "lddru".
        """
        assert self.lower_row_invariant(target_row, target_col)

        move_string = ""
        target_tile_end_pos = (target_row, target_col)
        temp_board = self.clone()

        move_string += temp_board.hit_target_with_zero(temp_board.current_position(target_row, target_col), target_tile_end_pos)

        move_string += temp_board.put_target_in_col(target_tile_end_pos)

        move_string += temp_board.get_final_seq(temp_board.current_position(target_row, target_col), target_tile_end_pos, (target_row, target_col))

        self.update_puzzle(move_string)
        assert self.lower_row_invariant(target_row, target_col - 1)
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string

        The second solution method solve_col0_tile(i) is designed to solve the puzzle at position (i,0) where i>1.
        Specifically, this method takes a puzzle that satisfies the invariant lower_row_invariant(i, 0) and repositions the tiles in the puzzle
        such that lower_row_invariant(i - 1, n - 1) is true where n is the width of the grid.
        Implementing solve_col0_tile is trickier than solve_interior_tile since the solution strategy for solve_interior_tile(i, j) involved moving tile zero through column j-1.
        In the case of the left column where j=0, this solution process is not feasible.

        Our recommended strategy for solve_col0_tile is to move the zero tile from (i,0) to (i-1,1) using the move string "ur".
        If you are lucky and the target tile (i.e, the tile being solved for) is now at position (i,0), you can simply move tile
        zero to the end of row i-1 and be done.
        However, if the target tile is not positioned at (i,0), we suggest the following solution strategy:

        Reposition the target tile to position (i-1,1) and the zero tile to position (i-1,0) using a process similar to that of solve_interior_tile,
        Then apply the move string for a 3x2 puzzle as described in problem #9 of the homework to bring the target tile into position (i,0),

        Finally, conclude by moving tile zero to the right end of row i-1.

        Note the process for the first step is so similar to that of solve_interior_tile that you may wish to refactor your
        implementation to include a helper method position_tile that is used by both tasks.

        Note that the invariant method lower_row_invariant can be extremely valuable as you test and debug
        solve_interior_tile and solve_col0_tile.
        Minimally, we recommend that you add assert statements to your solution methods that verify that these methods
        are receiving a puzzle in a proper input configuration and producing a puzzle with the proper output configuration.

        Once you are confident that these methods are correct, use OwlTest to confirm that they are correct.
        """
        assert self.lower_row_invariant(target_row, 0)

        move_string = ""
        target_tile_end_pos = (target_row, 0)

        next_move = 'ur'
        move_string += next_move
        self.update_puzzle(next_move)

        if self.current_position(target_row, 0) == target_tile_end_pos:
            for _ in range(self.get_width() - 2):
                next_move = 'r'
                move_string += next_move
                self.update_puzzle(next_move)
            assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
            return move_string
        else:
            temp_target = (target_tile_end_pos[0] - 1, 1)

        move_string += self.hit_target_with_zero(self.current_position(target_row, 0), self.current_position(0, 0))
        move_string += self.put_target_in_temp_col(target_tile_end_pos, temp_target)
        move_string += self.get_final_seq(self.current_position(target_row, 0), temp_target, temp_target, target_tile_end_pos)

        seq_string = "ruldrdlurdluurddlur"

        count = 0
        while self.current_position(target_row, 0) != target_tile_end_pos:
            next_move = seq_string[count]
            self.update_puzzle(next_move)
            move_string += next_move
            count += 1

        while self.current_position(0, 0) != (target_tile_end_pos[0] - 1, self.get_width() - 1):
            next_move = 'r'
            self.update_puzzle(next_move)
            move_string += next_move

        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1)
        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean

        The invariant row0_invariant(j) checks a similar condition,
        but additionally checks whether position (1,j) is also solved.

        Tile zero is positioned at (0,j).
        All tiles in rows 2 or below are positioned at their solved location.
        All tiles in row 1 to the right of position (1,j) are positioned at their solved location.
        All tiles in row 0 to the right of position (0,j) are positioned at their solved location.
        """
        if self.get_number(0, target_col) != 0:
            print "error 1"
            return False

        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                predicted_cell_value = (row * self.get_width()) + col
                if predicted_cell_value != self.get_number(row, col):
                    print "error 2"
                    return False

        for col in range(target_col + 1, self.get_width()):
            predicted_cell_value = (0 * self.get_width()) + col
            if predicted_cell_value != self.get_number(0, col):
                print "error 3"
                return False

        for col in range(target_col, self.get_width()):
            predicted_cell_value = (1 * self.get_width()) + col
            if predicted_cell_value != self.get_number(1, col):
                print "error 4"
                return False

        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean

        The invariant row1_invariant(j) should check whether tile zero is at (1,j)
        and whether all positions either below or to the right of this position are solved.

        Tile zero is positioned at (1,j).
        All tiles in rows 2 or below are positioned at their solved location.
        All tiles in row 1 to the right of position (1,j) are positioned at their solved location.
        """
        if self.get_number(1, target_col) != 0:
            print "error 1"
            return False

        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                predicted_cell_value = (row * self.get_width()) + col
                if predicted_cell_value != self.get_number(row, col):
                    print "error 2"
                    return False

        for col in range(target_col + 1, self.get_width()):
            predicted_cell_value = (1 * self.get_width()) + col
            if predicted_cell_value != self.get_number(1, col):
                print "error 3"
                return False

        return True


    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string

        To implement solve_row0_tile(j), we suggest that you use a method similar to that for solve_col0_tile.
        In particular, you should move the zero tile from position (0,j) to (1,j-1) using the move string "ld" and check whether target tile is at position (0,j).
        If not, reposition the target tile to position (1,j-1) with tile zero in position (1,j-2).
        At this point, you can apply the move string from problem 10 in the homework to complete the method.
        """
        assert self.row0_invariant(target_col)

        move_string = ''
        target_tile_end_pos = (0, target_col)

        next_move = 'ld'
        move_string += next_move
        self.update_puzzle(next_move)

        if self.current_position(0, target_col) == target_tile_end_pos:
            assert self.lower_row_invariant(1, target_tile_end_pos[1] - 1)
            return move_string
        else:
            temp_target = (1, target_tile_end_pos[1] - 1)

        move_string += self.hit_target_with_zero(self.current_position(0, target_col), temp_target)
        move_string += self.put_target_in_temp_col((0, target_col), temp_target)
        move_string += self.get_final_seq(self.current_position(0, target_col), temp_target, temp_target, target_tile_end_pos)

        seq_string = "urdlurrdluldrruld"

        count = 0
        while self.current_position(0, target_col) != target_tile_end_pos:
            next_move = seq_string[count]
            self.update_puzzle(next_move)
            move_string += next_move
            count += 1

        next_move = 'd'
        self.update_puzzle(next_move)
        move_string += next_move

        assert self.row1_invariant(target_col - 1)
        return move_string


    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row1_invariant(target_col)

        move_string = ""
        target_tile_end_pos = (1, target_col)

        move_string += self.hit_target_with_zero(self.current_position(1, target_col), target_tile_end_pos)
        move_string += self.put_target_in_col(target_tile_end_pos)
        move_string += self.get_final_seq(self.current_position(1, target_col), target_tile_end_pos, (1, target_col))

        next_move = 'ur'
        move_string += next_move # move zero above
        self.update_puzzle(next_move)

        assert self.row0_invariant(target_col)
        return move_string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string

        The method solve_2x2() solves the final upper left 2x2 portion of the puzzle under the assumption that the remainder of the puzzle is solved (i.e, row1_invariant(1) is true).
        When building test cases for your solver, note that not all puzzles generated by random placement of the tiles can be solved.
        """
        assert self.row1_invariant(1)

        move_string = ''
        seq_string = 'lurd'
        tile_one_zero = self.get_width()
        tile_one_one = tile_one_zero + 1

        count = 0

        # if tiles aren't correct, keep cycling through the sequence.

        while self.get_number(0, 0) != 0 or self.get_number(0, 1) != 1 or self.get_number(1, 0) != tile_one_zero or self.get_number(1, 1) != tile_one_one:
            next_move = seq_string[count % len(seq_string)]
            self.update_puzzle(next_move)
            move_string += next_move
            count += 1
            if count > 20:
                print "solution not found"
                return move_string

        # check all tiles are in the right place.
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                predicted_cell_value = (row * self.get_width()) + col
                if predicted_cell_value != self.get_number(row, col):
                    print "error"
                    return False

        return move_string


    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string

        The final method solve_puzzle() takes a solvable Puzzle object and solves the puzzle.
        This method should call the various solution methods that you have implemented and
        join the move string returned by these methods to form a single move string that solves the entire puzzle.

        First - do all cols (except 0) in the bottom row, starting with bottom right.
        Second - do col 0 for bottom row.
        Third - repeat for all rows below 2
        Fourth - do row1, last col. then row0, last col. then row1, last col -1 and so on.
        Fifth - solve 2x2 grid in top left (if possible)
        """
        move_string = self._move_zero_to_start_pos()
        for row in range(self.get_height() - 1, 1, -1):
            for col in range(self.get_width() - 1, 0, -1):
                move_string += self.solve_interior_tile(row, col)
            move_string += self.solve_col0_tile(row)

        for col in range(self.get_width() - 1, 1, -1):
            move_string += self.solve_row1_tile(col)
            move_string += self.solve_row0_tile(col)

        move_string += self.solve_2x2()

        return move_string


def test_lower_row_invariant():
    '''
    Test Function
    '''
    obj = Puzzle(3, 3, [[3, 2, 1], [4, 5, 0], [6, 7, 8]])
    print obj.lower_row_invariant(1, 2), 'True'
    obj = Puzzle(3, 3, [[3, 2, 1], [4, 5, 0], [7, 6, 8]])
    print obj.lower_row_invariant(1, 2), 'False'
    obj = Puzzle(4, 4, [[3, 2, 1, 4], [5, 4, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print obj.lower_row_invariant(1, 2), 'True'
    obj = Puzzle(4, 4, [[3, 2, 1, 4], [5, 4, 10, 8], [7, 0, 9, 11], [12, 13, 14, 15]])
    print obj.lower_row_invariant(2, 1), 'False'

def test_solve_interior_tile():
    '''
    Test Function
    '''

    obj = Puzzle(3, 3, [[7, 5, 6], [4, 2, 1], [3, 0, 8]])
    print 'Start pos'
    print obj
    obj.solve_interior_tile(2, 1)
    print 'End pos'
    print obj

    obj = Puzzle(3, 3, [[5, 7, 6], [4, 2, 1], [3, 0, 8]])
    print 'Start pos'
    print obj
    obj.solve_interior_tile(2, 1)
    print 'End pos'
    print obj

    obj = Puzzle(3, 3, [[5, 6, 7], [4, 2, 1], [3, 0, 8]])
    print 'Start pos'
    print obj
    obj.solve_interior_tile(2, 1)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[4, 2, 3, 13], [8, 5, 6, 10], [9, 1, 7, 11], [12, 0, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_interior_tile(3, 1)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[15, 2, 4, 7], [8, 5, 6, 10], [9, 1, 3, 11], [12, 13, 14, 0]])
    print 'Start pos'
    print obj
    obj.solve_interior_tile(3, 3)
    print 'End pos'
    print obj


def test_solve_col0_tile():
    '''
    Test Function
    '''

    obj = Puzzle(3, 3, [[6, 5, 3], [4, 2, 1], [0, 7, 8]])
    print 'Start pos'
    print obj
    obj.solve_col0_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(3, 3, [[3, 5, 6], [4, 2, 1], [0, 7, 8]])
    print 'Start pos'
    print obj
    obj.solve_col0_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[6, 5, 3, 8], [4, 2, 1, 7], [0, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_col0_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[6, 5, 3, 8], [7, 2, 1, 12], [4, 9, 10, 11], [0, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_col0_tile(3)
    print 'End pos'
    print obj


def testing_row_invariants():
    '''
    Test Function
    '''
    obj = Puzzle(4, 4, [[4, 6, 1, 3], [5, 2, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print obj.row1_invariant(2), 'True'

    obj = Puzzle(4, 4, [[5, 4, 1, 3], [6, 2, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print obj.row1_invariant(2), 'True'

    obj = Puzzle(4, 4, [[7, 4, 1, 3], [6, 2, 5, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    print obj.row1_invariant(3), 'True'

    obj = Puzzle(4, 4, [[4, 6, 1, 3], [7, 2, 0, 5], [8, 9, 10, 11], [12, 13, 14, 15]])
    print obj.row1_invariant(2), 'False'

    obj = Puzzle(4, 4, [[4, 6, 1, 3], [5, 2, 0, 7], [9, 8, 10, 11], [12, 13, 14, 15]])
    print obj.row1_invariant(2), 'False'

    obj = Puzzle(4, 4, [[4, 2, 0, 3], [5, 1, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print obj.row0_invariant(2), 'True'

    obj = Puzzle(4, 4, [[4, 2, 3, 0], [5, 1, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print obj.row0_invariant(3), 'True'

    obj = Puzzle(4, 4, [[4, 2, 0, 3], [5, 1, 6, 9], [7, 8, 10, 11], [12, 13, 14, 15]])
    print obj.row0_invariant(2), 'False'

def test_solve_row1_tile():
    '''
    Test function
    '''

    obj = Puzzle(4, 4, [[4, 6, 1, 3], [5, 2, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_row1_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[5, 4, 1, 3], [6, 2, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_row1_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[4, 6, 1, 3], [5, 2, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_row1_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(5, 5, [[7, 1, 2, 3, 4], [5, 6, 0, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24] ])
    print 'Start pos'
    print obj
    obj.solve_row1_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[4, 3, 7, 6], [5, 2, 1, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_row1_tile(3)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[7, 4, 1, 3], [6, 2, 5, 0], [8, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_row1_tile(3)
    print 'End pos'
    print obj

def test_solve_row0_tile():
    '''
    Test function
    '''
    obj = Puzzle(4, 4, [[2, 3, 1, 0], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_row0_tile(3)
    print 'End pos'
    print obj

    obj = Puzzle(4, 4, [[2, 1, 0, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    print 'Start pos'
    print obj
    obj.solve_row0_tile(2)
    print 'End pos'
    print obj

    obj = Puzzle(5, 5, [[3, 1, 2, 0, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24] ])
    print 'Start pos'
    print obj
    obj.solve_row0_tile(3)
    print 'End pos'
    print obj

    obj = Puzzle(5, 5, [[2, 1, 3, 0, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24] ])
    print 'Start pos'
    print obj
    obj.solve_row0_tile(3)
    print 'End pos'
    print obj

def test_solve_2x2():
    '''
    Test function
    '''
    obj = Puzzle(2, 2, [[3, 2], [1, 0]])
    print 'Start pos'
    print obj
    obj.solve_2x2()
    print 'End pos'
    print obj

    obj = Puzzle(2, 2, [[1, 3], [2, 0]])
    print 'Start pos'
    print obj
    obj.solve_2x2()
    print 'End pos'
    print obj

    obj = Puzzle(2, 2, [[2, 1], [3, 0]])
    print 'Start pos'
    print obj
    obj.solve_2x2()
    print 'End pos'
    print obj

    # obj = Puzzle(2, 2, [[1, 2], [3, 0]]) unsolvable
    # obj = Puzzle(2, 2, [[2, 3], [1, 0]]) unsolvable
    # obj = Puzzle(2, 2, [[3, 1], [2, 0]]) unsolvable

def test_solve_puzzle():
    '''
    Test function
    '''
    grid_size = random.randint(3, 5)
    num_list = [num for num in range(grid_size ** 2)]
    random.shuffle(num_list)
    obj = Puzzle(grid_size, grid_size)
    for row in range(grid_size):
        for col in range(grid_size):
            obj.set_number(row, col, num_list.pop())

    print 'Start pos'
    print obj
    obj.solve_puzzle()
    print 'End pos'
    print obj

def all_tests():
    '''
    All test functions
    '''
    #test_lower_row_invariant()
    #testing_row_invariants()

    test_solve_interior_tile()
    print "test_solve_interior_tile() completed"
    test_solve_col0_tile()
    print "test_solve_col0_tile() completed"
    test_solve_row1_tile()
    print "test_solve_row1_tile() completed"
    test_solve_row0_tile()
    print "test_solve_row0_tile() completed"
    test_solve_2x2()
    print "test_solve_2x2() completed"
    test_solve_puzzle()
    print "test_solve_puzzle() completed"


#all_tests()


# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
