# Print the following pattern
# Pattern for N = 4

# ...*
# ..***
# .*****
# *******
# The dots represent spaces.

# Input Format :
# N (Total no. of rows)

# Output Format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
k = n - 1
for i in range(0, n):

    # Spaces
    for j in range(0, k):
        print(" ", end='')
    k = k - 1

    # Increasing sqn
    for j in range(0, i + 1):
        # print("n", end="")
        print("*", end="")

    # Decreasing sqn
    temp = i
    for p in range(1, i + 1):
        print("*", end="")
        temp = temp - 1

    print("\r")
#         Code by Srijan Samridh
