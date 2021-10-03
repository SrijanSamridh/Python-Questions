# You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, merge them into a third
# array/list such that the third array is also sorted.

# Input Format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#
# Second line contains 'N' single space separated integers representing the elements of the first array/list.
#
# Third line contains an integer 'M' representing the size of the second array/list.
#
# Fourth line contains 'M' single space separated integers representing the elements of the second array/list.
# Output Format :
# For each test case, print the sorted array/list(of size N + M) in a single row, separated by a single space.
#
# Output for every test case will be printed in a separate line.

from sys import stdin


def merge(arr1, n, arr2, m):
    i = 0
    j = 0
    arr3 = []

    # Traverse both array
    while i < n and j < m:

        # Check if current element
        # of first array is smaller
        # than current element of
        # second array. If yes,
        # store first array element
        # and increment first array
        # index. Otherwise do same
        # with second array
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i = i + 1
        else:
            arr3.append(arr2[j])
            j = j + 1

    # Store remaining elements
    # of first array
    while i < n:
        arr3.append(arr1[i])
        i = i + 1

    # Store remaining elements
    # of second array
    while j < m:
        arr3.append(arr2[j])
        j = j + 1

    # print("Array after merging")
    # for i in range(n + m):
    #     print(str(arr3[i]), end=" ")
    return arr3


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1