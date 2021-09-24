# Print the following pattern for the given number of rows.
# Note: N is always odd.
#
#
# Pattern for N = 5
#   *
#  ***
# *****
#  ***
#   *

# The dots represent spaces.

# Input format :
# N (Total no. of rows and can only be odd)
# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
N = int(input())
n1 = (N + 1) // 2
n2 = n1 - 1
for i in range(1, n1 + 1):

    for spaces in range(n1 - i, 0, -1):
        print(" ", end="")

    for j in range(0, 2 * i - 1):
        print("*", end="")
    print("\r")

for i in range(n2, 0, -1):

    for spaces in range(0, n2 - i + 1):
        print(" ", end="")

    for j in range(0, 2 * i - 1):
        print("*", end="")
    print("\r")