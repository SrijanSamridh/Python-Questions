# You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements in the array/list.
# You don't need to print or return anything, just change in the input array itself.
# Input Format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the elements of the resulting array in a single row separated by a single space.
#
# Output for every test case will be printed in a separate line.

from sys import stdin


def swapAlternate(arr, n):
    # Your code goes here
    # if n % 2 == 0:
    #     end = n
    # else:
    #     end = n-1
    end = n - 1 if n % 2 else n
    arr[1:end:2], arr[:end:2] = arr[:end:2], arr[1:end:2]
    return arr








# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# Printing the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    if n != 0:
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1




