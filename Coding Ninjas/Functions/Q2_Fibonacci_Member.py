# Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of
# fibonacci series else false. Fibonacci Series is defined by the recurrence F(n) = F(n-1) + F(n-2) where F(0) = 0
# and F(1) = 1
#
#
# Input Format :
# Integer N
# Output Format :
# true or false

def checkMember(n):
    # Implement Your Code Here
    f1 = 0
    f2 = 1
    ch = 0
    if n == 0 or n == 1:
        return True
    else:
        while ch < n:
            ch = f1 + f2
            f1 = f2
            f2 = ch
        if ch == n:
            return True
        else:
            return False


n = int(input())
if checkMember(n):
    print("true")
else:
    print("false")
