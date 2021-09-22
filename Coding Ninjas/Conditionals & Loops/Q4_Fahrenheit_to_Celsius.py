# Given Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to
# convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print
# the table. Input Format : 3 integers - S, E and W respectively Output Format : Fahrenheit to Celsius conversion
# table. One line for every Fahrenheit and corresponding Celsius value. On Fahrenheit value and its corresponding
# Celsius value should be separate by tab ("\t")version table. One line for every Fahrenheit and corresponding
# Celsius value. On Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")


# Read input as specified in the question
# Print output as specified in the question

#	(Â°F â 32) Ã 5/9 = Â°C
#	C = (F-32)*5//9

S = int(input())
E = int(input())
W = int(input())
F = S
# C = (F-32)*5//9
# print(C)
for F in range(S, E + 1, W):
    C = int((F - 32) * 5 / 9)
    print(F, "", C)
