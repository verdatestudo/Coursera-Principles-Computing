"""
Create a rectagular grid and iterate through
a subset of its cells in a specified direction
"""

GRID_HEIGHT = 4
GRID_WIDTH = 6

# Create a rectangular grid using nested list comprehension
# Inner comprehension creates a single row
EXAMPLE_GRID = [[row + col for col in range(GRID_WIDTH)]
                           for row in range(GRID_HEIGHT)]

def traverse_grid(start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction

    Both start_cell is a tuple(row, col) denoting the
    starting cell

    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """

    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        print "Processing cell", (row, col),
        print "with value", EXAMPLE_GRID[row][col]

def run_example():
    """
    Run several example calls of traverse_grid()
    """
    print "Print out values in grid"
    for row in range(GRID_HEIGHT):
        print EXAMPLE_GRID[row]
    print

    print "Traversing first row"
    traverse_grid((0, 0), (0, 1), GRID_WIDTH)
    print

    print "Traversing second column"
    traverse_grid((0, 1), (1, 0), GRID_HEIGHT)
    print

    print "Traversing second column in reverse order"
    traverse_grid((GRID_HEIGHT - 1, 1), (-1, 0), GRID_HEIGHT)
    print

    print "Traversing diagonal"
    traverse_grid((0, 0), (1, 1), min(GRID_WIDTH, GRID_HEIGHT))

run_example()
