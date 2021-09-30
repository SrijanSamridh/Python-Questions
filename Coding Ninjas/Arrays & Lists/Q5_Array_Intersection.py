# You have been given two integer arrays/list(ARR1 and ARR2) of size M and N, respectively. You need to print their
# intersection; An intersection for this problem can be defined when both the arrays/lists contain a particular value
# or to put it in other words, when there is a common value that exists in both the arrays/lists.

# Note :
# Input arrays/lists can contain duplicate elements.

# The intersection elements printed would be in the order they appear in the first array/list(ARR1)

# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#
# Second line contains 'N' single space separated integers representing the elements of the first the array/list.
#
# Third line contains an integer 'M' representing the size of the second array/list.
#
# Fourth line contains 'M' single space separated integers representing the elements of the second array/list.
# Output format :
# For each test case, print the intersection elements in a row, separated by a single space.
#
# Output for every test case will be printed in a separate line.

# Sample Input 1 :
# 2
# 6
# 2 6 8 5 4 3
# 4
# 2 3 4 7
# 2
# 10 10
# 1
# 10

# Sample Output 1 :
# 2 4 3
# 10

import sys


def intersections(arr1, n, arr2, m):
    # Your code goes here
    intersection = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                intersection.append(arr1[i])
                arr2.remove(arr2[j])
                break
    for i in intersection:
        print(i, end=" ")


# Taking Input Using Fast I/O
def takeInput():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(sys.stdin.readline().strip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1


