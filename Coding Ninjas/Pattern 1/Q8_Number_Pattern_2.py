# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# 1
# 11
# 202
# 3003

# Input format :
# Integer N (Total no. of rows)
# Contraints:
# 1 <= n <= 50

# Output format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
print(1)
for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0 or j == i:
            print(i, end='')
        else:
            print("0", end='')
    print()
