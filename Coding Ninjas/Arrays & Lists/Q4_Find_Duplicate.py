# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). Each number is
# present at least once. That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these,
# there is a single integer value that is present twice. You need to find and return that duplicate number present in
# the array.
# Note : Duplicate number is always present in the given array/list.

# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Output Format :
# For each test case, print the duplicate element in the array/list.
#
# Output for every test case will be printed in a separate line.

import sys
from collections import Counter


def duplicateNumber(arr, n):
    # Your code goes here
    dict = Counter(arr)
    keys = [k for k, v in dict.items() if v == 2]
    for key in keys:
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
    print(duplicateNumber(arr, n))

    t -= 1
