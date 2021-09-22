# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# 1
# 11
# 111
# 1111

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(1, end='')
    print()
#         Code by Srijan Samridh
