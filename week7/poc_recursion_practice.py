
'''
Recursion Practice Activities
Principles of Computing - Week 7
Python 2.7
Chris
'''


def triangular_sum(num):
    '''
    Write a function triangular_sum(num) that computes the arithmetic sum 0+1+2...+(num-1)+num.
    For example, triangular_sum(3) should return 6.
    Note that this sum can be computed directly via a simple arithmetic formula, but use a recursive approach instead.
    Solution - http://www.codeskulptor.org/#poc_recursion_triangular.py
    '''
    if num == 0:
        return num
    else:
        return num + triangular_sum(num-1)

def test_triangular_sum():
    for x in range(1,11):
        print x, triangular_sum(x), 'should return %d' %(x * (x+1)/2)

def number_of_threes(num):
    '''
    Write a function number_of_threes(num) that returns the number of times the digit 3 appears in the decimal
    representation of the non-negative integer num. For example number_of_threes(34534) should return 2.
    Solution - http://www.codeskulptor.org/#poc_recursion_threes.py
    '''
    if num == 0:
        return 0

    last_digit = num % 10

    if last_digit == 3:
        return 1 + number_of_threes(num / 10)
    else:
        return number_of_threes(num / 10)

def test_number_of_threes():
    print number_of_threes(34534), 'should return 2'
    print number_of_threes(678), 'should return 0'

def is_member(my_list, elem):
    '''
    Write a function is_member(my_list, elem) that returns True if elem is a member of my_list and False otherwise.
    For example, is_member(['c', 'a', 't'], 'a') should return True.
    Do not use any of Python's built-in list methods or an operator like in.
    Solution - http://www.codeskulptor.org/#poc_recursion_member.py
    '''
    if len(my_list) < 1:
        return False

    first_item = my_list[0]
    if first_item == elem:
        return True
    else:
        return is_member(my_list[1:], elem)

def test_is_member():
    print is_member(['c', 'a', 't'], 'a'), 'should return TRUE'
    print is_member(['c', 'b', 't'], 'a'), 'should return FALSE'

def remove_x(my_string):
    '''
    Write a function remove_x(my_string) that takes the string my_string and deletes all occurrences of the character 'x' from this string.
    For example, remove_x("catxxdogx") should return "catdog". You should not use Python's built-in string methods.
    Solution - http://www.codeskulptor.org/#poc_recursion_removex.py
    '''
    if len(my_string) < 1:
        return my_string

    first_item = my_string[0]
    if first_item == 'x':
        return remove_x(my_string[1:])
    else:
        return first_item + remove_x(my_string[1:])

def test_remove_x():
    """
    Some test cases for remove_x
    """
    print "Computed:", "\"" + remove_x("") + "\"", "Expected: \"\""
    print "Computed:", "\"" + remove_x("cat") + "\"", "Expected: \"cat\""
    print "Computed:", "\"" + remove_x("xxx") + "\"", "Expected: \"\""
    print "Computed:", "\"" + remove_x("dxoxg") + "\"", "Expected: \"dog\""
    print "Computed:", "\"" + remove_x("bxbxox") + "\"", "Expected: \"bbo\""
    print "Computed:", "\"" + remove_x("xxx") + "\"", "Expected: \"\""

def insert_x(my_string):
    '''
    Write a function insert_x(my_string) that takes the string my_string and adds the character 'x' between each pair of consecutive characters in the string.
    For example, insert_x("catdog") should return "cxaxtxdxoxg".
    Solution - http://www.codeskulptor.org/#poc_recursion_insertx.py
    '''
    if len(my_string) < 2:
        return my_string
    else:
        return my_string[0] + 'x' + insert_x(my_string[1:])

def test_insert_x():
    """
    Some test cases for insert_x
    """
    print "Computed:", "\"" + insert_x("") + "\"", "Expected: \"\""
    print "Computed:", "\"" + insert_x("c") + "\"", "Expected: \"c\""
    print "Computed:", "\"" + insert_x("pig") + "\"", "Expected: \"pxixg\""
    print "Computed:", "\"" + insert_x("catdog") + "\"", "Expected: \"cxaxtxdxoxg\""

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
    return [last_item] + list_reverse(my_list[1:-1]) + [first_item]

def test_list_reverse():
    """
    Some test cases for list_reverse
    """
    print "Computed:", list_reverse([]), "Expected: []"
    print "Computed:", list_reverse([1]), "Expected: [1]"
    print "Computed:", list_reverse([1, 2, 3]), "Expected: [3, 2, 1]"
    print "Computed:", list_reverse([2, 3, 1]), "Expected: [1, 3, 2]"
    print "Computed:", list_reverse([1, 2, 3, 4, 5, 6, 7, 8]), "Expected: [8, 7, 6, 5, 4, 3, 2, 1]"

def gcd(num1, num2):
    '''
    Challenge: Write a function gcd(num1, num2) that takes two non-negative integers and computes the greatest common divisor of num1 and num2.
    To simplify the problem, you may assume that the greatest common divisor of zero and any non-negative integer is the integer itself.
    For an extra challenge, your programs should only use subtraction. Hint: If you get stuck, try searching for "Euclid's Algorithm".
    Solution - http://www.codeskulptor.org/#poc_recursion_gcd.py
    '''
    if num1 < 0 and num2 < 0:
        return None
    elif num1 <= 0 or num2 <= 0:
        return max(num1, num2)
    else:
        a = max(num1, num2)
        b = min(num1, num2)
        rem = a % b
        return gcd(b, rem)

def binary_gcd(num1, num2):
    '''
    https://en.wikipedia.org/wiki/Binary_GCD_algorithm

    Algorithm
    The algorithm reduces the problem of finding the GCD by repeatedly applying these identities:
    gcd(0, v) = v, because everything divides zero, and v is the largest number that divides v.
    Similarly, gcd(u, 0) = u. gcd(0, 0) is not typically defined, but it is convenient to set gcd(0, 0) = 0.
    If u and v are both even, then gcd(u, v) = 2gcd(u/2, v/2), because 2 is a common divisor.
    If u is even and v is odd, then gcd(u, v) = gcd(u/2, v), because 2 is not a common divisor.
    Similarly, if u is odd and v is even, then gcd(u, v) = gcd(u, v/2).
    If u and v are both odd, and u = v, then gcd(u, v) = gcd((u - v)/2, v).
    If both are odd and u < v, then gcd(u, v) = gcd((v - u)/2, u).
    These are combinations of one step of the simple Euclidean algorithm, which uses subtraction at each step, and an application of step 3 above.
    The division by 2 results in an integer because the difference of two odd numbers is even.[3]
    '''
    if num1 == 0 and num2 == 0:
        return 0
    elif num1 <= 0 or num2 <= 0:
        return max(num1, num2)
    else:
        if num1 % 2 == 0 and num2 % 2 == 0:
            return 2 * gcd(num1 / 2, num2 / 2)
        elif (num1 % 2 == 0 and num2 % 2 != 0):
            return gcd(num1 / 2, num2)
        elif (num1 % 2 != 0 and num2 % 2 == 0):
            return gcd(num1, num2 / 2)
        elif num1 % 2 != 0 and num2 % 2 != 0:
            if num1 == num2:
                return gcd((num1 - num2) / 2, num2)
            else:
                a = max(num1, num2)
                b = min(num1, num2)
                return gcd((a - b) / 2, b)


def test_gcd():
    """
    Some test cases for gcd
    """
    print "Computed:", gcd(0, 0), "Expected: 0"
    print "Computed:", gcd(3, 0), "Expected: 3"
    print "Computed:", gcd(0, 2), "Expected: 2"
    print "Computed:", gcd(12, 4), "Expected: 4"
    print "Computed:", gcd(24, 18), "Expected: 6"
    print "Computed:", gcd(1071, 462), "Expected: 21"
    print "Computed:", gcd(8765, 1234), "Expected: 1"

def test_binary_gcd():
    """
    Some test cases for binary gcd
    """
    print "Computed:", binary_gcd(0, 0), "Expected: 0"
    print "Computed:", binary_gcd(3, 0), "Expected: 3"
    print "Computed:", binary_gcd(0, 2), "Expected: 2"
    print "Computed:", binary_gcd(12, 4), "Expected: 4"
    print "Computed:", binary_gcd(24, 18), "Expected: 6"
    print "Computed:", binary_gcd(1071, 462), "Expected: 21"
    print "Computed:", binary_gcd(8765, 1234), "Expected: 1"

def slice(my_list, first, last):
    '''
    Challenge: Write a function slice(my_list, first, last) that takes as input a list my_list and two non-negative integer indices first and last
    satisfying 0 <= first <= last <= n where n is the length of my_list.
    slice should return the corresponding Python list slice my_list[first:last].
    For example, slice(['a', 'b', 'c', 'd', 'e'], 2, 4]) should return ['c', 'd'].

    Important: Your solution should not use Python's built-in slice operator : anywhere in its implementation.
    Instead use the method pop to remove one element from the input list during each recursive call.
    (You may mutate the input list to simplify your solution.)
    Solution - http://www.codeskulptor.org/#poc_recursion_slice.py
    '''
    if len(my_list) == 0:
        return []
    else:
        if last - first > 0:
            popped = my_list.pop(first)
            return [popped] + slice(my_list, first, last - 1)
        else:
            return []

def test_slice():
    """
    Some test cases for slice
    """
    print "Computed:", slice([], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 0), "Expected: []"
    print "Computed:", slice([1], 0, 1), "Expected: [1]"
    print "Computed:", slice([1, 2, 3], 0, 3), "Expected: [1, 2, 3]"
    print "Computed:", slice([1, 2, 3], 1, 2), "Expected: [2]"

def testing():
    '''
    test_triangular_sum()
    test_number_of_threes()
    test_is_member()
    test_remove_x()
    test_insert_x()
    test_list_reverse()
    '''
    print 'test gcd'
    test_gcd()
    print 'test binary gcd'
    test_binary_gcd()
    print 'test slice'
    test_slice()

testing()
