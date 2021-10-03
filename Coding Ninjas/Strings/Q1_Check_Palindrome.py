# Given a string, determine if it is a palindrome, considering only alphanumeric characters.
# Palindrome
# A palindrome is a word, number, phrase, or other sequences of characters which read the same backwards and forwards.

from sys import stdin


def isPalindrome(string):
    # Your code goes here
    rev = string[::-1]
    if rev == string:
        return True
    else:
        return False


# main
string = stdin.readline().strip();
ans = isPalindrome(string)

if ans:
    print('true')
else:
    print('false')
