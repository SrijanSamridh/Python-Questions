# For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. That is, you need to
# print in the order followed for every iteration:

# a. First row(left to right)
# b. Last column(top to bottom)
# c. Last row(right to left)
# d. First column(bottom to top)
#  Mind that every element will be printed only once.
# Spiral path of a matrix
#
# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They
# represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
#
# Second line onwards, the next 'N' lines or rows represent the ith row values.
#
# Each of the ith row constitutes 'M' column values separated by a single space.
# Output format : For each test case,
# print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single
# space.
#
# Output for every test case will be printed in a seperate line.


from sys import stdin


def spiralPrint(mat, nRows, mCols):
    # Your code goes here
    result = []
    if len(mat) == 0:
        return result

    row_begin = 0
    row_end = nRows - 1
    col_begin = 0
    col_end = mCols - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            result.append(mat[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end + 1):
            result.append(mat[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                # print("col_end", col_end, "col_begin", col_begin)
                result.append(mat[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                result.append(mat[i][col_begin])
        col_begin += 1

    for i in result:
        print(i, end=" ")


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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
