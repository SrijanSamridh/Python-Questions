# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
# Input format :
#  Integer N
# Output format :
# Sum_of_Even_Digits Sum_of_Odd_Digits
# (Print first even sum and then odd sum separated by space)

## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
num = int(input())
even = 0
odd = 0
s = num % 10
while num > 0:
    s = num % 10
    if s % 2 == 0:
        even = even + s
    else:
        odd = odd + s
    num = num // 10

print(even, odd)
