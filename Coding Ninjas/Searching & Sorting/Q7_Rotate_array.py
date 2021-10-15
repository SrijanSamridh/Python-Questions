# You have been given a random integer array/list(ARR) of size N. Write a function that rotates the given array/list
# by D elements(towards the left).

#  Note:
# Change in the input array/list itself. You don't need to return or print the elements.

# Input format : The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
# Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
#
# Third line contains the value of 'D' by which the array/list needs to be rotated.
# Output Format :
# For each test case, print the rotated array/list in a row separated by a single space.
#
# Output for every test case will be printed in a separate line.

def rotate(arr, n, d):
    # Your code goes here
    # arr[:] = arr[d:n] + arr[0:d]
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp


                            # One Line Code
def rotate(arr, n, d):
    # Your code goes here
    arr[:] = arr[d:n] + arr[0:d]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    n = int(li[0])
    d = int(li[1])
    
    if n == 0 :
        return list(), 0, 0
    
    arr = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return arr, n, d


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n, d = take2DInput()
    rotate(arr, n, d)

    t -= 1
