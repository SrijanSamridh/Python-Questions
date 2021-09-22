# Print the following pattern for the given number of rows.
# Assume N is always odd.

# Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
n1 = (n // 2) + 1
n2 = n - n1
i = 1
while i <= n1:
    s = 1
    while s <= i - 1:
        print(" ", end="")
        s += 1
    j = 1
    while j <= i:
        print("* ", end="")
        j += 1
    print()
    i += 1
i = 1
while i <= n2:
    s = 1
    while s <= n2 - i:
        print(" ", end="")
        s += 1
    j = 1
    while j <= n2 - i + 1:
        print("* ", end="")
        j += 1
    print()
    i += 1
