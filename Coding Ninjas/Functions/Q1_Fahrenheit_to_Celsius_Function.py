# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert
# all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the
# table.
# Input Format : 3 integers - S, E and W respectively
# Output Format : Fahrenheit to Celsius conversion table.
# One line for every Fahrenheit and Celsius Fahrenheit value. Fahrenheit value and its corresponding Celsius value
# should be separate by tab ("\t")


def printTable(S, E, W):
    # Implement Your Code Here
    for F in range(S, E + 1, W):
        C = int((F - 32) * 5 / 9)
        print(F, "", C)


s = int(input())
e = int(input())
step = int(input())
printTable(s, e, step)




