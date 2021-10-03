# You have been given a random integer array/list(ARR) of size N. You are required to find and return the second
# largest element present in the array/list. If N <= 1 or all the elements are same in the array/list then return
# -2147483648 or -2 ^ 31(It is the smallest value for the range of Integer)
#
# Input format : The first line contains an
# Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#
# The first line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# The second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the second largest in the array/list if exists, -2147483648 otherwise.
#
# Output for every test case will be printed in a separate line.


# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def secondLargestElement(arr, n):  # 9 3 6 2 9
    # Your code goes here
    MIN_VALUE = -2147483648
    arr = sorted(list(set(arr)))
    # print(arr)
    n = len(arr)
    if n <= 1:
        return MIN_VALUE
    else:
        for i in range(n - 1, 0, -1):
            if arr[-2] != arr[-1]:
                return arr[-2]
            else:
                return MIN_VALUE


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1