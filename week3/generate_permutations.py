
import itertools
import pickle

# can change this function later so you can input what posNums and
# noOfPos's you want etc. for now this is set up for mansala

def generate_permutations():
    # e.g 2048 game this would be [0, 2, 4, 8] for testing purposes

    list_of_possible_numbers = [0,1,2,3,4,5,6,7,8,9,10]
    myList = []

    # range is number of positions available. for example in 2048 you might say
    # ok lets test a grid with length 1 up to a grid of length 7
    # for mansala testing we're only interested in range 6 (we add house 0 later)

    for number_of_positions_available in range(6, 7):
        temp_list = list(itertools.product(list_of_possible_numbers, repeat=number_of_positions_available))
        for value in temp_list:
            myList.append(list(value))
            # tuple is quicker, using a list because for mansala i need to insert a value below

    print len(myList)

    ### this is for mansala only, adding the house at the front of each item
    print myList[1111]
    for item in myList:
        item.insert(0, 0)
    print myList[1111]
    ###
    return myList


'''# e.g 2048 game this would be [0, 2, 4, 8] for testing purposes

list_of_possible_numbers = [0,1,2,3,4,5,6,7,8,9,10]
myList = []

# range is number of positions available. for example in 2048 you might say
# ok lets test a grid with length 1 up to a grid of length 7
# for mansala testing we're only interested in range 6 (we add house 0 later)

for number_of_positions_available in range(6, 7):
    temp_list = list(itertools.product(list_of_possible_numbers, repeat=number_of_positions_available))
    for value in temp_list:
        myList.append(list(value))
        # tuple is quicker, using a list because for mansala i need to insert a value below

print len(myList)

### this is for mansala only, adding the house at the front of each item
print myList[1111]
for item in myList:
    item.insert(0, 0)
print myList[1111]
###

with open('mansala_all_permutations', 'wb') as f:
    pickle.dump(myList, f)'''
