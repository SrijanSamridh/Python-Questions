# Print the following pattern for the given number of rows.

# Pattern for N = 4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

# Input format : N (Total no. of rows)
#
# Output format : Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
# number of rows and columns to be printed
s = 2 * n - 1

# Upper Half
for i in range(0, (s // 2) + 1):

    m = n

    # Decreasing part
    for j in range(0, i):
        print(m, end="")
        m -= 1

    # Conatsant Part
    for k in range(0, s - 2 * i):
        print(n - i, end="")

    # Increasing part.
    m = n - i + 1
    for l in range(0, i):
        print(m, end="")
        m += 1

    print("\r")

# Lower Half
for i in range((s // 2) - 1, -1, -1):

    # Decreasing Part
    m = n
    for j in range(0, i):
        print(m, end="")
        m -= 1

    # Constant Part.
    for k in range(0, s - 2 * i):
        print(n - i, end="")

    # Decreasing Part
    m = n - i + 1
    for l in range(0, i):
        print(m, end="")
        m += 1

    print("\r")
