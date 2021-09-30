# You have been given an integer array/list(ARR) and a number X. Find and return the total number of pairs in the
# array/list which sum to X.
# Note: Given array/list can contain duplicate elements.

# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
#
# Third line contains an integer 'X'.

# Output format :
# For each test case, print the total number of pairs present in the array/list.
#
# Output for every test case will be printed in a separate line.

from sys import stdin  ## Print output as specified in the question.


def pairsum(arr, n, x):
    count = 0
    for i in range(n):
        for j in range((i + 1), n):
            if arr[i] + arr[j] == x:
                count = count + 1
    return count


# Taking Input Using Fast I/
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairsum(arr, n, x))

    t -= 1


