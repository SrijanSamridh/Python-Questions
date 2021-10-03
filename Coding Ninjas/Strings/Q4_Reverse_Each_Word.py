# Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a
# function so as to print the sentence such that each word in the sentence is reversed.

# Example:
# Input Sentence: "Hello, I am Aadil!"
# The expected output will print, ",olleH I ma !lidaA".

# Input Format: The first and only line of input contains a string without any leading and trailing spaces. The input
# string represents the sentence given to Aadil.

# Output Format:
# The only line of output prints the sentence(string) such that each word in the sentence is reversed.

from sys import stdin


def reverseEachWord(string):
    # Your code goes here
    # Splitting the Sentence into list of words.
    words = string.split(" ")

    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]

    # Joining the new list of words
    # to for a new Sentence
    newString = " ".join(newWords)

    return newString


# main
string = stdin.readline().strip()

ans = reverseEachWord(string)

print(ans)