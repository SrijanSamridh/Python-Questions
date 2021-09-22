# Given an integer n, find and print the sum of numbers from 1 to n.
# Note : Use while loop only.

# Input Format :
# Integer n

# Output Format :
# Sum

# Read input as specified in the question
# Print output as specified in the question
n = int(input())
i = 1
Sum = 0
while i <= n:
    Sum = Sum + i
    i += 1

print(Sum)
