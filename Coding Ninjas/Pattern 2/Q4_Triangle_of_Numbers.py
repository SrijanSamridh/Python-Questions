# Print the following pattern for the given number of rows.
# Pattern for N = 4

# ...1
# ..232
# .34543
# 4567654
# The dots represent spaces.

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
l = 0
m = 0
for i in range(n):
    for s in range(n - (i + 1)):
        print(" ", end="")
    for j in range(i + 1):
        print(j + i + 1, end="")
    for k in range(i):
        print(l, end="")
        l -= 1
    l = m = m + 2
    print()
