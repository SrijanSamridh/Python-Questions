# For a given string(str), remove all the consecutive duplicate characters.
# Example:
# Input String: "aaaa"
# Expected Output: "a"
#
# Input String: "aabbbcc"
# Expected Output: "abc"

# Input Format: The first and only line of input contains a string without any leading and trailing spaces. All the
# characters in the string would be in lower case.

# Output Format:
# The only line of output prints the updated string.

from sys import stdin


def removeConsecutiveDuplicates(string):
    # Your code goes here
    seen = string[0]
    ans = string[0]
    for i in string[1:]:
        if i != seen:
            ans += i
            seen = i
    return ans
    # str = ""
    # if len(string) <= 1:
    #     return string
    # else:
    #     for i in range(len(string)):
    #         if string[i] not in str:
    #             str += string[i]
    #     return str


# main
string = stdin.readline().strip()

ans = removeConsecutiveDuplicates(string)

print(ans)