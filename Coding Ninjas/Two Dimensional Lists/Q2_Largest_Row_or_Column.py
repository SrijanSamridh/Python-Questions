# For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the
# largest sum(sum of all the elements in a row/column) amongst all the rows and columns.
#
# Note : If there are more
# than one rows/columns with maximum sum, consider the row/column that comes first. And if ith row and jth column has
# the same largest sum, consider the ith row as answer.

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
# For each test case, If row sum is maximum, then print: "row" <row_index> <row_sum>
# OR
# If column sum is maximum, then print: "column" <col_index> <col_sum>
# It will be printed in a single line separated by a single space between each piece of information.
#
# Output for every test case will be printed in a seperate line.


"""
    In order to print two or more integers in a line separated by a single
    space then you may consider printing it with the statement,

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

"""

from sys import stdin


def findLargest(arr, nRows, mCols):
    # Your code goes here
    n = nRows
    m = mCols

    max_row_sum = 0
    max_row_index = 0
    row_sum = [sum(x) for x in arr]
    for i in range(len(row_sum)):
        if row_sum[i] > max_row_sum:
            max_row_sum = row_sum[i]
            max_row_index = i

    max_col_sum = 0
    max_col_index = 0
    for j in range(m):
        col_sum = 0
        for ele in arr:
            col_sum += ele[j]
        if col_sum > max_col_sum:
            max_col_sum = col_sum
            max_col_index = j
    if max_col_sum == 0 and max_row_sum == 0:
        print("row", max_row_index, -2147483648)
        exit()
    elif max_col_sum > max_row_sum:
        print("column", max_col_index, max_col_sum)
    else:
        print("row", max_row_index, max_row_sum)


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
    findLargest(mat, nRows, mCols)

    t -= 1
