# Print the following pattern for the given number of rows.
# Pattern for N = 4

# 1111
# 000
# 11
# 0

# Input format : N (Total no. of rows)

# Output format : Pattern in N lines

# Sample Input :
# 5
n = int(input())
for i in range(1,n+1):
    if i%2 != 0: # if the row is odd as it starts from 1
        for j in range(n-i+1):
            print("1", end="")
    else: # if the row is even it comes to else
        for j in range(n-i+1):
            print("0", end="")
    print()