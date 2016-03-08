'''
Principles of Computing - week 7
Binary representations for numbers - practice activity
2016-Mar-03
Python 2.7
Chris
'''

def make_binary(length):
    '''
    Binary numbers
    A decimal number is typically modeled as a sequence of the decimal digits (0 to 9).)
    A binary number is expressed as a sequence of binary digits (either 0 or 1) often called bits.
    Binary numbers are particularly important in computer science since they are the fundamental representation used to model the digital logic that underlies all modern computer hardware.

    Creating a list of all binary numbers of a given length is not particularly difficult.
    For example, the iterative method in gen_all_sequences can enumerate all 2n binary numbers of length n.
    Your first task for this activity is to write a recursive function make_binary(length) that returns a list containing all binary numbers of the specified length.

    Observe that this problem has a natural recursive structure.
    If n is zero, your implementation should return a list consisting of exactly one string, the empty string "".
    Otherwise, your implementation should compute make_binary(length - 1) and use the resulting list to construct the final list.
    Once you have attempted the problem, you are welcome to examine our code which contains solutions to all four of the problems in this exercise.
    '''
    if length == 0:
        return [""]

    all_but_first = make_binary(length - 1)

    answer = []
    for bits in all_but_first:
        answer.append("0" + bits)
    for bits in all_but_first:
        answer.append("1" + bits)
    return answer

def bin_to_dec(bin_num):
    '''
    Computing the value of a binary number
    For decimal numbers, the leftmost digits are usually treated as being more significant that the rightmost digits.
    This convention is also followed in binary numbers. If the binary number has the n bits bn-1bn-2...b1b0, then the corresponding decimal value of this number is ?i=0n-12ibi.
    For example, the binary string "100" has the decimal value 4 while the binary string "001" has the decimal value 1.
    As a point of interest, notice that our solution for make_binary generates the binary strings ordered by ascending value.

    Your next task is to write a recursive function bin_to_dec(bin_num) that computes the decimal value of the specified binary number.
    While the iterative definition given above can be used to compute this value, we suggest that you implement bin_to_decrecursively to gain further practice with recursion.
    If the length of the binary string is zero, your implementation should return zero.
    Otherwise, your implementation should compute the decimal value of the n-1 most significant bits and then use this value along with the value
    of the least significant bit to compute the decimal value of all n bits. Once you have attempted the problem, you are welcome to examine our sample solution.
    '''

    if len(bin_num) == 0:
        return 0
    else:
        return 2 * bin_to_dec(bin_num[:-1]) + int(bin_num[-1])

def make_gray(length):
    '''
    Gray codes
    The standard binary representation, while incredibly useful in many applications, is not always the best binary representation for some applications.
    For example, imagine an application in which one is scanning a positional or rotational value and converting this value into an n-bit number.
    Due to inaccuracy in the scanner, the resulting value may be off by one.
    Using a standard binary number system, the resulting n-bit number may have several incorrect bits.
    For example, if the value 7 was incorrectly scanned as 8, the resulting five-bit binary strings "00111"and "01000" would differ by 4 bits.

    Gray coding (also known as reflected binary numbers) is a binary number system in which strings corresponding to consecutive values always differ by exactly one bit.
    In the example above, the five-bit Gray codes corresponding to 7 and 8 are "00100" and "01100", respectively.
    Note that these two strings differ by exactly one bit.

    For the third problem, your task is to write a recursive function make_gray(length) that generates a list of binary strings of the specified length
    ordered such that consecutive strings differ by exactly one bit.
    Your recursive solution should be very similar to make_binary which generated a list of all binary strings ordered by their standard values.
    If the length is zero, the answer is the list consisting of the empty string.
    Otherwise, your function should recursively compute make_gray(length-1) and use this list to construct make_gray(length).
    In the case of standard binary numbers, make_binary(length) created two copies of the list make_binary(length - 1).
    make_gray(length) should also create two copies of make_gray(length - 1).
    However, one of these copies should be reflected (i.e; reversed).
    Spend a few minutes experimenting with some simple examples and see if you can implement make_gray.
    If you need more help, this section of the Wikipedia page on Gray codes explains the solution.
    '''
    if length == 0:
        return [""]
    else:
        binary_nums = make_binary(length - 1)
        rev_nums = []
        for item in binary_nums:
            rev_nums.append(list_reverse(item))

    return ['0' + x for x in binary_nums] + ['1' + x for x in rev_nums]

    '''
    # alternate solution
    def make_gray(length):
    """
    Function that generates ordered list of Gray codes in
    ascending order
    """
    if length == 0:
        return [""]

    all_but_first = make_gray(length - 1)

    answer = []
    for bits in all_but_first:
        answer.append("0" + bits)

    all_but_first.reverse()

    for bits in all_but_first:
        answer.append("1" + bits)
    return answer
    '''

def list_reverse(my_list):
    '''
    Write a function list_reverse(my_list) that takes a list and returns a new list whose elements appear in reversed order.
    For example, list_reverse([2, 3, 1]) should return [1, 3, 2]. Do not use the reverse() method for lists.
    Solution - http://www.codeskulptor.org/#poc_recursion_reverse.py
    '''
    if len(my_list) < 2:
        return my_list

    first_item = my_list[0]
    last_item = my_list[-1]
    return last_item + list_reverse(my_list[1:-1]) + first_item

def gray_to_bin(gray_code):
    '''
    Computing the value of a Gray code
    Our solution for make_gray returns a list of Gray codes ordered in ascending value.
    For standard binary numbers, the function bin_to_dec computes the value of a binary number.
    To compute the decimal value of a Gray code, we will implement a function gray_to_bin that converts a Gray code to the standard binary number with same value.
    This function can then be used to compute the value of a Gray code by evaluating bin_to_dec(gray_to_bin(gray_code)).

    Challenge problem: Your final task is to write a recursive function gray_to_bin(gray_code) that performs this conversion.
    Again, this function is remarkably simple. However, deriving this function on your own may prove to be quite difficult.
    So, we recommend that you read up further on Gray codes as you work on this problem.
    In particular, we suggest that you focus on the next to last paragraph in the Wikipedia section referenced above.
    '''
    # copied from examples
    if len(gray_code) <= 1:
        return gray_code
    else:
        significant_bits = gray_to_bin(gray_code[:-1])
        last_bit = (int(gray_code[-1]) + int(significant_bits[-1])) % 2
        return significant_bits + str(last_bit)

def run_examples():
    """
    print out example of Gray code representations
    """
    num = 5
    print
    print "Binary numbers of length", num
    bin_list = make_binary(num)
    print bin_list

    print
    print "Decimal numbers up to", 2 ** num
    print [bin_to_dec(binary_number) for binary_number in bin_list]

    print
    print "Gray codes of length", num
    gray_list = make_gray(num)
    print gray_list

    print
    print "Gray codes converted to binary numbers"
    print [gray_to_bin(gray_code) for gray_code in gray_list]

run_examples()
