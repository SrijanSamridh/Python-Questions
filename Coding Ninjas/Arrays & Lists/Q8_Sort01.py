# You have been given an integer array/list(ARR) of size N that contains only integers, 0 and 1. Write a function to
# sort this array/list. Think of a solution which scans the array/list only once and don't require use of an extra
# array/list.
# Note: You need to change in the given array/list itself. Hence, no need to return or print anything.

# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# Second line contains 'N' single space separated integers(all 0s and 1s) representing the elements in the array/list.
# Output format :
# For each test case, print the sorted array/list elements in a row separated by a single space.
#
# Output for every test case will be printed in a separate line.
from sys import stdin


def sortZeroesAndOne(a, arr_size):
    # Your code goes here
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
