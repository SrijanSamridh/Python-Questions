# For a given a string(str), find and return the highest occurring character.
# Example:
# Input String: "abcdeapapqarr"

# Expected Output: 'a' Since 'a' has appeared four times in the string which happens to be the highest frequency
# character, the answer would be 'a'. If there are two characters in the input string with the same frequency,
# return the character which comes first.

# Consider:
# Assume all the characters in the given string to be in lowercase always.
# Input Format:
# The first and only line of input contains a string without any leading and trailing spaces.
# Output Format:
# The only line of output prints the updated string.


from sys import stdin


# def highestOccuringChar(string):
#     # Your code goes here
#     max_l = ""
#     max = 0
#     count = 0
#     for i in range(len(string)):
#         for j in string:
#             if j == string[i]:
#                 count += 1
#         if count > max:
#             max = count
#             max_l = j
#             count = 0
#     return max_l

def highestOccuringChar(string):
    ASCII_SIZE = 256
    ctr = [0] * ASCII_SIZE
    max = -1
    ch = ''
    for i in string:
        ctr[ord(i)] += 1

    for i in string:
        if max < ctr[ord(i)]:
            max = ctr[ord(i)]
            ch = i
    return ch


# main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)
