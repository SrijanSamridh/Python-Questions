# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# 1234
# 123
# 12
# 1

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
