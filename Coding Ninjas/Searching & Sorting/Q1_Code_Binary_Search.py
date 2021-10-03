# You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X. Write a
# function to search this element in the given input array/list using 'Binary Search'. Return the index of the
# element in the input array/list. In case the element is not present in the array/list, then return -1.

# Input format
# : The first line contains an Integer 'N' which denotes the size of the array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.

# Third line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases
# follow..
# All the 't' lines henceforth, will take the value of X to be searched for in the array/list.

# Output Format :
# For each test case, print the index at which X is present, -1 otherwise.
#
# Output for every test case will be printed in a separate line.


from sys import stdin


def binarySearch(arr, n, x):
    low = 0
    high = n - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0:
    x = int(input().strip())
    print(binarySearch(arr, n, x))

    t -= 1
