# For a given two-dimensional integer array/list of size (N x M), print the array/list in a sine wave order, i.e,
# print the first column top to bottom, next column bottom to top and so on.

# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They
# represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
#
# Second line onwards, the next 'N' lines or rows represent the ith row values.
#
# Each of the ith row constitutes 'M' column values separated by a single space.

# Output format : For each test case, print the elements of the two-dimensional array/list in the sine wave order in
# a single line, separated by a single space.
#
# Output for every test case will be printed in a seperate line.

from sys import stdin


def wavePrint(arr, nRows, mCols):
    # Your code goes here
    rev_Wave = []
    n = nRows
    m = mCols
    # j = m - 1                            			# to print reversed Wave
    j = 0
    wave = 1

    # n     - Ending row index
    # m     - Ending column index
    # i, j     - Iterator
    # wave     - for Direction
    # wave = 1 - Wave direction down
    # wave = 0 - Wave direction up

    # while j >= 0:                         		# do this to print reversed Wave
    while j < m:  # doing this to print Wave

        # Check whether to go in
        # upward or downward
        if wave == 1:

            # Print the element of the
            # matrix downward since the
            # value of wave = 1
            for i in range(n):
                print(arr[i][j], end=" ")
                # rev_Wave.append(arr[i][j])
            wave = 0
            j += 1
            # j -= 1

        else:
            # Print the elements of the
            # matrix upward since the
            # value of wave = 0
            for i in range(n - 1, -1, -1):
                print(arr[i][j], end=" ")
                # rev_Wave.append(arr[i][j])

            wave = 1
            j += 1
            # j -= 1


# Taking Iput Using Fast I/O
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
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1
