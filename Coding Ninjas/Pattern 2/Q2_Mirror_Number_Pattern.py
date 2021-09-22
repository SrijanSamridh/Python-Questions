# Print the following pattern for the given N number of rows.
# Pattern for N = 4

# ...1
# ..12
# .123
# 1234

# The dots represent spaces.

# Input format :
# Integer N (Total no. of rows)
# Output format :
# Pattern in N lines

## Read input as specified in the question
## Print the required output in given format
n = int(input())
# number of spaces
k = n - 1
# outer loop to handle number of rows
for i in range(0, n):
    # inner loop to handle number spaces
    # values changing acc. to requirement
    for j in range(0, k):
        print("", end=" ")
    # decrementing k after each loop
    k = k - 1
    # inner loop to handle number of columns
    # values changing acc. to outer loop
    for j in range(0, i + 1):
        # printing stars
        print(j + 1, end="")
    # ending line after each row
    print("\r")
