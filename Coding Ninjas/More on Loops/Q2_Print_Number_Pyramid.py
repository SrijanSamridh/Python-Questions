# Print the following pattern for a given n.
# For eg. N = 6

# 123456
#   23456
#     3456
#       456
#         56
#           6
#         56
#       456
#     3456
#   23456
# 123456

# Sample Input 1 :
# 4

# Sample Output 1 :
# 1234
#   234
#     34
#       4
#     34
#   234
# 1234


## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
up = n
low = n - 1

for up in range(1, n + 1):

    for s in range(1, up):
        print(' ', end='')

    for p in range(up, n + 1):
        print(p, end="")

    print("\r")

for low in range(1, n):

    for s in range(1, n - low):
        print(' ', end='')

    for p in range(n - low, n + 1):
        print(p, end="")

    print("\r")
