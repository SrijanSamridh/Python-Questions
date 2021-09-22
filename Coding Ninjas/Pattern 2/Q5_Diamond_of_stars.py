# Print the following pattern for the given number of rows.
# Note: N is always odd.

# Pattern for N = 5
#   *
#  ***
# *****
#  ***
#   *

# Input format :
# N (Total no. of rows and can only be odd)
# Output format :
# Pattern in N lines


n = int(input())
currRow = 1

# Upper half
while currRow <= (n // 2) + 1:

    # This tells us the number of spaces to give.
    spaces = 1
    while spaces <= (n // 2) + 1 - currRow:
        print(" ", end="", sep='')
        spaces += 1

    currCol = 1
    # This tells us the number of stars for current row.
    while currCol <= (2 * currRow) - 1:
        print("*", end="", sep='')
        currCol += 1

    print()
    currRow += 1

currRow = 1

# Lower half
while currRow <= n // 2:

    # This tells us the number of spaces to give.
    spaces = 1
    while spaces <= currRow:
        print(" ", end="", sep='')
        spaces += 1

    currCol = 2 * ((n // 2) - currRow + 1) - 1

    # This tells us the number of stars for current row.
    while currCol >= 1:
        print("*", end="", sep='')
        currCol -= 1

    print()
    currRow += 1
#         Code by Srijan Samridh
