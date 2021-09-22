# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# 4444
# 4444
# 4444
# 4444

# Input format :
# Integer N (Total no. of rows)

# Output format :
# Pattern in N lines


n = int(input())

# print("Square pattern is: ")
for i in range(1, n+1):
    for j in range(1, n+1):
        print(n, end="")
    print()
    #         Code by Srijan Samridh
