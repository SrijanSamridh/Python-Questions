# Given an integer n, find if n is positive, negative or 0.
# If n is positive, print "Positive"
# If n is negative, print "Negative"
# And if n is equal to 0, print "Zero".

# Input Format :
# Integer n

# Output Format :
# "Positive" or "Negative" or "Zero" (without double quotes)

# Read input as specified in the question
# Print output as specified in the question
n = int(input())
if n == 0:
    print("Zero")
elif n < 0:
    print("Negative")
else:
    print("Positive")
