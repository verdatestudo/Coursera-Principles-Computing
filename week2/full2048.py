"""
Principles of Computing - week 2
Clone of 2048 game.
2016-Jan-22
Python 2.7
Chris
"""

import random

# CHANCE OF drawing VAl1 or VAl2 on new tile - number shows chance of drawing VAL1
NEW_TILE_CHANCE = 90    # out of 100, could use 0-1 but this looks nicer
# possible values of NEW tile
NEW_TILE_VAL1 = 2
NEW_TILE_VAL2 = 4

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    new_line = list(line[:])

    def slide(new_line):
        '''
        slides values leftwards into empty spaces
        '''
        for item in range(1, len(new_line)):
            if new_line[item] != 0:
                for place in range(item):
                    if new_line[place] == 0:
                        new_line[place] = new_line[item]
                        new_line[item] = 0

    slide(new_line)

    # double value for matching pairs
    for num in range(1, len(new_line)):
        if new_line[num] == new_line[num-1]:
            new_line[num-1] *= 2
            new_line[num] = 0

    slide(new_line)

    return new_line

class  TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid = []
        self._grid_height = grid_height
        self._grid_width = grid_width

        self._endptsdict = {UP: [], DOWN: [], LEFT: [], RIGHT: []}

        for xxx in range(self._grid_width):
            self._endptsdict[UP].append([0, xxx])
            self._endptsdict[DOWN].append([self._grid_height-1, xxx])

        for yyy in range(self._grid_height):
            self._endptsdict[LEFT].append([yyy, 0])
            self._endptsdict[RIGHT].append([yyy, self._grid_width-1])

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid[:] = []
        for _ in range(self._grid_height):
                self._grid.append([0] * self._grid_width)

        # LIST COMPREHENSION
        #self._grid = [[row + col for col in range(self._grid_width)]
        #                   for row in range(self._grid_height)]

        self.new_tile()
        self.new_tile()

        # NEED TO ADD CODE TO RESET ALL VARS ON RESTART GAME

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for line in self._grid:
            print str(line)
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        new_merge_list = []
        for value in self._endptsdict[direction]:
            next_cell = value[:]
            temp_merge_list = []
            while (0 <= next_cell[0] < self._grid_height) and (0 <= next_cell[1] < self._grid_width):
                temp_merge_list.append(self._grid[next_cell[0]][next_cell[1]])
                next_cell[0] += OFFSETS[direction][0]
                next_cell[1] += OFFSETS[direction][1]
            new_merge_list.append(merge(temp_merge_list))

        tile_moved = False
        next_line = 0

        for value in self._endptsdict[direction]:
            next_cell = value[:]
            step = 0
            while (0 <= next_cell[0] < self._grid_height) and (0 <= next_cell[1] < self._grid_width):
                if self._grid[next_cell[0]][next_cell[1]] != new_merge_list[next_line][step]:
                    self._grid[next_cell[0]][next_cell[1]] = new_merge_list[next_line][step]
                    tile_moved = True
                next_cell[0] += OFFSETS[direction][0]
                next_cell[1] += OFFSETS[direction][1]
                step += 1
            next_line += 1

        if tile_moved == True:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_s = []
        for xxx in range(len(self._grid)):
            for yyy in range(len(self._grid[xxx])):
                if self._grid[xxx][yyy] == 0:
                    empty_s.append([xxx, yyy])
        new_sq = random.choice(empty_s)
        roll = random.randint(1,100)
        if roll <= NEW_TILE_CHANCE:
            self.set_tile(new_sq[0], new_sq[1], NEW_TILE_VAL1)
        else:
            self.set_tile(new_sq[0], new_sq[1], NEW_TILE_VAL2)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


    def temp_test(self):
        '''
        temp tests
        '''
        #print self.__str__()
        #print 'gridH 4', self.get_grid_height()
        #print 'gridW 8 ', self.get_grid_width()
        #print 'getTile 0,0', self.get_tile(0,0)
        #print 'self._endptsdict', self._endptsdict
        #self.move(RIGHT)
        #print self.__str__()
        pass

# no need to "call" str, just print like below comment
# print str(TwentyFortyEight(4, 8))

#myGame =  TwentyFortyEight(4, 8)
#myGame.temp_test()

# import poc_2048_gui
# poc_2048_gui.run_gui( TwentyFortyEight(4, 4))
