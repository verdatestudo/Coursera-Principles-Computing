"""
Merge function for 2048 game.
"""

# using len(new_line) etc is probably lazy code
# started a separate file to improve this, but this is MAIN file for now.

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
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

def merge_test():
    '''
    some testing
    '''
    print merge([2, 0, 2, 4]), 'should be: [4, 4, 0, 0]'
    print merge([0, 0, 2, 2]), 'should be: [4, 0, 0, 0]'
    print merge([2, 2, 0, 0]), 'should be: [4, 0, 0, 0]'
    print merge([2, 2, 2, 2, 2]), 'should be: [4, 4, 2, 0 ,0]'
    print merge([8, 16, 16, 8]), 'should be: [8, 32, 8, 0]'
    print merge([4, 2, 8, 2, 0, 8, 8]), 'should be: [4, 2, 8, 2, 16, 0, 0]'

#merge_test()

TEST_CASES = [[0], [0, 4, 8, 0, 4], [2, 4, 4, 0, 0], [2, 8, 2, 8, 8, 0], [4, 2, 2, 2, 0, 0], \
    [4, 4, 2, 2, 0], [4, 0, 8, 0, 0, 0], \
    [8, 8, 4, 4, 0, 0], [8, 8, 4, 8, 2, 0], [2, 4, 0, 4, 0, 0] ]

#TEST_CASES = [[0], [2], [0, 4, 8, 0, 4], [2, 4, 4, 0, 0], [2, 8, 2, 8, 8, 0], [4, 2, 2, 2, 0, 0], \
#    [4, 2, 2, 0, 0, 0], [8,8,0,0,0], [4, 4, 2, 2, 0, 0], [4, 0, 8, 0, 0, 0], [0, 4, 2, 0, 0, 0], \
#    [8, 8, 4, 4, 0, 0], [8, 8, 4, 8, 2, 0], [2, 4, 0, 4, 0, 0] ]

#TEST_CASES = [[2, 0, 2, 4], [0, 0, 2, 2], [2, 2, 0, 0], [2, 2, 2, 2, 2], [8, 16, 16, 8], \
#            [4, 2, 8, 2, 0, 8, 8], [0,0,0,0], [0], [2] ]
