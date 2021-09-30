# Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
# For example,
# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
# Input Format :
# Integer n
# Output Format :
# true or false


## Read input as specified in the question.
## Print output as specified in the question.
def len_num(number):
    count = 0
    while number != 0:
        number % 10
        number //= 10
        count += 1
    return count


def Am(number):
    num = number
    power = len_num(num)
    nums = []
    while num != 0:
        digit = num % 10
        nums.append(digit ** power)
        num //= 10
    if sum(nums) == number:
        return "true"
    else:
        return "false"


n = int(input())
print(Am(n))




