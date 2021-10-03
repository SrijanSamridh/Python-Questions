# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given
# string. The input string will remain unchanged if the given character(X) doesn't exist in the input string.

# Input Format:
# The first line of input contains a string without any leading and trailing spaces.
#
# The second line of input contains a character(X) without any leading and trailing spaces.
# Output Format:
# The only line of output prints the updated string.

from sys import stdin


def removeAllOccurrencesOfChar(string, ch):
    # Your code goes here
    str = ""
    for i in string:
        if i != ch:
            str += i
    return str


# main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]

ans = removeAllOccurrencesOfChar(string, ch)

print(ans)