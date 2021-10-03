# Write a program to do basic string compression. For a character which is consecutively repeated more than once,
# replace consecutive duplicate occurrences with the count of repetitions.

# Example:
# If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".
#
# The string is compressed only when the repeated character count is more than 1.
# Note:
# Consecutive count of every character in the input string is less than or equal to 9.
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# Output Format:
# The output contains the string after compression printed in single line.

from sys import stdin


def getCompressedString(string):
    # Write your code here.
    res = ""

    count = 1

    # Add in first character
    res += string[0]

    # Iterate through loop, skipping last one
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            if count > 1:
                # Ignore if no repeats
                res += str(count)
            res += string[i + 1]
            count = 1
    # print last one
    if count > 1:
        res += str(count)
    return res


# Main.
string = stdin.readline().strip()
ans = getCompressedString(string)
print(ans)
