# Print the following pattern for the given number of rows.
# Pattern for N = 5

# E
# DE
# CDE
# BCDE
# ABCDE

# Input format :
# N (Total no. of rows)

# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for i in range(1, n + 1):
    order = ord('A') + n - 1
    start_char = chr(order - i + 1)
    for j in range(1, i + 1):
        char = chr(ord(start_char) + j - 1)
        print(char, end='')
    print()
#         Code by Srijan Samridh
