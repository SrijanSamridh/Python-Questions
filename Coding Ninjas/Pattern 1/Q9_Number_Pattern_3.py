# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# 1
# 11
# 121
# 1221

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("1", end='')
        else:
            print("2", end='')
    print()
#         Code by Srijan Samridh
