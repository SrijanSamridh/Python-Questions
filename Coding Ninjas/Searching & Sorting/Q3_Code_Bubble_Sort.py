# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Bubble
# Sort'.

# Note:
# Change in the input array/list itself. You don't need to return or print the elements.

# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output format :
# For each test case, print the elements of the array/list in sorted order separated by a single space.
#
# Output for every test case will be printed in a separate line.

from sys import stdin


def bubbleSort(arr, n):
    # Your code goes here
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # return arr


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    bubbleSort(arr, n)
    printList(arr, n)

    t -= 1