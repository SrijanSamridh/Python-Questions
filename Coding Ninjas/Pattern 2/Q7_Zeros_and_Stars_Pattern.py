# Print the following pattern
# Pattern for N = 4
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

# Input Format :
# N (Total no. of rows)

# Output Format :
# Pattern in N lines

## Read input as specified in the question.
## Print output as specified in the question.

                            # With "While Loop"
n = int(input())

i = 1
j = 1
while i <= n:
    j = 1
    while j <= n:
        if i == j:
            print('*', end="")
        else:
            print('0', end="")
        j += 1
    j -= 1
    print('*', end="")

    while j > 0:
        if i == j:
            print('*', end="")
        else:
            print('0', end="")
        j -= 1
    print()
    i += 1
#         Code by Srijan Samridh



                                    # With "For Loop"
for i in range(n):
    for j in range(n):
        if i == j:
            print("*", end="")
        else:
            print("0", end="")
            
    print("*", end="")
    
    for j in range(n-1, -1, -1):
        if i == j:
            print("*", end="")
        else:
            print("0", end="")
    print()
    
    
    
