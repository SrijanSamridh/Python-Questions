# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
# Sample Input 1 :
# 121
# Sample Output 1 :
# true

def reverse(num):
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num


def checkPalindrome(num):
    # Implement Your Code Here
    if reverse(num) == num:
        return True
    else:
        return False


num = int(input())
isPalindrome = checkPalindrome(num)
if isPalindrome:
    print('true')
else:
    print('false')
