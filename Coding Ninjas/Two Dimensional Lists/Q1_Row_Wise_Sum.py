# For a given two-dimensional integer array/list of size (N x M), find and print the sum of each of the row elements
# in a single line, separated by a single space.

# Input Format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They
# represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
#
# Second line onwards, the next 'N' lines or rows represent the ith row values.
#
# Each of the ith row constitutes 'M' column values separated by a single space.
# Output Format :
# For each test case, print the sum of every ith row elements in a single line separated by a single space.
#
# Output for every test case will be printed in a seperate line.

from sys import stdin


def rowWiseSum(mat, nRows, mCols):
    # Your code goes here
    Sum = [sum(x) for x in mat]
    for i in Sum:
        print(i, end=" ")
    # print(i,)


# Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


# main
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    rowWiseSum(mat, nRows, mCols)
    print()

    t -= 1
