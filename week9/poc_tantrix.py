"""
Student facing code for Tantrix Solitaire
http://www.jaapsch.net/puzzles/tantrix.htm

Game is played on a grid of hexagonal tiles.
All ten tiles for Tantrix Solitaire and place in a corner of the grid.
Click on a tile to rotate it.  Cick and drag to move a tile.

Goal is to position the 10 provided tiles to form
a yellow, red or  blue loop of length 10
"""



# Core modeling idea - a triangular grid of hexagonal tiles are
# model by integer tuples of the form (i, j, k)
# where i + j + k == size and i, j, k >= 0.

# Each hexagon has a neighbor in one of six directions
# These directions are modeled by the differences between the
# tuples of these adjacent tiles

# Numbered directions for hexagonal grid, ordered clockwise at 60 degree intervals
DIRECTIONS = {0 : (-1, 0, 1), 1 : (-1, 1, 0), 2 : (0, 1, -1),
              3 : (1, 0, -1), 4 : (1, -1, 0), 5 : (0,  -1, 1)}

def reverse_direction(direction):
    """
    Helper function that returns opposite direction on hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions / 2) % num_directions



# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]


# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 4

import random

class Tantrix:
    """
    Basic Tantrix game class
    """

    def __init__(self, size):
        """
        Create a triangular grid of hexagons with size + 1 tiles on each side.
        See poc_tantrix_grid.png for example
        """
        assert size >= MINIMAL_GRID_SIZE

        self._size = size
        self._tile_value = {}
        temp_sol_codes = SOLITAIRE_CODES[:]

        # randomly place tiles in grid
        # in this system i, j, k must equal 6
        while len(temp_sol_codes) > 0:
            i = random.randint(0, size)
            j = random.randint(0, size - i)
            k = size - i - j
            if self.tile_exists((i, j, k)) == False:
                self.place_tile((i, j, k), temp_sol_codes.pop())

    def __str__(self):
        """
        Return string of dictionary of tile positions and values
        """
        return str(self._tile_value)

    def get_tiling_size(self):
        """
        Return size of board for GUI
        """
        return self._size

    def tile_exists(self, index):
        """
        Return whether a tile with given index exists
        """
        if index in self._tile_value:
            return True
        else:
            return False

    def place_tile(self, index, code):
        """
        Play a tile with code at cell with given index
        """
        self._tile_value[index] = code

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index
        and return the code value for that tile
        """
        return self._tile_value.pop(index)

    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        """
        # if BBRRYY then YBBRRY. Zero index is the south-east face of hexagon.
        self._tile_value[index] = self._tile_value[index][-1] + self._tile_value[index][0:-1]

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        """
        return self._tile_value[index]

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in given direction
        """
        # adds elements of both tuples to return the neighbor
        return tuple(map(sum,zip(index,direction)))

    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for adjacent tiles
        """
        # for all tiles, for all directions
        # if there is a tile in neighbouring square
        # then if they do not match, return False.
        # directions match in reverse - e.g tile direction 2 needs to equal neighbour direction 5

        for key, value in self._tile_value.items():
            for key2, value2 in DIRECTIONS.items():
                nebor = self.get_neighbor(key, value2)
                if self.tile_exists(nebor):
                    if value[key2] != self._tile_value[nebor][reverse_direction(key2)]:
                        return False
        return True

    def has_loop(self, color):
        """
        Check whether a tile configuration has a loop of size 10 of given color
        """

        if self.is_legal() == False:
            return False
        else:
            key, value = random.choice(self._tile_value.items())
            return self.has_loop_helper(color, key, value, 0, [], key)

    def has_loop_helper(self, color, key, value, count, checked_tiles, original_tile):
        '''
        Helper function for has loop
        '''
        checked_tiles.append(key)

        if len(checked_tiles) == len(SOLITAIRE_CODES):
            for key2, value2 in DIRECTIONS.items():
                nebor = self.get_neighbor(key, value2)
                # make sure it's a loop and not just 10 tiles in a line
                if self.tile_exists(nebor) and value[key2] == color and value[key2] == self.get_code(nebor)[reverse_direction(key2)] and nebor == original_tile:
                    return True

        for key2, value2 in DIRECTIONS.items():
            nebor = self.get_neighbor(key, value2)
            if self.tile_exists(nebor) and nebor not in checked_tiles: # if there is a nebor and we haven't seen it before
                if value[key2] == color and value[key2] == self.get_code(nebor)[reverse_direction(key2)]: # if it's the right colour and both match
                    return self.has_loop_helper(color, nebor, self._tile_value[nebor], count, checked_tiles, original_tile)
        return False

'''
# run GUI for Tantrix
import poc_tantrix_gui
poc_tantrix_gui.TantrixGUI(Tantrix(6))
'''
