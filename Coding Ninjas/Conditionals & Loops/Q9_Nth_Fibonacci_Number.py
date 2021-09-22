# Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
#     F(n) = F(n-1) + F(n-2),
#     Where, F(1) = F(2) = 1

# Provided N you have to find out the Nth Fibonacci Number.
# Input Format :
# The first line of each test case contains a real number ‘N’.

# Output Format :
# For each test case, return its equivalent Fibonacci number.

## Read input as specified in the question.
## Print output as specified in the question.


n = int(input())
# print(fib(n))
f1 = 0
f2 = 1
f3 = 0
if n == 1:
    print(n)
else:
    i = 1
    while i < n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        # print(f3)
        i += 1
    print(f3)

# 1 1 2 3 5 8 13 21
