# Two random integer arrays/lists have been given as ARR1 and ARR2 of size N and M respectively. Both the
# arrays/lists contain numbers from 0 to 9(i.e. single digit integer is present at every index). The idea here is to
# represent each array/list as an integer in itself of digits N and M. You need to find the sum of both the input
# arrays/list treating them as two integers and put the result in another array/list i.e. output array/list will also
# contain only single digit at every index.

# Note:
# The sizes N and M can be different.
#
# Output array/list(of all 0s) has been provided as a function argument. Its size will always be one more than the
# size of the bigger array/list. Place 0 at the 0th index if there is no carry.
#
# No need to print the elements of the output array/list. Using the function "sumOfTwoArrays", write the solution to
# the problem and store the answer inside this output array/list. The main code will handle the printing of the
# output on its own.
#
# Input format : The first line contains an Integer 't' which denotes the number of test cases or
# queries to be run. Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#
# Second line contains 'N' single space separated integers representing the elements of the first array/list.
#
# Third line contains an integer 'M' representing the size of the second array/list.
#
# Fourth line contains 'M' single space separated integers representing the elements of the second array/list.
# Output Format :
# For each test case, print the required sum of the arrays/list in a row, separated by a single space.
#
# Output for every test case will be printed in a separate line.

from sys import stdin


def sumOfTwoArrays(arr1, n, arr2, m, output=None):
    # Your code goes here
    if output is None:
        output = []
    # filling the array having minimum length with Zeros
    if n > m:
        for i in range(n - m):
            arr2.insert(0, 0)
    else:
        for i in range(m - n):
            arr1.insert(0, 0)
    arr1.insert(0, 0)
    arr2.insert(0, 0)
    for i in range(len(arr1)):
        output.append(0)
    f = 0
    for i in range(len(arr1) - 1, -1, -1):
        x = arr1[i] + arr2[i] + f
        output[i] = (arr1[i] + arr2[i] + f) % 10
        if x > 9:
            f = 1
        else:
            f = 0
    # return output


# def sumOfTwoArrays(arr1, n, arr2, m, output):
#     # Your code goes here
#     i, j = 0, 0
#     carry = 0
#     output = []
#     while i<n and j<m:

#         Sum = arr1[i] + arr2[j] + carry
#         if Sum > 9:
#             output.insert(0, Sum%10)
#             carry = Sum//10
#         else:
#             output.insert(0, Sum)

# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


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

    outputSize = (1 + max(n, m))
    output = outputSize * [0]

    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)

    t -= 1