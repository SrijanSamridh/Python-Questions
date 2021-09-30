# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.
#  Note:
# Unique element is always present in the array/list according to the given condition.

# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Output Format :
# For each test case, print the unique element present in the array.
#
# Output for every test case will be printed in a separate line.

import sys

from collections import Counter
def findUnique(arr, n):
    # Your code goes here
    dic = Counter(arr)
    for key, value in dic.items():
        if 1 == value:
            return key


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1


