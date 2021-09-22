# Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
# 1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
# 2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
# 3. If the input is 3, then 2 integers are taken from the user and their product is printed.
# 4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
# 6. If the input is 6, then the program exits.
# 7. For any other input, then print "Invalid Operation".

# Note: Each answer in next line.
# Input format:
# Take integers as input, in accordance to the description of the question.

# Constraints:
# Time Limit: 1 second

# Output format:
# The output lines must be as prescribed in the description of the question.

# Write your code here
while True:
    terms = int(input())
    # val1 = int(input())
    # val2 = int(input())
    if terms == 1:
        c = int(input()) + int(input())
        print(c)
    if terms == 2:
        c = int(input()) - int(input())
        print(c)
    elif terms == 3:
        c = int(input()) * int(input())
        print(c)
    elif terms == 4:
        c = int(input()) // int(input())
        print(c)
    elif terms == 5:
        c = int(input()) % int(input())
        print(c)
    elif terms == 6:
        break
    elif terms > 6:
        c = "Invalid Operation"
        print(c)
